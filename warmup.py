# Exercise #1
# write the code to take a string and produce a dictionary out of 
# that string such that the output looks like the following: Some thoughts:

# You'll need a way to get the first part of the 
# string and a way to get the second part of the string
# Feel free to make new variables/data types 
# in between the string and the output dictionary
# Input truck = "toyota tacoma"

#Output

# #truck = {
#     "make": "toyota",
#     "model": "tacoma"
# }


truck = "Toyota Tacoma"

make_and_model= truck.split()

make= make_and_model[0]
model= make_and_model[1]

truck= {
  "make": make,
  "model": model,
}

print(truck)


sedan = "Kia Rio"
m_and_m= sedan.split()
make= m_and_m[0]
model= m_and_m[1]

print(m_and_m)


sports_car = "Mustang GT"
m_and_m= sports_car.split()
make= m_and_m[0]
model= m_and_m[1]

print(m_and_m)
        

# Exercise #2
# Write the code that takes a dictionary containing make/model for 
# a vehicle and capitalizes the first character of the make and the model:
# Input
# truck = {
#     "make": "toyota",
#     "model": "tacoma"
# }
# Output

# truck = {
#     "make": "Toyota",
#     "model": "Tacoma"
# }

truck = {
    "make": "toyota",
    "model": "tacoma"
}
truck['make'] = truck["make"].title()
truck['model'] = truck["model"].title()

sedan = {
    "make": "kia",
    "model": "rio"
}

sedan['make'] = sedan["make"].title()
sedan['model'] = sedan["model"].title()

sports_car = {
    "make": "mustang",
    "model": "gt"
}


sports_car['make'] = sports_car["make"].title()
sports_car['model'] = sports_car["model"].title()



# Exercise #3
# Create a list of 3 dictionaries where each dictionary represents a 
# vehicle, as above Write the code 
# that operates on that list of dictionaries in 
# order to uppercase the entire make and model values.
# Input
# truck = {
#     "make": "Toyota",
#     "model": "Tacoma"
# }
# Output

# truck = {
#     "make": "TOYOTA",
#     "model": "TACOMA"
# }

truck = {
    "make": "toyota",
    "model": "tacoma"
}
truck['make'] = truck["make"].upper()
truck['model'] = truck["model"].upper()

sedan = {
    "make": "kia",
    "model": "rio"
}

sedan['make'] = sedan["make"].upper()
sedan['model'] = sedan["model"].upper()


sports_car = {
    "make": "mustang",
    "model": "gt"
}

sports_car['make'] = sports_car["make"].upper()
sports_car['model'] = sports_car["model"].upper()