from hypothesis import given
from hypothesis.strategies import decimals

from test_github_actions.something import foo


@given(decimals(-1000, 1000))
def test_foo(param: int):
    assert foo(param) == 2 * param
