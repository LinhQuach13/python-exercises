# Create a Python script file named data_types_and_variables.py. 

# Inside it, write some Python code, that is, variables and operators, 
# to describe the following scenarios. Do not worry about the real operations to get the values, 
# the goal of these exercises is to understand how real world conditions can be represented with code.


# You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and 
# Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?
    # Answer: $27.00
    lm=3
    bb= 5
    h= 1
    total = (lm + bb + h) * 3
    print(total)


# Another way to do example above:
little_mermaid = 3
brother_bear = 5
hercules = 1
price_per_day = 3
total_price= price_per_day * (little_mermaid + brother_bear + hercules)
print(total_price)
    

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, 
# and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
    # Answer: $7,420.00 will be the payment for the week.
google= (400 *6)
amazon= (380 * 4)
facebook= (350 * 10)
total_pay = google + amazon + facebook
print(total_pay)


# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.
    #Answer
class_is_not_full= True
conflict= False
student_can_enroll= class_is_not_full and not conflict
print(student_can_enroll)

# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to
#  buy a specific amount of products.
more_than_2_items_bought= True
expired= False
premium_membership= True
product_offer_valid= more_than_2_items_bought and not expired or premium_membership and not expired
print(product_offer_valid)

# Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
    #Answer:
ps_len = len(password) >= 5
usr_len =len(username) < 21
ps_not_usr= username != password

usr_and_ps_valid = ps_len and usr_len and ps_not_usr

print (usr_and_ps_valid)


# bonus neither the username or password can start or end with whitespace
pw_len_stuff = len(password) >= 5
var_len_stuff =len(username) < 21
pw_not_usr= username != password
user_no_space= not (username.startswith(' ') or username[-1] == ' ' )
pw_no_space= not (password.startswith(' ') or password[-1] ==  ' ')

usr_and_pw_valid = pw_len_suff and usr_len_stuff and pw_not_user and user_no_space and pw_no_space

print(user_and_pw_valid)