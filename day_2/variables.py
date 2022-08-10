# Day2: 30 Days of python programming

# Declare a first name variable and assign a value to it
from math import floor


firstname = 'wahaha'
print('firstname:' + firstname)

# Declare a last name variable and assign a value to it
lastname = 'guolicheng'
print('lastname:' + lastname)

# Declare a full name variable and assign a value to it
fullname = 'wahaha guolicheng'
print('fullname:' + fullname)

# Declare a country variable and assign a value to it
country = 'Japan'
print('country:' + country)

# Declare a city variable and assign a value to it
city = 'Tokyo'
print('city:' + city)

# Declare an age variable and assign a value to it
age = 20
print('age:' + str(age))    # int can not cancate with str directly. it needs to transfer int into a str

# Declare a year variable and assign a value to it
year = 2022
print('year:' + str(year))

# Declare a variable is_married and assign a value to it
is_married = False  # different from java, boolean should be uppercase
print('is_married:' + str(is_married))

# Declare a variable is_true and assign a value to it
is_true = True
print('is_true:' + str(is_true))

# Declare a variable is_light_on and assign a value to it
is_light_on = False
print('is_light_on:' + str(is_light_on))

# Declare multiple variable on one line
first_variable, second_variable = 'wahaha', 18
print('first:' + first_variable + ' second:' + str(second_variable))

# Using the _len()_ built-in function find the length of your first name
print('len-first:' + str(len(first_variable)))

# Compare the length of your first name and your last name
print(max(firstname, lastname))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# 1. Add num_one and num_two and assign the value to a variable \_total
_total = num_one + num_two
print('_total:' + str(_total))

# 2. Subtract num_two from num_one and assign the value to a variable \_diff
_diff = num_one - num_two
print('_diff:' + str(_diff))

# 3. Multiply num_two and num_one and assign the value to a variable \_product
_product = num_one * num_two
print('_product:' + str(_product))

# 4. Divide num_one by num_two and assign the value to a variable \_division
_division = num_one / num_two
print('_division:' + str(_division))

# 5. Use modulus division to find num_two divided by num_one and assign the value to a variable \_remainder
_remainder = num_two // num_one
print('_remainder:' + str(_remainder))

# 6. Calculate num_one to the power of num_two and assign the value to a variable \_exp
_exp = pow(num_one, num_two)
print('_exp:' + str(_exp))

# 18. The radius of a circle is 30 meters.
radius = 3

# 1. Calculate the area of a circle and assign the value to a variable _area_of_circle_
_area_of_circle_ = 3.14 * radius * radius
print('_area_of_circle_:' + str(_area_of_circle_))


# 2. Calculate the circumference of a circle and assign the value to a variable _circum_of_circle_
_circum_of_circle_ = 2 * 3.14 * radius
print('_circum_of_circle_:' + str(_circum_of_circle_))

# 3. Take radius as user input and calculate the area.
input_radius = int(input('Please input radius: ')) # it is necessary to do type casting, because input param is a str
print('area is :' + str(input_radius * input_radius * 3.14))

