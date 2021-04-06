# Exercises
#  For this exercise, you will be working mostly in the python (or ipython) REPL. 
# You are not required to create a file for this exercise, but are encouraged to in order to 
# play around with the concepts you are learning.


# Identify the data type of the following values:

99.9
type(99.9)
    #Answer: float
"False"
type("False")
    #Answer: string

False
type(False)
    #Answer: boolean
'0'
type('0')
    #Answer: string
0
type(0)
    #Answer: Integer
True
type(True)
    #Answer: boolean
'True'
    #Answer: string
[{}]
type([{}])
    #Answer: list
{'a': []}
type({'a': []})
    #Answer: dictionary



# What data type would best represent:

# A term or phrase typed into a search box?
   #Answer: string

# If a user is logged in?
    #Answer: boolean

# A discount amount to apply to a user's shopping cart?
    #Answer: float

# Whether or not a coupon code is valid?
    #Answer: boolean

# An email address typed into a registration form?
    #Answer: string

# The price of a product?
    #Answer: float

# A Matrix?
    #Answer: list 

# The email addresses collected from a registration form?
    #Answer: string

# Information about applicants to Codeup's data science program?
    #Answer: dictionary



# For each of the following code blocks, read the expression 
# and predict what the result of evaluating it would be, then execute the expression in your Python REPL.

'1' + 2
#Answer: I would guees it would produce an error becasue it is comparing a string and an integer. You cannot
# perform operations on two data types.

6 % 4
    
type(6 % 4)

type(type(6 % 4))

'3 + 4 is ' + 3 + 4

0 < 0

'False' == False

True == 'True'

5 >= -5

True or "42"

6 % 5

5 < 4 and 1 == 1

'codeup' == 'codeup' and 'codeup' == 'Codeup'

4 >= 0 and 1 !== '1'

6 % 3 == 0

5 % 2 != 0

[1] + 2

[1] + [2]

[1] * 2

[1] * [2]

[] + [] == []

{} + {}