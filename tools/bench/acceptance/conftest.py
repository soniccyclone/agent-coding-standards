import pytest

ROUNDS = ("round1", "round2", "round3", "round4")


def pytest_configure(config):
    for r in ROUNDS:
        config.addinivalue_line("markers", f"{r}: checks that round's requirements")


@pytest.fixture(autouse=True)
def _fail_fast_on_hang():
    """Nothing here should be slow; a hung queue is a failure, not a wait."""
    yield
