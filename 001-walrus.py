# Understanding the "Walrus" Operator
# ===================================
# An assignment expression returns a value, while a traditional assignment
# doesn't.

# A traditional assignment
walrus = True

# If were to use
# print(f"{walrus = True}")
# We will get an error

# An assignment expression
print((walrus := True))

# A  'statement' in Python is a unit of code.
# An 'expression' is a special statement that can be evaluated to some value.
# In the first example, there is nothing to be evaluated, so an error occurs.
# In the second example, using the walrus operator := an evaluation occurs.

#One design principle behind the walrus operator is that there are no identical
#code contexts where both an assignment statement using the '=' operator and an
#assignment expression using the ':=' operator would be valid.
#You can't do a plain assignment with the walrus operator:
#>>> walrus := True
#Would produce a SyntaxError

#You could use parentheses around the assignment expression to make it valid.
#>>> (walrus := True)
#While the following will return an error:
#>>> (walrus = True)


# Walrus Operator Use Cases
# =========================
# The Walrus operator can be useful in situations where you'd want to assign values
# to variables within an expression.

def some_func():
    # Assume some expensive computation here
    # time.sleep(1000)
    return 5

# So instead of:
if some_func():
    print(some_func()) # Which is bad practice since computation is happening twice

# or:
a = some_func()
if a:
    print(a)

# Now you can concisely write
if a := some_func():
    print(a)



