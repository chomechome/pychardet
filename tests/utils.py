import pytest


def skip(*params, reason=None):
    return pytest.param(*params, marks=pytest.mark.skip(reason=reason))
