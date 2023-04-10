"""Wow! This problem is kind of tricky.
The function closest_higher_mod_5
takes exactly one integer argument x and returns the smallest integer y such that:

y is greater than or equal to x,
y is divisible by 5.

Correct the last line of the code below to make the function work.

Tip: Try to think about how the variable remainder might be useful to you.

def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    return "I don't know :("
"""


def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    return x + 5 - remainder


