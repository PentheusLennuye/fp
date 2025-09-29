"""
monad.py contains the Monad Base Class
"""

from typing import Callable, Self

class Monad:
    """Base Class"""
    def __init__(self):
        self._keys = []

    @staticmethod
    def unit(**kwargs):
        m = Monad()
        for k, v in kwargs.items():
            setattr(m, k, v)
            m._keys.append(k)
        return m

    def identity(self) -> Self:
        return self

    def unwrap(self):
        result = {}
        for k in self._keys:
            result[k] = getattr(self, k)
        return result

    def bind(self, f: Callable) -> Self:
        args = self.unwrap()
        f(**args)
        return type(self).unit(**args)

    def __rshift__(self, f: Callable) -> Self:
        """
        >> is a Haskell-like bind operator. It makes chained code easier to
        read.
        """
        args = self.unwrap()
        f(**args)
        return type(self).unit(**args)
        
        