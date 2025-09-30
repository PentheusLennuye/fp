# The Monad: Schroedinger's Chicken Wrap

A monad at first glance is related to a Python decorator. Like the decorator,
it wraps a function within another function. However, unlike a decorator, a
monad does not return the results of the funcion. It only returns its own
attributes, probably modified by the results of wrapped function, and only
when it is asked to.

Think of it like this: a monad is Schroedinger's Chicken Wrap. You take
chicken, lettuce, sauce, and possibly bacon if your culture permits it. Then
you stuff it in a wrap instead of the safe Schroedinger dreamed around his
cat. Then the chicken, lettuce, sauce, and bacon are affected by one or more
functions with the same signature. However, unlike Schroedinger's Cat, who
might be affected by the radiation source _inside_ its safe, Schroedinger's
Chicken Wrap is affected by _outside_ influences.

## Identity and Unit Functions

Consider the chicken, lettuce, sauce, and bacon. Together, they compose type
$a$. The function that puts the wrap around type $a$ is called the _unit_
function. $a \rightarrow M a$  (_M_ for monad, obviously).

>![ASIDE] In category theory, an arrow -> represents a function. The lower-case
>letters represent types. Our type here in Python might be a class with
>attributes _self.chicken_, _self.lettuce_ and so on. On the other hand, it
>might be a dictionary with keys chicken, lettuce, etc. Or a quintuple. The
>upper-case letters represent a _category_, which is a collection of valid
>functions and types. So M (Monad) is a category.

On occasion, you might want to look in your bag to see that small package in
the bottom is still a wrap and not, say, a melted chocolate bar. Checking on
the wrap won't affect its contents. The function that identifies the monad and
doesn't affect _a_ is, well, the _identity function_. $M a \rightarrow M a$.

## Binding

If you carry the wrap around your bag all day, things happen to the ingredients
in the wrap. Maybe it's a hot day and lunch was delayed. One _binds_ the
function _apply_heat_ to the monad:

1. The monad sends the ingredients to _apply_heat_
2. _apply_heat_ does terrible things to the ingredients
3. _apply_heat_ returns the ingredients to the wrap. 

Using _f_ to represent the function _apply heat_ (remember in functional
programming, a function signature is a type): $M a \rightarrow (a \rightarrow f)
\rightarrow M a$

M does not change, and type _a_ remains type _a_, although the values _a_ holds
may change courtesy of function _f_. In the case of our chicken wrap, the bound
function _f_ liquifies the lettuce, poisons the sauce, ignores the bacon, and
turns the chicken an unfortunate colour.

## Unwrapping

You should not know what happened to the contents of the monad until you
_unwrap_ it. Until you unwrap Schroedinger's Chicken Wrap, it is simultaneously
healthy and unhealthy to eat. But once unwrapped, $M a \rightarrow a$, you can
look and smell at the results and balance your immediate hunger against your
future health.

Of course, there are no private attributes in Python but try to keep discipline.

## The Three Laws of Monads

A monad, to be classified as a category in Category Theory, must conform to:

- The _left identity law_: the _unit_ function that takes type a and returns M
  a. What do you get when you wrap chicken, lettuce, sauce, bacon and an
  inevitable starting bacteria count in a wrap? You get a chicken wrap.
- The _right identity law_: the _identity_ function explained above. Am I a
  chicken wrap? Why, yes I am.
- The _associative law_: changing the grouping of functions bound to the monad
  does not change the final outcome.

This last law needs some clarification. What if I chain a division function and
an addition function? After all, $(3/2) + 1 \ne 3 / (2 + 1)$.

Let's look at the bind function again but this time we will use Python rather
than category theory and keep it simple enough to be practically useless:

```python
from types import None, Self
from functools import reduce
class Monad:
    def __init__(self) -> None:
        self.hidden = None
    
    def identity(self) -> Self:
        return self

    def unit(self, **kwargs) -> Monad:
        return Monad().hidden = kwargs

    def bind(f: Callable) -> Monad:
        result = f(**self.unwrap())
        if self._type_changed(result):
            raise KeyError(f"{f.__name__} changed type")

    def _type_changed(result: dict) -> int:
        return sum(k not in result for k, _ in self.hidden.items()):

    def unwrap(self):
        return self.hidden


m = Monad.unit(x=1)
m.bind(lambda x: x)
```

The short form of the bind is `M a -> (a -> M b) -> M b`. Note that this is not
category theory. Here _a_ and _b_ represent different values of the same type.
The bound function is in the parentheses: `(a -> M b)`.

Now, let's do some associative checks. We want to show that `(M.bind(f)).bind(g)
= M.bind((f).bind(g))`

From the short form above, the left association $(M(f) \rightarrow M b$ 

In the example above, the monad isn't doing anything particularly awesome. In
reality, the monad will have additional attributes and methods to react to
the results of the bound functions. For example, maybe the wrap changes colour
every time a function is bound.

Chicken Wrap -> (squishing -> heating) -> flipping -> Chicken Wrap = \
Chicken Wrap -> squishing -> (heating -> flipping) -> Chicken Wrap.

Note that a change in order can change the outcome (heating before squishing
might not increase the bacteria count so much), but the grouping cannot.

Thanks to Graham Joncas at <https://gjoncas.github.io/posts/2020-05-30-monad-associativity-law.html> for explaining associativity.
`M -> M a -> (a -> M b) -> M b`

This is up to the writer. For example a monad that wraps type _float_ with value
3.0 and then operates three functions `divide(x: float)` -> `add(x: float)` is
not associative at all. (3.0 / 2.0) + 1.0 += 3.0 / (2.0 + 1.0)

## So What?

Why this is so interesting and valuable is up to the monad writer. The contents
of this directory presents practical examples. But first, we will create the
Monad base class.

This sounds weird, because monads are very much a part of functional
programming, and a class is, well, object-oriented.

We must use classes. Python does not offer structures and interfaces. We'll
create the base class without attributes, and use _abc.ABCMeta_ to make it a
formal interface. Python uses duck-typing, so we can go ahead and use _**kwargs_
to convert arguments into attributes and vice-versa rather than using templates.

The code is in [monad.py](monad.py)
