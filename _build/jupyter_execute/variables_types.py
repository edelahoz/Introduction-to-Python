#!/usr/bin/env python
# coding: utf-8

# # Basic Data Types
# 
# 
# ## Numerical data types
# 
# Python support the following scalar numerical types:
# - **Integers:**
#     - Python interprets a sequence of decimal digits without any prefix to be a decimal number.
#     - To define an integer value in binary add 0b or 0B before

# In[1]:


# This is a comment in python
type(1)


# In[2]:


print(0b01010111)


# - **Floats:**
# 
#     - float values are specified with a decimal point. 
#     - To write a number in scientific notation append the character e or E followed by a positive or negative integer.
#     - Python float values are represented as 64-bit “double-precision". The maximum value a floating-point number can have is approximately $1.8 \times 10^{308}$.
#     - The closest a nonzero number can be to zero is approximately $5.0 \times 10^{-324}$.

# In[3]:


print(type(12.0))
print(type(3e-5))


# In[4]:


2e308


# In[5]:


print(3e-324)
print(1e-324)


# <div class="alert alert-block alert-success">
# Floating point numbers are represented internally as binary (base-2) fractions. Most decimal fractions cannot be represented exactly as binary fractions, so in most cases the internal representation of a floating-point number is an approximation of the actual value. In practice, the difference between the actual value and the represented value is very small and should not usually cause significant problems.
#     
#     
# Try running the following snippet:
#     
#     a = 1.0
#     b = 1.0 + 1e-16
#     b - a 
#     
# Do you get what you expected?
# </div>

# - **Complex:**
#     - Complex numbers are specified as <real part>+<imaginary part>j

# In[6]:


a = 1.5 + 0.5j
print(type(a))


# In[7]:


a.real


# In[8]:


a.imag


# **Type conversion (casting)**

# In[9]:


print(int(1.6))
print(complex(1))
print(float(2))


# <div class="alert alert-block alert-danger"> <strong>&#9888; WARNING &#9888; </strong>
#     
# In python 2, the divison between two integers returns an integer -> $3/2 = 1$
#     
# In python 3, the type of the result of an integer division is float -> $3/2 = 1.5$
# </div>
# 

# ## Variables
#  
#  * Variables consist of two parts: the name and the value. 
#  * To assign a variable to a name, use a single equals sign (=). E.g.,:
#  ```python
# c = 3e8 # speed of light [m/s]
# ```
#  * Variable names may be made up of upper- and lowercase letters, digits (0–9), and underscores (_).
#  
#  * Python is dynamically typed. This means that:
#     1. Types are set on the variable values and not on the variable names.
#     2. Variable types do not need to be known before the variables are used.
#     3. Variable names can change types when their values are changed.
# ```python
# x = 1 # integer
# x = "hello" # string
# ```
#  * In other language programs such as C, C++, Fortran, etc. is the other way round:
#     1. Types are set on the variable names and not on the variable values.
#     2. Variable types must be specified (declared or inferred) before they are used.
#     3. Variable types can never change, even if the value changes.
# ```c
# int main{
#           int x=1;
#           return x;
# }
# ```
#  * Note that variables do not store a value in python, they store a pointer to the memory location where the actual value is stored.

# In[10]:


a = [2, 3]
b = a
print('a:', a, '\tb:', b)


# In[11]:


b[0] = 3
print('a:', a, '\tb:', b)


# To modify list b without modyfing a one should create a copy of the list:

# In[12]:


a = [2, 3]
b = a[:]
print('a:', a, '\tb:', b)


# In[13]:


b[0] = 3
print('a:', a, '\tb:', b)


# ## Special variables in python
# 
# Python has a few special variables that are so important that their values are built into
# the language: 
# ```python
# True, False, None, NotImplemented
# ```
# Each of these variables exists only once whenever you start up a Python interpreter. For this reason, they are
# known as **singletons**. 
# 
#  * **Booleans**
#  
# Other values can be converted to Booleans:
# ```python
# bool(0) == False
# bool([]) == False
# bool("hello world") == True
# ```
#  * **None**
#  
# None is a special variable in Python that is used to denote that no value was given or
# that no behavior was defined. This is different than just using zero, an empty string,
# or some other nil value. Zero is a valid number, while None is not. If None happens to
# make it to a point in a program that expects an integer or float, then the program
# with rightfully break. With a zero, the program would have continued on. This fills
# the same role as NULL in C/C++ and null in JavaScript. 
# 
#  * **NotImplemented**
#  
# Unlike None, the variable NotImplemented is used to signal not only that behavior is
# not defined but also that the action is impossible, nonsensical, or nonexistent. For
# example, NotImplemented is used under the covers when you are trying to divide a
# string by a float.

# ## Strings
# 
# - String can be specified with different syntaxes: simple, double or triple quotes. With the latter one can create strings that can span several lines.
# - Strings are one of the data types Python considers immutable, meaning not able to be changed. In fact, all the data types you have seen so far are immutable.
# - Strings can be sliced.
# 
# <div class="alert alert-block alert-info"><b>Note: </b>Slicing in Python is a feature that enables accessing parts of sequences like strings, tuples, and lists. You can also use them to modify or delete the items of mutable sequences such as lists. Slices can also be applied on other objects like NumPy arrays, or Pandas data frames as we will see.
#     
# <strong>Slicing syntax:</strong> variable[start:stop:stride]
# </div>
# 
# - Python provides a lot of built-in methods to work with strings. We show here some examples but check the documentaion for more information.

# In[14]:


s1 = "This is a string"
s2 = 'This is also string'
s3 = """ This 
string
spans 
multiple 
lines"""


# Strings can be sliced. Below there are several examples of string slices

# In[15]:


s1[:4]


# In[16]:


s1[::2]


# In[17]:


s1[5:7]


# In[18]:


s1[-6:]


# In[19]:


s1[::-1]


# Strings are immutable. They cannot be modified in place. But one can make a copy of it.

# In[20]:


s1[:4] = 'That'


# In[143]:


s1 = s1.replace("This","That")
s1


# In[144]:


# Unlike list s1[:] does not return a copy of s1, it returns a pointer
new_s1 = s1[:]
new_s1  is s1


# #### Examples of built-in functions

# In[146]:


s = "hello!"
s.capitalize()


# In[147]:


s = "fulano garcia"
s.title()


# In[148]:


s = "hello!"
s.upper()


# In[149]:


s = "Hello world! blablabla"
s.find('bla')


# In[150]:


s = "Hello world! blablabla"
s.count('bla')


# In[151]:


s = "124.4"
s.isdigit()


# In[153]:


s = "1244"
s.isdigit()


# In[154]:


s = "hello"
s.center(10)


# ### Interpolating variables into a string (f-strings)
# 
# f-strings are a type of strings introduced in Python version 3.6, that enables you to write code withing a string statement. f-strings have many applications here we will cover some simple but handy examples of its use.

# In[119]:


a = 5
b = 34

print(f"The result of the product is {b*a}")


# One can also cutomize the format of the variables.

# In[122]:


from math import pi

print(f"pi value: {pi:.4f}")


# ## Containers
# 
# Python provide several efficient types of containers where python objects can be stored.
# 
# - **Lists:**
# 
#     - A list is an **ordered** collection of objects, that can contain different types. 
#     - Lists are defined in Python by enclosing a comma-separated sequence of objects in square brackets.
#     - List are **mutable** objects, i.e., can be changed in place. 
#     - A list can contain any number of objects, (the only limit is the computer’s memory).
#     - Python provide several built-in handy methods such as **append, pop, insert, extend, reverse**, etc. to modify list.
#     - **Slicing** also works in lists.

# In[35]:


# A list can contain objects of different types
mylist = [1, '4', len, "python", 3., 5, 8]


# In[36]:


# List are mutable objects
mylist[2] = 3
print(mylist)


# In[37]:


# Lists can be nested to arbitrary depth.
l1 = [1, [3, 4, [3, 3]], 4]


# In[38]:


# The order in list is important
[1, 2, 3, 4] == [4, 1, 3, 2]


# In[39]:


# List are dynamic
mylist.append(1 + 3j)
print(mylist)


# In[50]:


# Individual elements in a list can be accessed using an index in square brackets.
# Note that Python starts indexing in 0
l1[1][-1]


# In[47]:


# Examples of slicing
print("1.", mylist[2:])
print("2.", mylist[1:5:2])
print("3.", mylist[-1::-2])
print("4.", mylist[::-1])
print("5.", mylist[:5])


# In[51]:


# mylist[:] returns a copy of the mylist
print(mylist[:] == mylist)
print(mylist[:] is mylist)


# In[52]:


# The concatenation (+) operator is override in list
new_list = [1,2] + [3, 4, 5]
print(new_list)


# In[59]:


# The replication (*) operator as well
new_list = 4 * [1, 2] 
print(new_list)


# **Examples of built-in methods**

# In[65]:


new_list = 3 * [1, 2, 3] 
print(f"{new_list = }")

# remove last element of the list
new_list.pop() 
print(f"{new_list = }")

# remove element at input index
a = new_list.pop(2) 
print(f"{new_list = }")
print(f"{a = }")


# In[69]:


# Append object at the end of the list
a = [1, 3, 5]
a.append(7)
print(f"{a = }")
# Extend the list with an iterable (containers are iterables)
a.extend([9])
print(f"{a = }")


# In[70]:


# Inserts object into list
a.insert(1, 2)
print(f"{a = }")


# In[71]:


# Reverse the list
a.reverse()
print(f"{a = }")


# In[73]:


# Order the list in increasing order
a.sort()
print(f"{a = }")


# - **Tuples:** Tuples are identical to lists in all respects, except for the following properties:
#     - Tuples are defined in Python by enclosing a comma-separated sequence of objects in parenthesis.
#     - Tuples are an example of immutable objects, i.e., cannot be modified once created as we will see in the next subsection.
# 

# In[75]:


# Definition of several tuples
tup1 = (3, 5, 6)
tup2 = ("python",)
tup3 = (3, (3, 5,), 5) 
print(f"{tup1 = }")
print(f"{tup2 = }")
print(f"{tup3 = }")


# In[76]:


# Tuples are immutable
tup1[2] = 3


# When to use a tuple instead of a list?
# 
#    - Program execution is faster when manipulating a tuple than it is for the equivalent list. (Not noticeable when the list or tuple is small)
# 
#    - When you don’t want data to be modified. 
# 
#    - Dictionaries (see below) require one of its components (the key) to be a value of an immutable type. A tuple can be used as a dictionary key, unlike lists.
# 

# - **Dictionaries:**
#     - Dictionaries are data structures that map a colletion of specific objects (keys) to other objects (values). One value per key, i.e., dictionaries are maps in the mathematical sense.
#     - Dictionaries are defined in python with comma-separated in curly-braces {}. The elements are given as key-value pairs separated by a colon (:).
#     - Dictionaries are **mutable**.
#     - Values are accesed by key not by index.
#     - Dictionary keys must be **hashable**.
#  
# <div class="alert alert-block alert-info"><b>Note: </b>
# An object is hashable if it can be passed to a hash function. A hash function is any function that can be used to map data of arbitrary size to fixed-size values. The values returned by a hash function are called hash values, hash codes, digests, or simply hashes. The values are usually used to index a fixed-size table called a hash table, e.g., dictionaries.
#     
# All of the built-in immutable types you have learned about so far are hashable, and the mutable container types (lists and dictionaries) are not. So for present purposes, you can think of hashable and immutable as more or less synonymous (although they are not).
# </div>

# In[82]:


# Dictionaries definition
d1 = {"python": 0, "c": 0, "fortran": 1,}
d2 = dict([(1,1), (2,4), (3,9), (4, 16)])


# In[84]:


# Dictionaries are dynamic 
d1["matlab"] = 1
print(f"{d1 =  }")


# In[86]:


# Accesing values 
d1["python"] 


# In[87]:


# Dictionaries can be nested
people = {"Elena": {"job": "PhD student", "age":26, },
          "Rigoberto":{"job": "unemployed", "age":34, }}
people["Elena"]["age"]


# In[89]:


# Tuples can be keys 
d3 = {(0,0): "origin"}
hash((0,0))


# In[90]:


# List cannot
d3 = {[0,0]: "origin"}


# **Examples of built-in methods**

# In[97]:


a = d1.items() # to access key-value pairs
# Note that a is not a list but is an iterable (check next section)
# To create a list
a = list(d1.items())
a


# In[98]:


d1.keys() # to access keys


# In[99]:


d1.values() # to access values


# In[100]:


d1.update(d2) # merges to dictionaries
d1


# - **Sets:** In Naïve Set Theory a set is just a collection of elements. However, not all collections of objects can be sets (see Russell's paradox). However, we can think of python sets as sets in naïve set theory and apply the same concepts as in mathematics: intersection, union, etc. The characterics of sets are the following:
# 
#     - Sets are unordered.
#     - Set elements are unique. 
#     - A set can be modified, but its elements must be of an immutable type.
#     - Sets can be defined with curly braces ({}).
# 

# In[101]:


# Several sets definitions
set1 = {1, 3, 4, 4}
set2 = set(["python", "fortran", "matlab", "mathematica"])
set3 = set("python")

print(f"{set1 = }")
print(f"{set2 = }")
print(f"{set3 = }")


# In[102]:


# Sets elements have to be immutable
s = set([[2, 3, 4], 1])


# **Examples of built-in methods and operators applied to sets**

# In[107]:


s1 = {'foo', 'bar', 'baz'}
s2 = {'baz', 'qux', 'quux'}

# Union
print(f"{s1 | s2 = }")
print(f"{s1.union(s2) = }")


# In[108]:


s1 = {'foo', 'bar', 'baz'}
s2 = {'baz', 'qux', 'quux'}

# Intersection
print(f"{s1 & s2 = }")
print(f"{s1.intersection(s2) = }")


# In[109]:


s1 = {'foo', 'bar', 'baz'}
s2 = {'baz', 'qux', 'quux'}

# Difference
print(f"{s1 - s2 = }")
print(f"{s1.difference(s2) = }")


# In[110]:


s1 = {'foo', 'bar', 'baz'}
s2 = {'baz', 'qux', 'quux'}

# Check whether two sets are disjoint
print(f"{s1.isdisjoint(s2) = }")


# In[114]:


s1 = {'foo', 'bar', 'baz'}
s2 = {'foo', 'bar', 'baz', 'qux', 'quux'}

# Check whether if a set is subset of another
print(f"{s1.issubset(s2) = }")
print(f"{s1 <= s2 = }")

# Check if subset is proper subset
print(f"{s1 < s2 = }")

# The other way
print(f"{s2.issuperset(s1) = }")
print(f"{s2 >= s1 = }")
print(f"{s2 > s1 = }")


# In[118]:


s1 = {'foo', 'bar', 'baz'}

s1.add('qux') # adding element
print(f"{s1 = }")

s1.remove('qux') # remove element from set. Raises an exception if element not in set
print(f"{s1 = }")

s1.discard('qux') # remove element from set. Does not raise and exception if element not in set
print(f"{s1 = }")

s1.pop() # remove random element from set
print(f"{s1 = }")

