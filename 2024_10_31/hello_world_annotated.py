# This is a comment
# Comments start with a hash (#) and are ignored by the interpreter
# Note: I'm using [brackets] to introduce analogies
# I'll use `backticks` to refer to code elements


# This is a function
# Functions are like a reusable sequence of instructions [a recipe]
# They can take between 0 and infinite inputs, called arguments [ingredients]
# They can return zero or one outputs [cake]
# This function uses the `def` keyword to define a function called `fibonacci`
# It takes one argument, `x`, which is an `int`eger; and returns an `int`eger
def fibonacci(x: int) -> int:
    if x <= 1:
        return 1

    return fibonacci(x - 1) + fibonacci(x - 2)


# `print` is a built-in function that prints a message to the console
# We call it with one argument, a string "Hello World"
# Strings are sequences of characters (letters, numbers, symbols), and are enclosed in quotes (`"` or `'`)
print("Hello World")

# Variables are named containers for storing data
# Here, we define a variable `numbers` and assign it an empty list (a variable-length sequence of arbitrarily-typed elements)
# For example, a list could contain integers [1, 2, 3], strings ["a", "b", "c"], a mix of types [1, "a", 2.0], other lists, etc.
numbers = []

# The `for _ in _:` phrase creates a loop that repeats the code inside for each element in a sequence
# Here, we loop over a range of 20 elements, from 0 to 19
for i in range(20):
    # We call the `fibonacci` function with the current element of the loop
    # Then we convert the `int` result into a string using the `str` function
    # Then we assign it to a variable called `string_number`
    string_number = str(fibonacci(i))

    # Before, we've seen functions called on their own.
    # However, python provides a special syntax so that we can call some functions on objects.
    # Here we append the `string_number` to the `numbers` list using the `append` method
    # This is roughly equivalent to calling `list.append(numbers, string_number)`, and python does this behind the scenes
    numbers.append(string_number)

# The `join` method of a string concatenates the elements of a sequence into a single string.
# Note: the sequence must only contain strings, this is why we converted the numbers to strings before
# This is roughly equivalent to str.join(", ", numbers)
print(", ".join(numbers))

"""
Output:
Hello World
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765
"""