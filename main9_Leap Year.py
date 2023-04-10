"""Write a program that checks if a year is leap.
A year is considered leap if it is divisible by 4
and NOT divisible by 100,
or if it is divisible by 400.

So, 2000 is leap and 2100 isn't.

Output either "Leap" or "Ordinary" depending on the input."""

print("Introduce  un año: ")
ano = int(input())

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("Leap")
else:
    print("Ordinary")