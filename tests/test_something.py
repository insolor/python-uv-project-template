from hypothesis import given
from hypothesis.strategies import decimals

from python_uv_project_template.something import foo


@given(decimals(-1000, 1000))
def test_foo(param: int):
    assert foo(param) == 2 * param
