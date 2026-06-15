# Here are some common Python errors:

# SyntaxError: this occurs when invalid Python code is present.
# NameError: this occurs when you're trying to use a variable without declaring it first.
# TypeError: this occurs when the data type you're using doesn't suit what you're trying to do.

# SyntaxError
# One of the most common errors is the SyntaxError, which occurs when you try to run code that is not valid Python – such as a misspelled keyword, a missing colon :, or a missing closing parenthesis.

# For example:

# print(Hello, World!

# # SyntaxError: invalid syntax

# The snippet above will throw a SyntaxError when run because the print() function requires a closing parenthesis. Also, 'Hello, World!' should be surrounded by quotes.

# The full error message might look something like:

#   File "main.py", line 1
#     print(Hello, World!
#                       ^
# SyntaxError: invalid syntax

# The File "main.py", line 1 describes the file name and the line number.
# The little arrow ^ points to where the error was detected.
# Note: The arrow ^ can be misleading sometimes because that's where the program thinks the error is; there are times when the errors happen before where it points!

# # NameError
# Another error you'll often come across is the NameError, which occurs when you're trying to refer to a variable that hasn't yet been made – it could be because you misspelled a variable name or forgot to define the variable!

# For example:

# print(greetings)

# # NameError: name 'greetings' is not defined

# # The snippet above throws a NameError because we hadn't defined a greetings variable. We can fix this by defining the variable beforehand:

# greetings = 'Howdy 🤠'
# print(greetings)

# # # Output: Howdy 🤠

# # TypeError
# One more common error that we will look at is the TypeError. When working with variables of various data types (e.g., numbers, strings, and booleans), you will likely come across this error.

# For example:

# message = 'The air quality is '
# print(message + 28)

# # TypeError: can only concatenate str (not "int") to str

# The message variable is a string data type. If we try to add an integer number 28 to it, a TypeError will be thrown. This can be fixed with something like the built-in str() function or with surrounding the number in quotes:

# message = 'The air quality is '
# print(message + str(28))

# # Output: The air quality is 28
# if True:
# print("Hello")

# | Error               | Think                          |
# | ------------------- | ------------------------------ |
# | SyntaxError         | "Python can't read my code"    |
# | IndentationError    | "Spaces are wrong"             |
# | NameError           | "Variable doesn't exist"       |
# | TypeError           | "Wrong data type"              |
# | ValueError          | "Wrong value"                  |
# | IndexError          | "List position doesn't exist"  |
# | KeyError            | "Dictionary key doesn't exist" |
# | AttributeError      | "Method doesn't belong here"   |
# | ZeroDivisionError   | "Can't divide by zero"         |
# | FileNotFoundError   | "File missing"                 |
# | ModuleNotFoundError | "Module missing"               |
# # 

# a = 12/0
# print(a)


# num = int("hhss")
# print(num)
name ="nandha"
result = name+12
print(result)