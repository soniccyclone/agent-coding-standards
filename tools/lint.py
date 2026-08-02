#!/usr/bin/env python3
"""Phase 6 lint for the OKF bundle.

Spec: technical-plan.md Phase 6. Not a one-time pass -- a recurring check,
which is why it lives in the repo rather than in a scratch directory.

Usage:  python3 tools/lint.py            # report
        python3 tools/lint.py --quiet    # exit 1 on findings, print nothing
"""
import re
import sys
import pathlib
import collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUNDLE = ROOT / 'bundle'

AXES = {'expressiveness', 'verifiability', 'parallelizability',
        'hardware-affinity', 'cognitive-load', 'primitive-count'}
SUBDOMAINS = {'algorithms-and-complexity', 'databases-and-data-management',
              'distributed-systems-and-concurrency', 'formal-methods-and-verification',
              'foundations-of-computation', 'operating-systems-and-systems-programming',
              'programming-environments-and-object-systems',
              'programming-languages-and-semantics', 'software-engineering-and-architecture'}


def frontmatter(text):
    if not text.startswith('---'):
        return {}
    end = text.find('\n---', 3)
    if end < 0:
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r'^([a-z_]+):\s*(.*)$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def listval(v):
    return [x.strip().strip('"\'') for x in v.strip('[]').split(',') if x.strip()]


def main():
    findings = collections.OrderedDict()

    def add(key, items):
        if items:
            findings[key] = items

    figures = sorted(p for p in (BUNDLE / 'figures').iterdir() if p.is_dir())
    lessons = sorted((BUNDLE / 'figures').glob('*/lessons/*.md'))
    works = sorted((BUNDLE / 'figures').glob('*/works/*.md'))
    tensions = [p for p in (BUNDLE / 'tensions').glob('*.md') if p.stem != 'index']

    # --- figures with no lessons
    add('figures with no lessons',
        [f.name for f in figures if not list(f.glob('lessons/*.md'))])

    # --- duplicate figures (same display title under two dirs)
    titles = collections.defaultdict(list)
    for f in figures:
        idx = f / 'index.md'
        if idx.exists():
            t = frontmatter(idx.read_text()).get('title', '').strip('"').lower()
            if t:
                titles[t].append(f.name)
    add('duplicate figure titles',
        [f'{t}: {dirs}' for t, dirs in titles.items() if len(dirs) > 1])

    # --- lessons missing / mis-tagging axes and subdomains
    no_axis, no_sub, bad_axis, bad_sub, no_src, bad_title = [], [], [], [], [], []
    for p in lessons:
        text = p.read_text()
        fm = frontmatter(text)
        rel = f'{p.parent.parent.name}/{p.stem}'
        ax, sb = listval(fm.get('axes', '')), listval(fm.get('subdomains', ''))
        if not ax:
            no_axis.append(rel)
        if not sb:
            no_sub.append(rel)
        for a in ax:
            if a not in AXES:
                bad_axis.append(f'{rel}: {a}')
        for s in sb:
            if s not in SUBDOMAINS:
                bad_sub.append(f'{rel}: {s}')
        if '**Source:**' not in text:
            no_src.append(rel)
        # rebuild-backlinks.py only matches double-quoted titles
        if not re.search(r'^title: ".*"$', text, re.M):
            bad_title.append(rel)
    add('lessons with no axis', no_axis)
    add('lessons with no subdomain', no_sub)
    add('invalid axis values', bad_axis)
    add('invalid subdomain values', bad_sub)
    add('lessons with no **Source:** line', no_src)
    add('lesson titles not double-quoted (breaks shared indexes)', bad_title)

    # --- orphan lessons: not linked from their work file
    linked = set()
    for w in works:
        for m in re.finditer(r'\]\(\.\./lessons/([^)]+)\.md\)', w.read_text()):
            linked.add(f'{w.parent.parent.name}/{m.group(1)}')
    add('lessons not linked from any work file',
        [f'{p.parent.parent.name}/{p.stem}' for p in lessons
         if f'{p.parent.parent.name}/{p.stem}' not in linked])

    # --- axis/subdomain backlinks out of sync with lesson tags
    for kind, valid in (('axes', AXES), ('subdomains', SUBDOMAINS)):
        want = collections.defaultdict(set)
        for p in lessons:
            fm = frontmatter(p.read_text())
            for v in listval(fm.get(kind, '')):
                if v in valid:
                    want[v].add(f'{p.parent.parent.name}/{p.stem}')
        drift = []
        for v in sorted(valid):
            f = BUNDLE / kind / f'{v}.md'
            if not f.exists():
                drift.append(f'{v}: file missing')
                continue
            have = set()
            for m in re.finditer(r'\]\(\.\./figures/([^/]+)/lessons/([^)]+)\.md\)', f.read_text()):
                have.add(f'{m.group(1)}/{m.group(2)}')
            miss, extra = want[v] - have, have - want[v]
            if miss or extra:
                drift.append(f'{v}: {len(miss)} tagged-but-unlisted, {len(extra)} listed-but-untagged')
        add(f'{kind} backlink drift', drift)

    # --- broken relative links, bundle-wide
    broken = []
    for p in BUNDLE.rglob('*.md'):
        for m in re.finditer(r'\]\((?!https?:|#)([^)]+\.md)[^)]*\)', p.read_text()):
            if not (p.parent / m.group(1)).exists():
                broken.append(f'{p.relative_to(ROOT)} -> {m.group(1)}')
    add('broken internal links', broken)

    # --- works: attestation and source reachability
    unattested = []
    for w in works:
        text = w.read_text()
        if 'extraction: complete' not in text and 'SOURCE-UNOBTAINABLE' not in text:
            unattested.append(f'{w.parent.parent.name}/{w.stem}')
    add('works neither attested nor marked unobtainable', unattested)

    add('works with no url', [f'{w.parent.parent.name}/{w.stem}' for w in works
                             if not frontmatter(w.read_text()).get('url')])

    # --- tensions left open
    add('tensions still status: open',
        [p.stem for p in tensions if 'status: open' in p.read_text()])

    # --- report
    if '--quiet' in sys.argv:
        return 1 if findings else 0

    print(f'OKF bundle lint — {len(figures)} figures, {len(works)} works, '
          f'{len(lessons)} lessons, {len(tensions)} tensions\n')
    if not findings:
        print('CLEAN — no findings.')
        return 0
    for k, items in findings.items():
        print(f'[{len(items):4d}] {k}')
        for i in items[:8]:
            print(f'         {i}')
        if len(items) > 8:
            print(f'         ... and {len(items) - 8} more')
        print()
    print(f'{sum(len(v) for v in findings.values())} findings in {len(findings)} categories.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
