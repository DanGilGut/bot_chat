"""
For the first stage, you will write a bot who displays a greeting,
its name, and the date of its creation. First impressions count!

Your program should print the following lines:

Hello! My name is {bot_name}.
I was created in {birth_year}.
Instead of {bot_name}, print any name you choose and replace {birth_year} with the current year (four digits).
"""
import datetime
print("Hello! My name is {}.\nI was created in {}.".format("Dani", datetime.datetime.now().year))