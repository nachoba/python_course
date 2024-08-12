# Python Crash Course
## Chater 03 :: Introducing Lists

### What is a List?
Lists allow you to store sets of information in one place. Lists are one of Python's most powerful features readily accessible to new programmers.

> A *list* is a collection of items in a particular order.

You can put anything you want into a list, and the items in your list don't have to be realted in any particular way. Because a list usually contains more than one element, it's a good idea to make the name of your list plural.

```python {cmd}
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```
#### Accessing Elements in a List
Lists are ordered collections, so you can access any element in a list by telling Python the position, or *index*, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.

```python {cmd}
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

# You can also use a string method on any element of this list as all are strings

print(bicycles[1].title())
```

> ***Index positions start at `0`, not `1`. The first item in a list is at position `0`

Python has a special syntax for accessing the last element in a list. If you ask for the item at index `-1`, Python returns the last item in the list. This convention extends to other negative values as well. The index `-2` returns the second item from the end of the list, the index `-3` returns the third element from the end, and so forth.

```python {cmd}
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
```
#### Using Individual Values from a List
You can use individual values form a list just as you would any other variable.

```python {cmd}
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)
```

#### Exercises
1. Your own list: Think of your favorite mode of transportation, such as a motorcycle or car. Use your list to print a series of statements about these items.

```python {cmd}
cars = ['Toyota', 'Honda', 'Porsche', 'Audi']
message = f"I would like to own a {cars[2]}!!"
print(message)
```
