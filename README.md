# Operators

> A program that allows you to use digits and operators as functions.

## Example

```py
# Instead of this
result = 3 + 2

# You can write that
result = three(plus(two()))
```

Operators supported: `plus`, `minus`, `times`, `divided_by`, `power` and `modulo`.

The number functions go to `zero` to `ten`. Note that these are not constants, but functions.

## Why I made this

I discovered this challenge on [CodeWars](https://codewars.com/), but I had no idea how to proceed. Then I thought about default arguments, so I tried and surprisingly, it works.

This project is not intended to be used in production, it is just a challenge to learn tricks about operators and default arguments.
