# 20 Python Data Structure Manipulation Exercises
# The following questions reference the students data structure below. 
# Write the python code to answer the following questions:

# 1. How many students are there?
len(students)


# 2. How many students prefer light coffee? For each type of coffee roast?
pref_light = []
pref_med = []
pref_dark = []
for student in students:
    if student.get("coffee_preference")== "light":
        pref_light.append(student)
print(len(pref_light))

for student in students:
    if student.get("coffee_preference")== "medium":
        pref_med.append(student)
print(len(pref_med))

for student in students:
    if student.get("coffee_preference")== "dark":
        pref_dark.append(student)
print(len(pref_dark))




# 3. How many types of each pet are there?
horses= []
dogs= []
cats=[]
for student in students:
    pets= student['pets']
    for species in pets:
        pet_spc= species['species']
        if pet_spc == 'horse':
            horses.append(pet_spc)
        if pet_spc == 'dog':
            dogs.append(pet_spc)
        if pet_spc == 'cat':
            cats.append(pet_spc)
            
            
print((f'Number of horses= {len(horses)}'))
print((f'Number of dogs= {len(dogs)}'))
print((f'Number of cats= {len(cats)}'))




# 4. How many grades does each student have? Do they all have the
#  same number of grades?
for student in students:
    number_of_grades= len(student["grades"])
    print(f"{student['student']} has {number_of_grades} grades")
print(f"All students have the same amount of grades")



# 5. What is each student's grade average?
for student in students:
    grade_avg= sum(student['grades'])/len(student['grades'])
    print(f"{student['student']} has a grade average of {grade_avg}")



# 6. How many pets does each student have?
pet_list= []
for student in students:
    number_of_pets= len(student['pets'])
    print(f"{student['student']} has {number_of_pets} pets")



# 7. How many students are in web development? data science?
web_stu = 0
for student in students:
    if student['course'] == 'web development':
        web_stu += 1
print('There are', (web_stu), ' web development students.')

DS_stu = 0
for student in students:
    if student['course'] == 'data science':
        DS_stu += 1
print('There are', (DS_stu), ' data science students.')



# 8. What is the average number of pets for students in 
# web development?
web_stu = 0
pets = 0
for student in students:
    if student['course'] == 'web development':
        web_stu += 1
        pets += len(student['pets'])
print('Web Development students have an average of ', (pets / web_stu), ' pets.')



# 9. What is the average pet age for students in data science?
total_age= 0 
number_pt= 0
for student in students:
    if student['course']== 'data science':
        pets = student['pets']
        for pet in pets:
            total_age += pet['age']
            number_pt+= 1
            avg= int(total_age/number_pets)
print("The avg pet age for students in data science is", avg)


#  10. What is most frequent coffee preference for data science students?
light= 0 
medium= 0
dark= 0
for student in students:
    if student['course']== 'data science':
        if student.get("coffee_preference")== "light":
            light+= 1
        elif student.get("coffee_preference")== "medium":
            medium+=1
        elif student.get("coffee_preference")== "dark":
            dark+=1
coffee_choices= dict(light= light, medium= medium, dark= dark)
coffee_preference= max(coffee_choices, key=coffee_choices.get)

print(coffee_preference)



# 11. What is the least frequent coffee preference 
# for web development students?


# 12. What is the average grade for students with at least 2 pets?



# 13. How many students have 3 pets?



# 14. What is the average grade for students with 0 pets?
# 15. What is the average grade for web development students? data science students?
# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# 17. What is the average number of pets for medium coffee drinkers?
# 18. What is the most common type of pet for web development students?
# 19. What is the average name length?
# 20. What is the highest pet age for light coffee drinkers?

# students.py

students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]