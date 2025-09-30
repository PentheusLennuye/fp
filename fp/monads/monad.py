"""
monad.py contains the Monad Base Class
"""

from copy import deepcopy
from typing import Callable, Self

class Monad:
    """Base Class"""
    def __init__(self):
        self._keys = []

    @staticmethod
    def unit(**kwargs):
        """
        Wrap the type into this monad. Fulfills the left identity law.
        a -> M a.
        """
        m = Monad()
        for k, v in kwargs.items():
            setattr(m, k, v)
            m._keys.append(k)  # pylint: disable=protected-access
        return m

    def identity(self) -> Self:
        """Return myself. Fulfills the right identity law."""
        return self

    def unwrap(self):
        """Return the original type. M a -> a."""
        result = {}
        for k in self._keys:
            result[k] = getattr(self, k)
        return result

    def bind(self, f: Callable, *args, **kwargs) -> Self:
        """
        Apply the function f to the monad. What the Monad pushes to the function
        and how it reacts to the results of the function is up to the writer.

        To ensure associativity, bind returns a copy of itself to be chained.

        This stub bind function does nothing before and after the call.
        """
        self._pre()
        f(*args, **kwargs)
        self._post()
        return deepcopy(self)

    def _pre(self):
        return

    def _post(self):
        return

    def __rshift__(self, f: Callable, *args, **kwargs) -> Self:
        """
        >> is a Haskell-like bind operator. It makes chained code easier to
        read.
        """
        return self.bind(f, *args, **kwargs)
