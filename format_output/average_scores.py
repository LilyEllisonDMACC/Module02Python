"""
Program: average_scores.py
Author: Lily Ellison
Last date modified: 01/20/2023

The purpose of this program is to accept user's name (first and last), age, and a constant number of scores,
calculate the average of the scores, and print out this information in a statement like:
Rodriguez, Linda age: 21 average grade: 92.50

"""

"""
Pseudo-code/comments included
"""

#store a constant for the number of scores for user to input: 4
NUMBER_OF_SCORES = 4


#prompt user for last_name and store as last_name
last_name = input("Please enter your last name: ")

#prompt for first_name and store as first_name
first_name = input("Please enter your first name: ")

#prompt for age and store as age
age = input("Please enter your age: ")

#prompt user for scores - either separate or a running total - constant times
score01 = float(input("Please enter your first score: "))
score02 = float(input("Please enter your second score: "))
score03 = float(input("Please enter your third score: "))
score04 = float(input("Please enter your fourth score: "))

#calculate average - sum and divide by number of values

average = (score01 + score02 + score03 + score04)/NUMBER_OF_SCORES

#print output; like:
#Rodriguez, Linda age: 21 average grade: 92.50

print(f'{last_name}, {first_name} age: {age} average grade: {average: 5.2f}')

"""
I tried this by concatination first and found that I needed to convert the float of average back to a string.
I didn't like that because I wanted to control the decimal precision at the print line. I much prefer this F
statement way of outputting info.
I ran several random inputs and got accurate results.
It does throw an error when a non-number is entered as a score, but I assume we will address this when we get
into loops. I imagine something that says "if score01 is not a number, ask for score01 again" written into the 
code would help.
"""

