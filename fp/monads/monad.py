# fp.monads.monad
#
# A monad is related to a Python decorator in that it wraps a function within
# another function. However, a monad does not return the results of the funcion.
# It returns a copy of itself, with its attributes modified by the results of
# that function.
#
# A monad is Schroedinger's chicken wrap. You take chicken, lettuce, sauce, and
# possibly bacon if your culture permits it. Then you stuff it in the wrap.
#
# Consider the chicken, lettuce, sauce, bacon, and bacteria count as _type_ a.
# The wrap with _type a_ is _type m a_ (_m_ for monad, obviously).
#
# On occasion, you want to look in your bag to see that small package in the
# bottom is still a wrap. The monadic function that identifies itself is, well,
# the _identity function_.
#
# You can carry the wrap around your bag and things happen to the ingredients of
# of the wrap. Maybe it's a hot day and lunch was delayed. Once _binds_ the
# function of heating the wrap to the monad. The monad, once processing the
# as well. _m a_ -> (heat_without_escape -> a) -> _m a_.
#
# You do not know the contents of the wrap until you unwrap it. To you, it is
# simultaneously healthy and unhealthy to eat. _m a_ -> _a_.
#
# A monad, to conform to Category Theory, must have:
# - an identity function, a map (or unwrap)