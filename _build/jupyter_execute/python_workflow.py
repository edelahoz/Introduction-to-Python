#!/usr/bin/env python
# coding: utf-8

# # Control flow
# 
# In this notebook we will study several statements to control the order in which the code is executed.

# ##  Conditionals
# 
# Conditionals are control structures which enable the user to run certain pieces of code if a condition is met. For example:

# In[1]:


number = 8
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# Notice that if/else blocks are delimited by indentation. To avoid problems with indentation one can use the **pass** statement: 

# In[2]:


condition = True
if condition:
    print("Condition is satisfied")
else:
    pass

print("Keeping with the code flow")


# More than one condition can be evaluated with elif clauses:

# In[3]:


grade = 8.5
if (grade >= 9) and (grade <= 10):
    print("You got an A")
elif (grade >= 7) and (grade < 9):
    print("You got a B")
elif (grade >= 6) and (grade < 7):
    print("You got a C")
elif (grade >= 5) and (grade < 6): 
    print("You got a D")
elif (grade >= 0) and (grade < 5):
    print("You failed")
else:
    print(f"{grade} is not a valid grade.")


# In python there is also a conditional operator or ternary operator:

# In[4]:


raining = False
print("Let's go to the", 'beach' if not raining else 'library')


# In[5]:


m = a if a > b else b
print(f"{m = }")


# In[ ]:


def get_maximum(a, b):
    return a if a > b else b

get_maximum(a, b)


# ####  Structural Pattern Matching
# 
# In other programming languages such as C, matlab, there is another structure to execute different chunks of code given the possible values that a variable can have, the switch-case statement. For example:
# ```C
# switch (grade){
#     case 'A':
#         printf("You got an excellent grade");
#         break;
#     case 'B':
#         printf("You got a good grade");
#         break;
#     case 'C':
#         printf("You got an average grade");
#         break;
#     default:
#         printf("You didn't meet the course minimum grade");
#         break;
# }
# ```
# 
# Python did not have an equivalent structures in versions previous to **python 3.10** (realeased in October 2021). A workaround could be to use multiple elif statements:
# ```python
# if grade == 'A':
#     print("You got an excellent grade")
# elif grade == 'B':
#     print("You got a good grade")
# elif grade == 'C':
#     print("You got an average grade")
# else:
#     print("You didn't meet the course minimum grade")
# ```
# or dictionaries:
# ```python
# d_grades = {'A': "You got an excellent grade", 
#             'B': "You got a good grade",
#             'C': "You got an average grade",}
# 
# print(d.get(grade, "You didn't meet the course minimum grade"))
# ```
# 
# 
# The new match-case statement has the functionalities of the switch-case statement:
# ```python
# match grade:
#     case 'A':
#         print("You got an excellent grade")
#     case 'B':
#         print("You got a good grade")
#     case 'C':
#         print("You got an average grade")
#     case _:
#         print("You didn't meet the course minimum grade")
# ```
# And more:
# ```python
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         
#     def __repr__(self):
#         return f"Person({self.name}, {self.age})"
#  
# def has_discount(person):
#     match person:
#         case Person(age=age) if (age <= 25) or (age >= 65):
#             return True
#         case Person():
#             return False
#         case _:
#             return ValueError(f"{person} is not an instance of class Person")
# ```
# 
# I wouldn't recommend downloading now python 3.10 if you use third party python libraries as they probably won't be compatible with this version yet.

# ##  Iterations 
# 
# Iteration means executing the same block of code over and over, potentially many times. A programming structure that implements iteration is called a loop. There are two types of iteration:
# 
# * Definite iteration, in which the number of repetitions is specified explicitly in advance (**for loops**).
# * Indefinite iteration, in which the code block executes until some condition is met (**while loops**).
# 
# Moreover, python can iterate over native structures such as lists or dicitionaries. These type of iterations are called **comprehensions**.
# 
# * ### while loops
# 
# The python while loop has the following structure:
# ```python
# while <expression>:
#     <statements>
# ```
# If  \<expression\> is **True**, the loop body (\<statements\>) is executed. Then \<expression\> is checked again, and if still true, the body is executed again. This continues until \<expression\> becomes false, at which point program execution proceeds to the first statement beyond the loop body. Example:

# In[7]:


total = 0
i = 1
while total < 100:
    total += i
    i += 1
print(f"{total = }, {i = }")


# While loops can include more advance features like the **break** and **continue** statements. **break** terminates the loop completely and proceeds to the first statement following the loop and **continue** terminates the current iteration and proceeds to the next iteration.

# In[10]:


total = 0
i = 1
while total < 100:
    if i > 10:
        break
    total += i
    i += 1
print(f"{total = }, {i = }")


# In[1]:


total = 0
i = 1
while total < 100:
    if i == 10:
        i += 1 # comment this line to enter an infinite loop
        continue
    total += i
    i += 1
print(f"{total = }, {i = }")


# The **break** and **continue** statements work the same way with for loops as with while loops.
# 
# A while loop can include an else clause:

# In[11]:


names = ["Fulanito", "Menganito", "Zutanito"]
target = "Perenganito"
while i < len(names):
    if names[i] == target:
        # Processing for item found
        break
    i += 1
else:
    # Processing for item not found
    print(target, 'not found in list.')


# While loops can also be written in one line of code:

# In[10]:


n = 5
while n > 0: n -= 1; print(n, end=' ')


# * ### for loops
# 
# Python implements collection-based or iterator-based for loops, i.e., the loop iterates over a collection of objects. For example:

# In[ ]:


students = ["Diego Álvarez", "Samir Belaoui", "Dario González", "Pablo Herreros", "Rubén López", 
            "Luis Fernando Mejía", "Conrado Muñoz", "Abram Pérez", "Miguel Ruiz"]

for student in students:
    print(f"Welcome to programming with python {student.title()}")


# The for loops over an iterable, in this case a list. Each time through the loop, student takes on a successive item in students. 
# 
# In python, iterable means an object can be used in iteration. If an object is iterable, it can be passed to the built-in Python function iter(), which returns something called an iterator. Examples:

# In[ ]:


iter_string = iter('foobar')
print(next(iter_string), end=''); print(next(iter_string), end=''); print(next(iter_string), end='');
#print(next(iter_string), end=''); print(next(iter_string), end=''); print(next(iter_string), end='')


# In[ ]:


iter_set = iter({'foo', 'bar', 'baz'}) 
print(next(iter_set))


# In[ ]:


iter_dict = iter({'foo': 1, 'bar': 2, 'baz': 3})
print(next(iter_dict))


# When there are no more elements left in the iterator a **StopIteration** exception is raised. You can only obtain values from an iterator in one direction. You can’t go backward. There is no prev() function.
# 
# All the data types you have encountered so far that are collection or container types are iterable. These include the string, list, tuple, dict, set. But these are by no means the only types that you can iterate over. Many objects that are built into Python or defined in modules are designed to be iterable. Even user-defined objects can be designed in such a way that they can be iterated over. 
# 
# To carry out the iteration in the **for loop** example above, python does the following:
# 
# 1. Calls iter() to obtain an iterator for students
# 2. Calls next() repeatedly to obtain each item from the iterator 
# 3. Terminates the loop when next() raises the StopIteration exception
# 
# The loop body is executed once for each item next() returns, with loop variable student set to the given item for each iteration.
# 
# Numeric range loops can be easily implemented using the range() function which returns an iterable that yields a sequence of integers.

# In[ ]:


for i in range(5):
    print(i, end=' ')


# In[ ]:


for i in range(3,24,7):
    print(i, end=' ')


# A for loop can have an else clause as well. The interpretation is analogous to that of a while loop. The else clause will be executed if the loop terminates through exhaustion of the iterable:

# In[2]:


for value in ['foo', 'bar', 'baz', 'qux']:
    print(value, end='. ')
else:
    print('\nLoop is finished.')  # Will execute


# In[3]:


for value in ['foo', 'bar', 'baz', 'qux']:
    if 'z' in value:
        break
    print(value, end='. ')
else:
    print('\nLoop is finished.')  # Won't execute


# Several values can be iterated at the same time:

# In[12]:


names = ["Fulanito", "Menganito", "Zutanito", "Perenganito"]
ages = [26, 22, 31, 38]
for name, age in zip(names, ages):
    print(f"{name.capitalize()} is {age} years old.")


# One can also keep the number of the iteration:

# In[7]:


for i, (name, age) in enumerate(zip(names, ages)):
    print(f"{i+1}. {name.capitalize()} is {age} years old.")


# * ### comprehensions
# 
# Instead of creating a list by means of a loop, one can make use of a list comprehension with a rather self-explaining syntax.

# In[13]:


list1 = [i**2 for i in range(5)]
print(list1)


# One can add if/else clause to the comprehensions

# In[15]:


list2 = [i**2 for i in range(5) if i % 2 == 0]
print(list2)


# In[16]:


list3 =  [i**2 if i % 2 == 0 else i**3 for i in range(5) ]
print(list3)


# Comprehensions can be used with all types of containers:

# In[18]:


names = ["Fulanito", "Menganito", "Zutanito", "Perenganito"]
d_names = {name:i for i,name in enumerate(names)}

for key in d_names:
    print(f"d_names[{key}] = {d_names[key]}")


# In[21]:


s = {i % 3 for i in range(6)}
print(s)

