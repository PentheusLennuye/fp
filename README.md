# FP Functional Programming

This project adds functional programming helpers up and beyond (and sometimes
parallels) Python function programming concepts.

For example, this includes monadic patterns such as State, Reader, Maybe and
Writer monads. In the case of Pipeline, it incorporates all three to ensure
chaining of logged functions.

Of interest are the IO monads. This permits a "promise": a side effect will
return a predictable value. This permits dependency injection^1 of a side effect
such as a system call or random number. No side effect, means the function is
predicatable and testable.

^1: That is to say, making the internal call an argument instead.
