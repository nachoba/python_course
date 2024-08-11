# Python Crash Course
## Chater 02 :: Variables and Simple Data Types

### Variables
Every variable is connected to a *value*, which is the information associated with that variable. You can change the value of a variable in your program at any time.

#### Variables are Labels
Variables are labels that you assign to values. You can also say that a variable references a certain value.

### Strings
A *string* is a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quote around your strings like this:

```python
"This is a string."
'This is also a string.'
```

#### Changing Case in a String with Methods
There are a number of methods that can be applied to string objects.

```python {cmd="python"}
name = "ada lovelace"
print(name.title())
```
```python {cmd}
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```
The `.lower()` method is particularly useful for storing data as you may want to standarize strings before storing them. Then when you want to display information, you'll use the case that makes the most sense for each string.

#### Using Variables in Strings
Sometimes you'll want to use a variable's value inside a string.

```python {cmd}
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```
To insert a variable's value into a string, place the letter `f`  immediately before the opning quotation mark and put braces `{}` around the name or names of any variable you want to use inside the string.

These strings are called *f-strings*, because Python formats the string by replacing the name of nay variable in braces with its value.

Also methods that are associated can be used.

```python {cmd}
first = "ana"
last = "lovelace"
full = f"{first} {last}"
print(f"Hello {full.title()}")
```
#### Stripping Whitespace
Extra whitespace can be confusing in your programs. Python can look for extra whitespace on the right and left sides of a string. To ensure that no whitespice exists at the right side of a string, use the `.rstrip()` method, at the left with `.lstrip()` and from both sides with `.strip()`.

```python {cmd}
favorite_language = '     python    '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
```
#### Removing Prefixes
If you want to remove some prefix you can use the method `.removeprefix("<prefix>")`

```python {cmd}
url = 'https://nostarch.com'
print(url.removeprefix("https://"))
```
```python {cmd}
# Exercise
# use .removesuffix()
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))
```

