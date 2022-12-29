# Lec123-124-Ch7Ex1-CipherSchools.py
#cube finder
def cube_finder(n):
    cubes={}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes

print(cube_finder(10))


# Lec125-WordCounterDictionary-CipherSchools.py
# word counter
def word_counter(s):
    count={}
    for char in s:
        count[char] = s.count(char)
    return count
print(word_counter('harshit'))


# Lec126-127-Ch7Ex2-CipherSchools.py

user={}
name=input('What is your name : ')
age=input('What is your age')
fav_movies=input('your fac movies separated by comma').split(",")
fav_songs=input('your fac songs separated by comma').split(",")

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
# print(user)
for key,value in user.items():
    print(f"{key} : {value}")


# Lec128-DictonarySummary-CipherSchools.py
# summary dictionary
# what is dictionary
# unordered collection of data

d={'name' : 'harshit', 'age' : 24}

# or
d1=dict(name = 'harshit',age = 24)

# or

d2={
    'name' : 'harshit', 
    'age' : 24,
    'fav_movies' : []
}



print(d['name'])


# add data inside empty dict
empty_dict={}
empty_dict['key1'] = 'value1'
empty_dict['key2'] = 'value2'

print(d.get('names'))

popped = d.popitem()
print(popped)
print(d)


Lec129-IntroToSets-CipherSchools.py
# set data type
# unordered collection of unique items

s={1,2,3}

s={1,1.0,2.3, 'string'} #cannot store list and dictionary in it

print(s)


# Lec130-MoreAboutSets-CipherSchools.py
# in keyword in sets and for loop

s = {'a', 'b', 'c'}

# in keyword to check if item is present or not in set
if 'a' in s:
    print("present")
else:
    print("not present")

# for loop
for item in s:
    print(item)
# set maths
s1={1,2,3,4}
s2={3,4,5,6}

print(s1 & s2)

 
# Lec131-ListComprehension-CipherSchools.py

names = ['Harshit', 'Mohit', 'Rohit']

new_list2 = [name[0] for name in names]
print(new_list2)




  
# Lec132-133-Ch9Ex1-CipherSchools.py

def reverse_strings(l):
    return [name[::-1] for name in l]

print(reverse_strings(['abc', 'tuv', 'xyz']))

def reverse_str(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return new_list

print(reverse_strings(['abc', 'tuv', 'xyz']))


# Lec134-ListsComprehensionWithIfStatement-CipherSchools.py

# list comprehension with if statement

numbers = list(range(1,11))
# [1,2,3,4,5,6,7,8,9,10]
# even_nums = [2,4,6]
nums = []
for i in numbers:
    if i%2==0 :
        nums.append(i)
print(nums)

even_nums = [i for i in numbers if i%2==0]
even_nums2 = [i for i in range(1,11) if i%2==0]
print(even_nums)
print(even_nums2)
odd_nums =  [i for i  in range(1,11) if i%2!=0]
print(odd_nums)


Lec135-136-Ch9Ex2-CipherSchools.py

def num_to_string(l):
    return [str(i) for i in l if (type(i) == int or type(i) == float)]


print(num_to_string([True, False , [1,2,3], 1, 1.0, 3]))


# Lec137-List comprehension with if else-CipherSchools.py
# list comprehension with if else
nums = [1,2,3,4,5,6,7,8,9,10]
# new_list = [-1,4, -3, 8]

new_list = []
for i in nums:
    if i%2 == 0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)

new_list2 = [i*2 if (i%2 == 0) else -i for  i in nums]
print(new_list2)


# Lec138-Nested list comprehension-CipherSchools.py

# list comprehension in nested list

example = [[1,2,3],[1,2,3],[1,2,3]]

nested_comp = [[i for i in range(1,4)] for j in range(3)]
print(nested_comp)

new_list = []
for j in range(3):
    new_list.append([1,2,3])



# Lec139-Chapter 9 Summary-CipherSchools.py
# LIST COMPREHENSIOM SUMMARY

nl = [[1,2,3], [1,2,3], [1,2,3]]
new_list = [[i for i in range(1,4)] for j in range(3)]
print(new_list)
new_list2 = []
for j in range(3):
    new_list.append([1,2,3])



# Lec140-Dictionary Comprehension-CipherSchools.py
# dictionary comprehension
# square ={1:1, 2:4, 3:9}
square = {f"Square of {num} is":num**2 for num in range(1,11)}
for k,v in square.items():
    print(f"{k} : {v}")

string = "Harshit"
# for i in string:
    # print(i)
# {'H' : 2 , 'a' : 1}
word_count = {char:string.count(char) for char in string}
print(word_count)



# Lec141-Dictionary comprehension with if else.py
# dictionary comprehension with if else
# d = {1:'odd' , 2:'even'}
odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)



# Lec142-Sets ComprehensionCipherSchools.py
# sets comprehension -----> only one video
s = {k**2 for k in range(1,11)}
print(s)

names = ['harshit', 'mohit', 'rohit']
first = {name[0] for name in names}
print(first)



# Lec143-Intro to arg-CipherSchools.py
# make flexible functions

# *operator
# *args

def total(a,b):
    return a+b

def all_total(*args):
    # (1,2,3,4,5,65)
    total = 0
    for num in args:
        total += num
    return total

print(all_total(1,2,3,4))



# Lec144-args with normal parameter-CipherSchools.py
# *args with normal parameter

def multiply_nums(num,*args):
    multiply = 1
    # print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2,4,3,4))



# Lec145-args as argument-CipherSchools.py
def multiply_nums(*args):
    multiply = 1
    print(args) # ([2,3,4])
    for i in args:
        multiply *= i
    return multiply

nums = (2,3,4)
print(multiply_nums(*nums)) #unpack
 


# Lec146-147-Ch11Ex1CipherSchools.py
def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass any args"

nums = [1,2,3]
print(to_power(3,*nums))



# Lec148-kwargs-CipherSchools.py
# kwargs (keyword arguments)
# **kwargs (double star operator)

# kwargs as a parameter
def func(**kwargs):
    for k,v in kwargs.items():
        print(f'{k} : {v}')

# dictionary unpacking
d= {'name':'Harshit', 'age':24}
func(**d)



# Lec149-Functions with all type of parameter-CipherSchools.py
# functions with all parameters
def func(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('harshit', 1,2,3, a=1, b=2)



# Lec150-151-Ch11Ex2-CipherSchools.py

def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]


names = ['harshit', 'mohit']
print(func(names, reverse_str = True))



# Lec152-Chapter 11 summary-CipherSchools.py
def add(a,b):
    return a+b

def new_add(*args):
    # 1,2,3,4
    # (1,2,3,4)
    total = 0
    for num in args:
        total+= num
    return total




def func2(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func2('harshit', 1,2,3, a=1, b=2)



# Lec153-Lambda Expression-CipherSchools.py
# lambada expressions (anonymous function)

def add(a,b):
    return a+b

add2 = lambda a,b : a+b
print(add2(2,3))


multiply = lambda a,b : a*b
print(multiply(2,3))

print(add)
print(add2)
print(multiply)




# Lec154-Lambda Expression practice-CipherSchools.py
# lambda expression practice

# lambda with if , else
def func(s):
    return len(s)>5


func = lambda s : len(s) > 5
print(func('abcdefg'))



# Lec155-Eumerate functioncipherSchools.py
# we use enumerate function with for loop to track position of our
# item in iterable


# How we can do this without enumerate function
names = ['abc', 'abcdef', 'harshit']

def find_pos(l, target):
    for pos, name in enumerate(l):
        if name== target:
            return pos
    return -1

print(find_pos(names, 'harshit'))



# Lec156-Map function-CipherSchools.py
# map function

numbers = [1,2,3,4]

def square(a):
    return a**2

squares = list(map(lambda a:a**2, numbers))
print(squares)

# list comp
squares_new = [i**2 for i in numbers]
print(squares_new)

new_list = []
for num in numbers:
    new_list.append(square(num))

print(new_list)

names = ['abc', 'abcd', 'abcde']
length = list(map(len,names))

print(length)



# Lec157-filter function-CipherSchools.py
# filter function

def is_even(a):
    return a%2==0

numbers = [3,4,2,1,5,6,9,8,10]

evens = filter(lambda a:a%2==0, numbers)

new_even = [i for i in numbers if i%2==0]

print(list(evens))
print(new_even)



# Lec158-Iterator vs iterable-CipherSchools.py
# iterator vs iterables

numbers = [1,2,3,4] #, tuples, strings --- iterables
squares = map(lambda a:a**2, numbers) # iterator

print(next(numbers))



# Lec159-zip function-CipherSchools.py
# zip function
user_id = ['user1', 'user2', 'user3']
names = ['harshit', 'mohit', 'rohit']
last_names = ['vashistha', 'vashishtha','sharma']

# ('user1','harshit'),('user2','mohit')
print(list(zip(user_id, names, last_names)))

# example =[('a',1), ('b', 2)]
# print(dict(example))
  


# Lec160-Zip function part2-Cipherschools.py
l1 =[1,3,5,7]
l2 =[2,4,6,8]
new_list = []

for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)



# Lec161-Advance function Practice 1-CipherSchools.py
# THIS IS CHALLENGE

average_finder = lambda *args: [(sum(pair)/len(pair)) for pair in zip(*args)]

print(average_finder([1,2,3] , [4,5,6], [7,8,9]))



# Lec162-any and all function-CipherSchools.py
# any , all function

numbers1 = [13,1,9,7,10]
numbers2 = [1,2,3,4,5,6]

print(any([num%2==0 for num in numbers1]))
print(all([num%2==0 for num in numbers1]))

  
# Lec163-any and all practice-CipherSchools.py
# any all function

def my_sum(*args):
    # args =()
    if all([(type(arg)==int or type(arg)== float) for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "Wrong input"

print(my_sum(1,2,3,4,8.9))



# Lec164-advance min() and max()-CipherSchools.py
# advabnce min() and max()

names = ['Harshit Vashisth', 'Moihit', 'ab', 'z']
print(max(names,key = lambda item : len(item)))

students = {
    'harshit' : {'score':50, 'age': 24},
    'mohit' : {'score':75, 'age': 19},
    'rohit' : {'score':76, 'age': 23}
}

print(max(students, key = lambda item : students[item]['age']))



# Lec165-Advance sorted function-CipherSchools.py
fruits = ['grapes', 'mango', 'apple']

fruits2 = ('grapes', 'mango', 'apple')
# print(sorted(fruits))


fruits3 = {'grapes', 'mango', 'apple'}
print(sorted(fruits))

guitars = [
    {'model': 'yamaha f310','price':8400},
    {'model': 'faith naptune','price':50000},
    {'model': 'faith apollo venus','price':35000},
    {'model': 'taylor 814ce','price':450000}
]

sorted_guitars = sorted(guitars, key = lambda d:d['price'], reverse = True)
print(sorted_guitars)



# Lec166-More about functions-CipherSchools.py

def add(a,b):
    ''' this function takes 2 numbers and return their sum'''
    return a+b


print(help(sum))



# Lec167-Chapter14 intro-CipherSchools.py

def square(a):
    return a**2

s = square
# print(s(7))
print(s.__name__)
print(square.__name__)
print(s)
print(square)



# Lec168-Pass function as argument-CipherSchools.py
# map
def square(a):
    return a**2

l = [1,2,3,4]
# print(list(map(lambda a: a**2,l)))

def my_map(func, l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list  

def my_map2(func, l):
    return [func(item) for item in l] 

print(my_map2(lambda a : a**3,l))



# Lec169-Function returning function-CipherSchools.py
# functions returning function

def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func

def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2

var = outer_func2("hello there ! ")
var()



# Lec170-Closures Practice-CipherSchools.py
# function returning function (closure) practice

def to_power(x): # x = 3
    def calc_power(n): # n =2
        return n**x
    return calc_power

cube = to_power(3)
print(cube(2))

square = to_power(2)
print(square(4))



# Lec171-Decorators intro-CipherSchools.py
# Decorators - enhance the functionality of other functions
def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function

# this is awesome function

@decorator_function #shortcut
def func1():
    print('this is function 1')

func1()

@decorator_function
def func2():
    print('this is function 2')

func2()



# Lec172-Decorators part2-CipherSchools.py
def decorator_function(any_function):
    def wrapper_function(*args, **kwargs):
        print('this is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def func(a):
    print(f'this is function with argument {a}')

func(5)

@decorator_function
def add(a,b):
    return a+b

print(add(2,3))



# Lec173-Decorators part3-CipherSchools.py
from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        """ this is wrapper function """
        print('this is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def add(a,b):
    ''' this is add function'''
    return a+b

print(add.__doc__)
print(add.__name__)



# Lec174-Decorators practice-CipherSchools.py
from functools import wraps

def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args, **kwargs)
    return wrapper


@print_function_data
def addition(a,b):
    '''This function takes two numbers as arguments and return their sum'''
    return a+b

print(addition(4,5))



# Lec175-Ch14Ex1-CipherSchools.py
# exercisse decorator
import time

t1=time.time()
print("this is line one")
x=5
if x==5:
    print('x is equal to 5')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
print('this is line two')
t2=time.time()
print(t2-t1)



# Lec176-Exercise 1 solution-cipherSchools.py
from functools import wraps
import time
def calculate_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'Executing .... {function.__name__}')
        t1=time.time()
        returned_value = function(*args, **kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(f'This function took {total_time} seconds')
        return returned_value
    return wrapper

@calculate_time
def square_finder(n):
    return [i**2 for i in range(1,n+1)]

square_finder(1000)



# Lec177-Decorators Practice 2-CipherSchools.py
from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([type(arg) == int for arg in args]):
            return function(*args, **kwargs)
        
        else:
            print("Invalid argument")
    return wrapper



@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1,2,3,4,5))



# Lec178-Decorators with arguments-CipherSchools.py
from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs)
            print("Invalid argument")
        return wrapper
    return decorator

@only_data_type_allow(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string

print(string_join('harshit', 'Vashisth', 'a'))



# Lec180-Generator example-CipherSchools.py
# Create your first generator with generator function
def nums(n):
    for i in range(1,n+1):
        yield(i)

numbers = nums(10)

for num in numbers:
    print(num)

for num in numbers:
    print(num)



  
# Lec181-182-Ch15Ex1-CipherSchools.py
def even_generator(n):
    for num in range(2,n+1,2):
        yield(num)

even_nums = even_generator(20)
for num in even_nums:
    print(num)



# Lec183-Generator comprehension-Cipherschools.py
square = (i**2 for i in range(1,11))

print(next(square))
print(next(square))
print(next(square))


for num in square:
    print(num)

for num in square:
    print(num)



# Lec184-List vs Generators-CipherSchools.py

import time
# list vs generator
# memory usage , time
# when to use list , when to use generator

# t1 = time.time()
# l = [i**2 for i in range(10000000)] #10million
# print(time.time() - t1)

t1 = time.time()
g = (i**2 for i in range(10000000)) #10million
print(time.time() - t1)



# Lec186-OOPs-CipherSchools.py

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        print('init method called')
        self.person_first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Harshit','Vashistha',24)
p2 = Person('Mohit', 'Vashistha', 19)

print(p1.person_first_name)
print(p2.person_first_name)



# Lec187-188-OPP Ex1-CipherSchools.py
class Laptop:
    def __init__(self, brand, model_name, price):
        #instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name


laptop1 = Laptop('hp', 'au114tx', 63000)
print(laptop1.laptop_name)



# Lec189-OOP instance methods-CipherSchools.py
# instance methods
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.full_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person('Harshit','Vashistha',24)
p2 = Person('Mohit', 'Vashistha', 19)
print(p1.is_above_18())



# Lec190-191-OOP Ex2-CipherSchools.py
class Laptop:
    def __init__(self, brand, model_name, price):
        #instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name

    def apply_discount(self,num):
        # self.price
        off_price = (num/100)*self.price
        return self.price - off_price



laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('apple', 'mackbook pro', 230000)
print(laptop2.apply_discount(5))



# Lec192-Class Variable-CipherSchools.py
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def calc_circumference(self):
        return 2*Circle.pi*self.radius


c = Circle(4)
c1 = Circle(5)
print(c1.calc_circumference())

class Laptop:
    discount_percent = 10
    def __init__(self, brand, model_name, price):
        #instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name

    def apply_discount(self):
        # self.price
        off_price = (Laptop.discount_percent/100)*self.price
        return self.price - off_price



laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('apple', 'mackbook pro', 230000)
print(laptop2.apply_discount())



# Lec193-Class Variable part2-CipherSchools.py

class Laptop:
    discount_percent = 10
    def __init__(self, brand, model_name, price):
        #instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name

    def apply_discount(self):
        # self.price
        off_price = (self.discount_percent/100)*self.price
        return self.price - off_price



laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('apple', 'mackbook pro', 230000)
laptop2.discount_percent = 50
print(laptop2.__dict__)
print(laptop2.apply_discount())



# Lec194-195-OOP Ex3-CipherSchools.py

class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.person_first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Harshit','Vashistha',24)
p2 = Person('Harshit','Vashistha',24)
p2 = Person('Harshit','Vashistha',24)
print(Person.count_instance)



# Lec196-OOP class methods-CipherSchools.py
# class methods
# difference between claass methods and instance methods

class Person:
    count_instance = 0 # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    def full_name(self):
        return f"{self.full_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person('Harshit','Vashistha',10)
p2 = Person('Harsh', 'Vashistha', 24)
print(Person.count_instances())



# Lec197-Class method as constructor-CipherSchools.py
# class method as a constructor
class Person:
    count_instance = 0 # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    def full_name(self):
        return f"{self.full_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18



p1 = Person('Harshit','Vashistha',10)
p2 = Person('Harsh', 'Vashistha', 24)

p3 = Person.from_string('Harshit,vashisth,24')
print(p3.full_name())



# Lec198-OOP Static method-CipherSchools.py
# class method as a constructor
class Person:
    count_instance = 0 # class variable / class attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    @staticmethod
    def hello():
        print('hello, static method is called')

    def full_name(self):
        return f"{self.full_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18



p1 = Person('Harshit','Vashistha',10)
p2 = Person('Harsh', 'Vashistha', 24)

p3 = Person.from_string('Harshit,vashisth,24')



# Lec199-Encapsulation, Abstraction, Naming Convention, Name Mangling -CipherSchools.py

class Phone:
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price

    def make_a_call(self, phone_number):
        print(f"callinfg {phone_number} .....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass # twilio

phone1 = Phone('nokia','1100',1000)
# print(phone1.__price)
print(phone1._Phone__price)
print(phone1.__dict__)



# Lec200-OOP property and setter decorator-CipherSchools.py
# will discuss three problems in existing
# the we will solve them using getter , setter decorator 


class Phone:
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name

    @property 
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)

    def make_a_call(self, phone_number):
        print(f"callinfg {phone_number} .....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone1 = Phone('Nokia','1100',1000)

phone1._price = -500
print(phone1.brand)
print(phone1.model_name)
print(phone1.price)
print(phone1.complete_specification)



# Lec201-Inheritance intro-CipherSchools.py
class Phone: # base class / parent class
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self, number):
        print(f"calling {number} .....")


class Smartphone(Phone): # derived / child class
    def __init__(self, brand,model_name, price,ram,internal_memory,rear_camera):
        # two ways
        # Phone.__init__(self,brand,model_name,price) uncommon way
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

phone = Phone('nokia', '1100', 1000)
smartphone = Smartphone('onePlus','5',30000,'6 GB','64GB','20MP')
print(phone.full_name())
print(smartphone.full_name() + f"and price is {smartphone._price}")



# Lec202-Multilevel inheritance , MRO, method overriding-CipherSchools.py
# can we derive more than one class from base class ?


class Phone: # base class / parent class
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self, number):
        print(f"calling {number} .....")


class Smartphone(Phone): # derived / child class
    def __init__(self, brand,model_name, price,ram,internal_memory,rear_camera):
        # two ways
        # Phone.__init__(self,brand,model_name,price) uncommon way
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

class FlagshipPhone(Smartphone):
    def __init__(self, brand,model_name, price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name, price,ram,internal_memory,rear_camera)
        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} and front_camera = {self.rear_camera}"





# phone = Phone('nokia', '1100', 1000)
# smartphone = Smartphone('onePlus','5',30000,'6 GB','64GB','20MP')
oneplus5 = Smartphone('onePlus','5',30000,'6 GB','64GB','20MP')
oneplus5t = FlagshipPhone('onePlus','5',30000,'6 GB','64GB','20MP','16MP')

print(issubclass(FlagshipPhone,Smartphone))



# Lec203-Multiple inheritance-CipherSchools.py
# Multiple Inheritance

class A:

    def class_a_methods(self):
        return 'I\'m just a class A method'

    def hello(self):
        return 'hello from class A'

class B:

    def class_a_methods(self):
        return 'I\'m just a class B method'

    def hello(self):
        return 'hello from class B'

class C(A,B):
    pass

instance_c = C()

print(C.__mro__)