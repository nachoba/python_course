# Chapter 01 :: A Gentle Introduction to Python
#
# Coding is not just putting together some instructions that work. Good code is
# short, fast, elegant, easy to read and understand, simple, easy to modify and
# extend, easy to scale and refactor, and easy to test.
#
# In this chapter:
#    1. Python's characteristics and ecosystem
#    2. Guidelines on how to get up and running with Python and virtual envs.
#    3. How to run Python programs
#    4. How to organize Python code and its execution model
#
# In order to program, you will need to create and handle objects. The two main
# features any object has are 'properties' and 'methods'.
# Properties are characteristics of an object.
# Methods are things that an object can do.
#
# Coding is simply about managing those objects that live in the subset of the
# world that we´re reproducing in our software.
# You can create, use, reuse, and delete objects as you please.
#
# According to the 'Data Model' chapter of Python documentation:
#     "Objects are Python's abstraction for data. All data in Python is
#      represented by objects or by relations between objects."
#
# For now, all we need to know is that every object has:
#    * An ID (or identity)
#    * A type
#    * A value
#
# Once created, the ID of an object is never changed. It's a unique identifier
# for it, and it's used behind the scenes by Python to retrieve the object when
# we want to use it.
#
# The type also never changes. The type states what operations are supported by
# the object and the possible values that can be asigned.
#
# Finally, the value can be changed or not. If it can, the object is 'mutable',
# otherwise is 'immutable'.
#
# How do We use an Object?
# We give them a name, usually we say this name is the name of a variable.


# How to check the Python version we are using?
import sys
print(sys.version)

# 3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:03:55)
# [GCC 11.2.0]

# About Virtual Enviroments
# =========================

  When working with Python, it is very common to use virtual environments.
  Virtual environments are isolated Python environments, each of which is
  a folder that contains all the necessary executables to use the packages
  that a Python project would need.

  | It is of vital importance that you never install libraries directly at
  | the system level. Take this as a rule: always create a virtual environ-
  | ment when you start a new project.

  There are different methods to carry this out:
      1. Using Anaconda: With 'conda create'
      2. Using Python's 'venv' module
      3. Using the 'virtualenv' third-party Python package

  In this book we use 'venv'

  You First Virtual Environment
  =============================
  
