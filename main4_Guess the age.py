"""
In this stage, you will introduce yourself to the bot.
It will greet you by your name and then try to guess your age using arithmetic operations.

Your program should print the following lines:

Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
Your age is {your_age}; that's a good time to start programming!
Read three numbers from the standard input. Assume that all the numbers will be given on separate lines.

Instead of {your_age}, the bot will print the age determined according to the special formula discussed above.

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

"""

print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is {}; that's a good time to start programming!".format(age))
print('Now I will prove to you that I can count to any number you want.')
number = int(input())
i = 0
while i <= number:
    print(str(i)+" !")
    i = i + 1

print('Completed, have a nice day!')
