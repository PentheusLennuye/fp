# Additional Functional Programming Concepts

## Adding Functional Programming Benefits to Python

This project adds functional programming helpers up and beyond (and sometimes
parallels) Python function programming libraries.

For example, this repository includes monadic patterns such as State, Reader,
Maybe and Writer monads. In the case of Pipeline (my name for what might be a
common pattern AFAIK), it incorporates all three to ensure chaining of logged
functions.

Of interest are the IO monads. This permits something akin to JavaScript's
"promise": a side effect will return a predictable value. This permits
dependency injection^1 of a side effect such as a system call or random number.
No side effect, means the function is predicatable and testable.

## Project layout

```text
mkdocs.yml    # The configuration file.
docs/
    index.md  # The documentation homepage.
    ...       # Other markdown pages, images and other files.
fp/
    monads/
```

^1: That is to say, making the internal call an argument instead.
