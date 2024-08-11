# Python Crash Course
## Chater 02 :: Variables and Simple Data Types

### Numbers
Python treats numbers in several different ways, depending on how they're being used.

#### Integers
You can do the usual operations in Python:

```python {cmd}
suma = 2 + 3

resta = 4 -6

division = 3 / 2

mult = 4 * 4
```

#### Floats
Python calls any number with a decimal point a *float*.

#### Underscores in Numbers
When writting long numbers, you can group digits using underscores to make large numbers more readable

```python {cmd}
universe_age = 14_000_000_000
print(universe_age)
```

#### Multiple Assignments
You can assign values to more than one variable using just a single line of code. You will use this technique often when initializing a set of numbers:

```python {cmd}
x, y, z = 0, 0, 0

print(x, y, z)
```

#### Constants
A *constant* is a variable whose value stays the same throughout the life of a program. Python doesn't have built-in constant types, but Python programmers use all capital letters to indicate a variable shuld be treated as a constant and never be changed.

```python {cmd}
NUMBER_OF_LIFES = 5
print(f"You have {NUMBER_OF_LIFES} remaining")
```
