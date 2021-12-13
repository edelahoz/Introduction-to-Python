#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# Function blocks must be indented as other control-flow blocks.

# In[1]:


def hello():
     print("Hello world!")
        
hello()


# Functions can return objects. By default, functions return **None**.

# In[2]:


def add(x, y):
    """
    A triple quoted string is usually written at the begging of the fuction as documentation 
    regarding what the function does and its parameters. 
    """
    return x + y

add(2,3)


# Functions are first-class objects, which means they can be:
# 
#  * assigned to a variable
#  * an item in a list (or any collection)
#  * passed as an argument to another function. (check last section about decorators)
#         
# To call them append () after the variable that stores the function.

# In[3]:


list_of_functions = [hello, add]


# In[4]:


a = list_of_functions[0]()


# In[5]:


a is None


# In[6]:


list_of_functions[1](2,3)


# ### Input parameters
# 
# There are two types of input parameters: positional and keyword parameters. 
# 
# * **Positional parameters** are mandatory and are specified by their position when the function is called.
# * **Keyword parameters** are optional parameters called by name. The order of the keyword arguments does not matter. Moreover, they allow you to specify default values.
# 
# 

# <div class="alert alert-block alert-danger"> <strong>&#9888; WARNING &#9888; </strong>
#     
# Default values are evaluated when the function is defined, not when it is called. This can be problematic when using mutable types (e.g. dictionary or list) and modifying them in the function body, since the modifications will be persistent across invocations of the function.
# </div>

# In[7]:


def add_to_list(x, l=[]):
    l.append(x)
    return l
    
x, y = 1, 2

out = add_to_list(x)
print(f"{out = }")


# In[8]:


out = add_to_list(y)
print(f"{out = }")


# ### Anonymos functions *lambda*

#  a lambda function has the following characteristics:
# 
# * It can only contain expressions and can’t include statements (return, pass, assert, raise, etc.) in its body.
# * It is written as a single line of execution.
# * It does not support type annotations.
# * It can be immediately invoked (IIFE).
# 

# In[9]:


add_one = lambda x: x + 1

add_one(3)


# In[10]:


full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'

full_name('ramón','garcía')


# **Immediately Invoked Function Expression**
# ```python
# (lambda x, y: x + y)(2,3)
# ```
# Python does not encourage using immediately invoked lambda expressions. It simply results from a lambda expression being callable, unlike the body of a normal function.
# 
# Lambda functions are frequently used with higher-order functions, which take one or more functions as arguments or return one or more functions. E.g.,
# ```python
# def hof(x, f):
#     return x + f(x)
# 
# hof(x, lambda x: x**2)
# ```
# Python exposes higher-order functions as built-in functions or in the standard library. Examples include map(), filter(), functools.reduce(), as well as key functions like sort(), sorted(), min(), and max(). You’ll use lambda functions together with Python higher-order functions in Appropriate Uses of Lambda Expressions.

# In[11]:


out = list(map(lambda x: x*2, range(3)))
print(f"{out =}")


# **Key Functions**
# 
# 
#     sort(): list method
#     sorted(), min(), max(): built-in functions
#     nlargest() and nsmallest(): in the Heap queue algorithm module heapq
# 

# In[12]:


ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids)) # Lexicographic sort

sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # Integer sort
print(sorted_ids)


# **Arguments**

# In[13]:


(lambda x, y, z=3: x + y + z)(1, y=2)


# In[14]:


(lambda *args: sum(args))(1,2,3)


# In[15]:


(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)


# ### Modifying variables in functions
# 
# Can you modify the value of a variable inside a function? Most languages (C, Java, …) distinguish “passing by value” and “passing by reference”. In Python, such a distinction is somewhat artificial, and it is a bit subtle whether your variables are going to be modified or not. Fortunately, there exist clear rules.
# 
# In Python the parameters given to functions are references to objects, which are passed by value. When you pass a variable to a function, python passes the reference to the object to which the variable refers (the value). Not the variable itself.
# 
# If the value passed in a function is immutable, the function does not modify the caller’s variable. If the value is mutable, the function may modify the caller’s variable in-place

# In[16]:


def try_to_modify(x, y, z):
    x = 23
    y.append(42)
    z = [99] # new reference


a = 77    # immutable variable
b = [99]  # mutable variable
c = [28]


# In[17]:


print(f"{a =}"); print(f"{b =}"); print(f"{c =}")


# In[18]:


try_to_modify(a, b, c)
print(f"{a =}"); print(f"{b =}"); print(f"{c =}")


# ### Scope of variables
# 
# Variables declared outside the function can be referenced within the function.
# But these “global” variables cannot be modified within the function, unless declared global in the function.

# In[19]:


x = 5
def addx(y):
     return x + y
    
print(f"{addx(10) = }")


# In[20]:


x = 5
y = "hello"

def modify_x(y):
    x = y

modify_x(y)

print(f"{x = }")


# In[21]:


x = 5
y = "hello"

def modify_x(y):
    global x
    x = y

modify_x(y)

print(f"{x = }")


# ### \*args and \*\*kwargs arguments
# 
# There are special forms of parameters:
# 
#   - **\*args**: any number of positional arguments packed into a tuple
#   - \****kwargs**: any number of keyword arguments packed into a dictionary
# 

# In[22]:


def print_args(*args, **kwargs):
    print('args is', args)
    print('kwargs is', kwargs)

print_args('one', 'two', x=1, y=2, z=3)


# ###  Special type of functions: Decorators
# 
# Decorators are functions that take a function as an argument and change its behaviour without modifying the  function it self. An example of decorator is the following:
# ```python
# import time
# 
# def time_function(f):
#     def wrapper(*args, **kwargs):
#         t0 = time.perf_counter()
#         res = f(*args, **kwargs)
#         t1 = time.perf_counter()
#         print(f"Time spent executing {f.__name__} was {t1-t0:.3f} seconds.")
#         return res
#     return wrapper     
# ```
# 
# This function receives an f function as an input, and returns the wrapper function. The wrapper function executes  
# ```python 
# f(*args,**kwargs)
# ``` 
# and times the time that executing it takes. The use of this decorator is very simple as shown below:

# In[23]:


import time

def time_function(f):
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        res = f(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"Time spent executing {f.__name__} was {t1-t0:.3f} seconds.")
        return res
    return wrapper  


def go_to_sleep_1(t, name=""):
    print(f"{name} goes to sleep")
    time.sleep(t)
    print(f"{name} has slept for {t} hours.")

@time_function
def go_to_sleep_2(t, name=""):
    print(f"{name} goes to sleep")
    time.sleep(t)
    print(f"{name} has slept for {t} hours.")


# In[24]:


t = 2
name = "Jane"


# In[25]:


go_to_sleep_1(t,name=name)


# In[26]:


go_to_sleep_2(t,name=name)


# In[ ]:




