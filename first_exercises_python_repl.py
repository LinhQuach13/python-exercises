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
#Answer: I would predict it would produce an error 
# because it is trying to operate on a string and an integer. You cannot
# perform operations on two data types. My answer was correct and returned a
# TypeError: can only concatenate str (not "int") to str.

6 % 4
# I would predict that it would return 1.5 because this operator includes the remainder when 
# the numbers are divided. The answer was 2 because the answer was returned as an integer data type
# and not a float data type thus the answer was rounded.
    
type(6 % 4)
# Answer: I would predict the integer data type would be returned and this answer is correct.

type(type(6 % 4))
# Answer: I would predict this might return and error. The answer was it returned the data type as type and
# researching into this it seems that because type is passed as the argument in the type function it returns 
# type as the data type.

'3 + 4 is ' + 3 + 4
#Answer: I would predict an error would occur because it is trying to combine two different data types.
# and this answer was correct an TypeError: can only concatenate str (not "int") to str was returned.

0 < 0
# Answer: I would predict this would return false because 0 is not larger than 0 and this is correct. 

'False' == False
# Answer: I would predict this would return false because it is comparing a string and a boolean data
# type which are not equal to eachother. This prediction was correct.

True == 'True'
# Answer: I would predict this would return false because it is comparing a string and a boolean data
# type which are not equal to eachother. This prediction was correct.

5 >= -5
# Answer: This would return true because positive 5 is larger than or equal to negative five.
# My prediction was correct.

True or "42"
#Answer: I would predict this would return True because as long as either condition is met 
# it will return True. My prediction was correct.

6 % 5
#Answer: I would predict it will return 1 because this is division with a remainder. In this case
# it would equal 1.2 and due to it being the integer data type it will round to 1.

5 < 4 and 1 == 1
# Answer:  I would predict false would be returned because 5 is not less than 4 as the the operator 
# is wanting the opposite. The operator 1 == 1 is correct but due to the first condition not being met
# then it will return false. My prediction was correct.

'codeup' == 'codeup' and 'codeup' == 'Codeup'
# Answer:  I predict this would return false because although the first operation is correct the second one
# is not and both must be correct to return true. My prediction was correct.

4 >= 0 and 1 !== '1'
# Answer: I would predict this would return an error because in the second operation is comparing
# two different data types and this is not valid syntax. My prediction was correct.

6 % 3 == 0
# Answer: I would predict this is true because 6/3 will not have a remainder thus == 0.
#My prediction was correct.

5 % 2 != 0
# Answer: I would predict this is true because 5/2 will have a remainder thus will not == 0
# as operator suggest in the statement. My prediction was correct.

[1] + 2
#Answer: I would predict this would produce an error because [1] is a list data type
# and 2 is an integer data type. You cannot perform operations on two different data types. 
#My prediction was correct and produced this error TypeError: can only concatenate list (not "int") to list


[1] + [2]
# Answer: I would predict this would concatenate the lists data types together and
# my answer was correct.

[1] * 2
# Answer: I would predict this would produce and error because you cannot perform an operation
#between two different data types. In this case my prediction was not correct 
# because it return 1 twice in a list due to it being re-assigned.
# The multiplication operator allows the variable to reference themselves due to this reassignment.
# Further explanation: It makes two lists, it literally multiple the quantity of lists with the same values.
# The integer 2 lets python concat the list to itself twice.


[1] * [2]
# Answer: I would have predict this might produce and error because it's referencing two list variables.
#Python will not run this because [2] is not an integer and lists variables cannot be multiplied
#by eachother.
# This resulted in an error message TypeError: can't multiply sequence by non-int of type 'list'.

[] + [] == []
# Answer: I would predict this would return true because a list plus a list will equal a list. 
#My prediction was correct.

{} + {}
# Answer: I would predict this might not work because this is not how you combine dictionaries.
# My prediction was correct in it would not work because the error resulted was
#  TypeError: unsupported operand type(s) for +: 'dict' and 'dict'


  