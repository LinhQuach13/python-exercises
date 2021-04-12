# Create a file named function_exercises.py for this exercise. 
# After creating each function specified below, write the necessary code in order to test your function.

# 1. Define a function named is_two. It should accept one input and return True 
# if the passed input is either the number or the string 2, False otherwise.
def is_two(n):
    if n == 2 or n == '2':
        return True
    else:
        return False


# 2. Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.
def is_vowel(word):
    vowels = set('AaEeIiOoUu')
    return any(ch in vowels for ch in word.lower())


#3. Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.
def is_consonant(word):
    vowels = set('AaEeIiOoUu')
    return any(ch not in vowels for ch in word.lower())


# 4. Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of 
# the word if the word starts with a consonant.
def capitalize(w):
    vowels = set('AaEeIiOoUu')
    if w not in vowels:
        return w.title()


#5. Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.
tip_percentage= input('Please enter tip percentage between 0.00 and 0.01: ')
bill_total = input('Please put in total of bill ')
def calculate_tip():
    total_tip= float(bill_total) * float(tip_percentage)
    return total_tip



#6. Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, disc_percentage):
    discount= float(original_price) * float(disc_percentage)
    total= float(original_price) - float(discount)
    return(total)


#7. Define a function named handle_commas. It should 
# accept a string that is a number that contains commas in it as input, 
#  and return a number as output.
def handle_commas(s):
    s = s.replace(',', '')
    return s



#8. Define a function named get_letter_grade. It should accept a number
#  and return the letter grade associated with that number (A-F).
def get_letter_grade(score):
    score = int(score)
    if  score >= 90: 
        return "A"
    if  90 > score >= 80: 
        return "B"
    if  80 > score >= 70: 
        return "C"
    if  70 > score >= 60: 
        return "D"
    if  60 > score: 
        return "F"
    

#9. Define a function named remove_vowels that accepts a string 
# and returns a string with all the vowels removed.
def remove_vowels(text):
    for vowel in "aeiouAEIOU":
        text = ''.join(text.split(vowel))
    return text



#10. Define a function named normalize_name. It should accept a string and 
# return a valid python identifier, that is:
#- anything that is not a valid python identifier should be removed

#- leading and trailing whitespace should be removed

#- everything should be lowercase

#- spaces should be replaced with underscores

#- for example:
        # Name will become name
        # First Name will become first_name
        # % Completed will become completed

def normalize_name(s):
    
    s = s.replace(' ','_')
    s = re.sub('[^0-9a-zA-Z_]', '', s)
    
    
    s = re.sub('^[^a-zA-Z]+', '', s)
    s = s.lower()
    return s


#11. Write a function named cumulative_sum that accepts a list of numbers and 
# returns a list that is the cumulative sum of the numbers in the list.
        #cumulative_sum([1, 1, 1]) returns [1, 2, 3]
        #cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(nums_list):
    return [sum(nums_list[:i+1]) for i in range(len(nums_list))]

# Bonus
# Create a function named twelveto24. It should accept a string in the format 10:45am or 
# 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.