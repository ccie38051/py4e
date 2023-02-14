# Python code examples 

# CHAPTER 1 & 2 - VARIABLES, EXPRESSIONS & STATEMENTS 

# VARIABLES

# Creating a variable and assigning a value
x = 5

# Using the variable in an expression
y = x + 2

# Printing the value of the variable
print(x) # Output: 5

# Printing the value of the expression using the variable
print(y) # Output: 7

In this example, we create a variable x and assign it the value 5. We then use the variable in an expression to create a new variable y with the value 7. Finally, we print the values of both x and y using the print() function. The output shows that x has the value 5 and y has the value 7.


# EXPRESSIONS

# Assigning values to variables
x = 5
y = 3

# Using the variables in an expression
z = x + y * 2

# Printing the value of the expression
print(z) # Output: 11

In this example, we create two variables x and y and assign them the values 5 and 3 respectively. We then use these variables in an expression to create a new variable z. The expression x + y * 2 is evaluated as follows:

y * 2 is evaluated first, resulting in the value 6.
The result of y * 2 (which is 6) is added to the value of x (which is 5), resulting in the value 11.
The value 11 is assigned to the variable z.
Finally, we print the value of z using the print() function, which outputs 11.


# STATEMENTS 

# Assignment statement
x = 5

# Print statement
print("The value of x is:", x)

# Conditional statement
if x > 0:
    print("x is positive")
else:
    print("x is not positive")

# Loop statement
for i in range(3):
    print("The value of i is:", i)

# Function definition statement
def greet(name):
    print("Hello, " + name + "!")

# Function call statement
greet("John")

In this example, we have an assignment statement that assigns the value 5 to the variable x. We then have a print statement that displays the value of x on the screen.

We also have a conditional statement that checks whether x is greater than zero and prints a message based on the result.

We then have a loop statement that repeats a block of code three times, printing the value of the loop variable i on each iteration.

Finally, we have a function definition statement that defines a function called greet which takes a name as a parameter and prints a greeting message. We then have a function call statement that calls the greet function with the argument "John".


# CHAPTER 3 - CONDITIONS STATEMENTS 

x = 5

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

In this example, we create a variable x and assign it the value 5. We then use a conditional statement (using the if, elif, and else keywords) to check the value of x and print a message based on the result.

The first condition x > 0 is true, so the message "x is positive" is printed.

If x were instead equal to 0, the second condition x == 0 would be true and the message "x is zero" would be printed.

If x were negative, neither the first nor the second condition would be true, so the message "x is negative" would be printed as a default in the else block.

Note that the elif block is optional and can be repeated as many times as needed to check additional conditions.


# CHAPTER 4 - FUNCTIONS 


# Define a function that takes two arguments and returns their sum
def add_numbers(x, y):
    return x + y

# Call the function and print the result
result = add_numbers(3, 5)
print(result) # Output: 8

In this example, we define a function called add_numbers that takes two arguments x and y and returns their sum using the return statement.

We then call the function and pass in the arguments 3 and 5. The function returns their sum (8) and we assign the result to a variable called result.

Finally, we print the value of result using the print() function, which outputs 8.

Functions are a powerful tool in programming as they allow you to write reusable blocks of code that can be called multiple times with different arguments.


# CHAPTER 5 - LOOPS AND ITERATION 

# For loop to iterate over a range of numbers
for i in range(5):
    print(i) # Output: 0, 1, 2, 3, 4

# For loop to iterate over a list of items
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) # Output: apple, banana, cherry

# While loop to repeat a block of code until a condition is met
i = 0
while i < 5:
    print(i)
    i += 1 # Increment i by 1 on each iteration

# Nested loop to iterate over multiple ranges of numbers
for i in range(3):
    for j in range(2):
        print(i, j) # Output: (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)


In the first example, we use a for loop to iterate over a range of numbers (from 0 to 4) using the range() function.

In the second example, we use a for loop to iterate over a list of strings (fruits) and print each item in the list.

In the third example, we use a while loop to repeat a block of code until the value of i is no longer less than 5.

In the fourth example, we use a nested loop (a loop inside another loop) to iterate over two ranges of numbers and print each pair of values.

These are just a few examples of the many types of loops that can be used in Python. Loops are a powerful tool in programming as they allow you to repeat blocks of code multiple times with different values or conditions.


# CHAPTER 6 - STRINGS 

# Define a string variable
my_string = "Hello, world!"

# Print the string
print(my_string)

# Get the length of the string
length = len(my_string)
print("Length of string:", length)

# Access individual characters of the string
first_char = my_string[0]
last_char = my_string[-1]
print("First character:", first_char)
print("Last character:", last_char)

# Concatenate two strings
name = "Alice"
greeting = "Hello, " + name + "!"
print(greeting)

# Convert a string to uppercase or lowercase
upper_case = my_string.upper()
lower_case = my_string.lower()
print("Uppercase string:", upper_case)
print("Lowercase string:", lower_case)

This code defines a string variable my_string, prints it to the console, gets the length of the string, accesses individual characters of the string using indexing, concatenates two strings using the + operator, and converts the string to uppercase and lowercase using the upper() and lower() methods, respectively.

