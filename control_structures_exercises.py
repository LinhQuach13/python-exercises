# Do your work for this exercise in a file named control_structures_exercises.py.

# 1. Conditional Basics

# a. prompt the user for a day of the week, print out whether 
# the day is Monday or not
message = ("1= Monday, 2= Tuesday, 3=Wednesday, 4= Thursday, \n5= Friday, 6= Saturday, 7= Sunday")
print(message)
day = int(input("Enter day of week in number form (1-7) : "))

if day == 1 :
    print("\nMonday");
else :
    print("\nIt is not monday")


# b. prompt the user for a day of the week, print out 
# whether the day is a weekday or a weekend
message = ("1= Monday, 2= Tuesday, 3=Wednesday, 4= Thursday, \n5= Friday, 6= Saturday, 7= Sunday")
print(message)
day = int(input("Enter day of week in number form (1-7) : "))

if day == 1 or 2 or 3 or 4 or 5:
    print("\nIt is a weekday.");
else :
    print("\nIt is a weekend")


# c. create variables and make up values for
# -the number of hours worked in one week
# -the hourly rate
# -how much the week's paycheck will be
# -write the python code that calculates the weekly paycheck. 
# -You get paid time and a half if you work more than 40 hours
number_hours_worked= 40
overtime= 2
hourly_rate= 50
overtime_rate= 75
this_week_paycheck = (number_hours_worked * hourly_rate) + (overtime * overtime_rate)
print(this_week_paycheck)



# 2. Loop Basics

# a. While

# -Create an integer variable i with a value of 5.
# -Create a while loop that runs so long as i is less than or equal to 15
# -Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

# -Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.
i = 0
while i < 101:
    print(i)
    i += 2

# -Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i += -5

# -Create a while loop that starts at 2, and displays the number 
# squared on each line while the number is less than 1,000,000. 
# Output should equal:
# -Write a loop that uses print to create the output shown below.
i = 2
while i < 1_000_000:
    print(i)
    i **= 2

#  Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i += -5



# b. For Loops

# i. Write some code that prompts the user for a number, 
#then shows a multiplication table up through 10 for that number.
p_num = input('Please insert a positive integer ')
p_num = (int(proposed_num))
for n in range(1,11):
    print(f'{proposed_num} X {n} = {p_num *n}')

# ii. Create a for loop that uses print to create the output shown below.
for n in range(1,10):
    print(str(n) * n)


# c. break and continue

# i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement 
# to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop 
# and the continue statement 
# to output all the odd numbers between 1 and 50, except for the number the user entered.
while True:
    pos_num = input('Please insert an odd number between 1 and 50: ')
    if pos_num.isdigit():
        if int(pos_num) % 2 == 1 and int(pos_num) <= 50:
            break

pos_num = int (pos_num)
for num in range(1,50,2):
    if num == pos_num:
        print ('Skipping number: ', num)
    else:
        print('Here is an odd number: ', num)

# d. The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that
#  counts from 0 to that number. (Hints: first make sure 
# that the value the user entered is a valid number, also note that
#  the input function returns a string, so you'll need to convert this to a numeric type.)
while True:
    pos_num = input('Please insert a positive number: ')
    if pos_num.isdigit():
        if int(pos_num) > 0:
            break
pos_num = int(pos_num)
for num in range(0, pos_num + 1):
    print(num)


# e. Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.
while True:
    pos_num = input('Please insert a positive number: ')
    if pos_num.isdigit():
        if int(pos_num) > 0:
            break
pos_num = int(pos_num)
for num in range(pos_num, 0, -1):
    print(num)




# 3. Fizzbuzz
# -One of the most common interview questions for entry-level programmers 
# -is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# -Write a program that prints the numbers from 1 to 100.
# -For multiples of three print "Fizz" instead of the number
# -For the multiples of five print "Buzz".
# -For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 101):
    if i % 3 ==0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)




# 4. Display a table of powers.
# -Prompt the user to enter an integer.
# -Display a table of squares and cubes from 1 to the value entered.
# -Ask if the user wants to continue.
# -Assume that the user will enter valid data.
#- Only continue if the user agrees to.
while True:
    pos_num = input('Please insert a positive integer: ')
    if pos_num.isdigit():
        if int(pos_num) > 0:
            break
proceed = input('Do you want to continue and print a table of powers? :')
if proceed.lower().startswith('y'):
    pos_num= int(pos_num)
    print()
    print('number | squared | cubed')
    print('------ | ------ | -----')
    for i in range(1, pos_num +1):
        i_squared = i ** 2
        i_cubed = i ** 3
        print(f' {i: 6} | {i_squared: 7} | {i_cubed: 5}')



# 5. Convert given number grades into letter grades.
    # -Prompt the user for a numerical grade from 0 to 100.
    # -Display the corresponding letter grade.
    # -Prompt the user to continue.
    #-Assume that the user will enter valid integers for the grades.
    #- The application should only continue if the user agrees to.
    #- Grade Ranges:

    # A : 100 - 88
    # B : 87 - 80
    # C : 79 - 67
    # D : 66 - 60
    # F : 59 - 0
while True:
    grade = input("Please enter a numerical between 0 and 100: ")
    if grade.isdigit():
        grade = int(grade)
        if grade <0 or grade> 100:
            continue
        break
if grade in range(60):
    grade = 'F'
elif grade in range(60,67):
    grade = 'D'
elif grade in range (67,80):
    grade = 'C'
elif grade in range (80, 88):
    grade = 'B'
else:
    grade = 'A'
print(grade)
    


    #Bonus

#Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
#Create a list of dictionaries where each dictionary represents 
#a book that you have read. Each dictionary in the list should have the keys title, 
# author, and genre. Loop through the list and print out information about each book.
#Prompt the user to enter a genre, then loop through your books list and 
# print out the titles of all the books in that genre.
bookshelf = [
    {'title': 'Annihilation',
    'author': 'Jeff Vandermeer',
    'genre': 'Science Fiction'},
    {'title': 'Octopus Pie',
    'author': 'Maredeth Gran',
    'genre': 'Comic'},
    {'title': 'Cabin At the End of the World',
    'author': 'Paul Tremblay',
    'genre': 'Horror'},
    {'title': 'Severance',
    'author': 'Ling Ma',
    'genre': 'Science Fiction'},
]

for book in bookshelf:
    [print(key,': ', book[key]) for key in book]

picked_genre = input('Please pick a genre: ')

genre_from_shelf= []
for book in bookshelf:
    if book['genre'].lower() == picked_genre.lower():
        genre_from_shelf.append(book['title'])
if genre_from_shelf == []:
    print("No books in this genre")
else:
    print(f'I have the following titles in the genre {picked_genre}:')
    [print(result) for result in genre_from_shelf]