"""
In this stage, you will introduce yourself to the bot so that it can greet you by your name.

Your program should print the following lines:

Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
What a great name you have, {your_name}!
You may change the name and the creation year of your bot if you want.

Instead of {your_name}, the bot must print your name entered from the standard input.
"""

print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

# reading a name
user = input()
print('What a great name you have, {}!'.format(user))