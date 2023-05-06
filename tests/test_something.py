from test_github_actions.something import foo
from hypothesis.strategies import decimals
from hypothesis import given


@given(decimals(-1000, 1000))
def test_foo(param):
    assert foo(param) == 2 * param
