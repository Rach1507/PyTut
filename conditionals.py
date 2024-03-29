# conditionals
# the print statement is executed if the statement after if evaluates to true
# make sure we have everything to be eexecute if the conditional is true to be intended ahead
#

if True:
    print('Conditional is true')

if False:
    print('Conditional is true')  # not executed

lang = 'py'
if lang == 'py':
    print('lang is py')

# == means checking equality
# = is assignment
#  >=
# <=
# >
# <
# !=
# Object identity : is
# is is used to know if two values have same id or if they re the same object in  memory
lang = 'java'
if lang == 'py':
    print('lang is py')
else:
    print('Lang is not py')

lang = 'c'
if lang == 'py':
    print('lang is py')
elif lang == 'java':
    print('lang is java')
else:
    print('no match')


# and , or , not

user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('Admin page')
else:
    print("bad creds")

user = 'admin'
logged_in = False

if not logged_in:
    print('Please login')
else:
    print("hey there")

user = 'admin'
logged_in = False


if user == 'admin' or logged_in:
    print('Admin page')
else:
    print("bad creds")

# Admin page
# Please login
# Admin page
# because user == admin is true so it doesnt matter logged_in is true or false
#  this isn't any expression , it just is switching btw true and false
#


# object identity
a= [1,2,3]
b = [1,2,3]

print(a == b)

# output : True ,coz two lists are equal



print(a is b) # identity operator
# False, because they are 2 diff objects in m/m
# how do we know that, we can print out these 2 ids using built function id

print(id(a), id(b))
print(id(a) == id(b))

# 13163528 20603784 , these ids are diff, coz they're diff objects in mm
# False


b=a
print(a is b)
print(a == b)
# True , coz they are same obj in m/m
# so behind the scenes , "a is b " is same as saying "id(a) == id(b)"



'''False Values: all the things in python that evaluates to true
    False
    None without ''
    Zero of any numeric type
    Any empty sequence. For example, '', (), [].
    Any empty mapping. For example, {}'''


condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Evaluated to False

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Evaluated to False

condition = 0

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Evaluated to False

condition = 10

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Evaluated to True

condition = ''   # empty string

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Evaluated to False

condition = 'hi'   # any string with chars evaluates to true

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Evaluated to True


#  Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}

condition = []  # any string with chars evaluates to true

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# Evaluated to False