"""
tests/test_monad.py: Testing the Monad class.

- A monad must have an identity function M a -> M a.
- A monad must have a wrap function a -> M a.
- A monad's bound functions must be associative, i.e. the effect on the monad's
  wrapped type is the same whether (a -> b)-> c or a -> (b -> c).
  This cannot be tested here as the Monad interface uses abstract classes.
- A monad must have an unwrap function M a -> a.
"""

from pytest import raises
from unittest import TestCase
from unittest.mock import Mock

from fp.monads.monad import Monad

class TestInterface(TestCase):
    def setUp(self):
        self.m = Monad.unit(key="value")

    def test_unit(self):
        assert self.m.key == "value"

    #def test_unwrap(self):
    #    assert self.m.unwrap() == {"key": "value"}

    #def test_bind_runs_a_function_and_returns_a_monad(self):
    #    myfunction = Mock()
    #    result = self.m.bind(myfunction)
    #    myfunction.assert_called_once_with(key="value")
    #    assert result.key == "value"

        # Sometimes >> (__rshift__) is useful for chaining operations
        #def true() -> bool:

    def test_identity(self):
        assert self.m.identity() == self.m
