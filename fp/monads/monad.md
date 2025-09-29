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

 Consider the chicken, lettuce, sauce, bacon -- and now bacteria. Together, they
 compose type `a`. The function that puts the wrap around type `a` is called
 the _unit_ function. `a -> M a`  (_M_ for monad, obviously).

 >![ASIDE] In category theory, an arrow -> represents a function. The lower-case
 >letters represent types. Our type here in Python might be a class with
 >attributes _self.chicken_, _self.lettuce_ and so on. On the other hand, it
 >might be a dictionary with keys chicken, lettuce, etc. Or a quintuple. The
 >upper-case letters represent a _category_, which is a collection of valid
 >functions and types. So M (Monad) is a category.

 On occasion, you might want to look in your bag to see that small package in
 the bottom is still a wrap and not, say, a melted chocolate bar. Checking on
 the wrap won't affect its contents. The function that identifies the monad and
 doesn't affect _a_ is, well, the _identity function_. `M a -> M a`.

## Binding

 If you carry the wrap around your bag all day, things happen to the ingredients
 in the wrap. Maybe it's a hot day and lunch was delayed. One _binds_ the
 function _apply_heat_ to the monad and the monad applies the results of the
 function to its ingredients. Using _f_ to represent the function _apply
 heat_ (remember in functional programming, a function signature is a type):
 `M a -> f -> M -> M a`.

 M does not change, and type _a_ remains type _a_, although its held values can
 change. In the case of our chicken wrap, the wrap increases the bacteria
 count, liquifies the lettuce, poisons the sauce, ignores the bacon, and turns
 the chicken an unfortunate colour.

## Unwrapping

You should not know what happened to the contents of the monad until you
_unwrap_ it. Until you unwrap Schroedinger's Chicken Wrap, it is simultaneously
healthy and unhealthy to eat. But once unwrapped, `M a -> a`, you can look and
smell at the results and balance your immediate hunger against your future
health.

Of course, there are no private attributes in Python but try to keep discipline.

## The Three Laws of Monads

A monad, to be classified as a category in Category Theory, must conform to:

- The _left identity law_: the _unit_ function that takes type a and returns M
  a. What do you get when you wrap chicken, lettuce, sauce, bacon and an
  inevitable starting bacteria count in a wrap? You get a chicken wrap.
- The _right identity law_: the _identity_ function explained above. Am I a
  chicken wrap? Why, yes I am.
- The _associative law_: changing the grouping of functions bound to the monad
  do not change the final outcome.
  
Chicken Wrap -> (squishing -> heating) -> flipping -> Chicken Wrap = \
Chicken Wrap -> squishing -> (heating -> flipping) -> Chicken Wrap.

Note that a change in order can change the outcome (heating before squishing
might not increase the bacteria count so much), but the grouping cannot.

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
