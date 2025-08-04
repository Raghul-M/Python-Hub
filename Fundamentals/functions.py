"""
FUNCTIONS - Python Fundamentals Practice

This file contains comprehensive practice problems covering all aspects of functions.
Write your solutions after each problem statement.

Topics covered:
- Function definition and calling
- Parameters and arguments (positional, keyword, default)
- Return values and multiple returns
- Variable scope (local, global)
- Lambda functions
- Recursive functions (basic)
"""

# =============================================================================
# SECTION 1: BASIC FUNCTION DEFINITION AND CALLING
# =============================================================================

# Problem 1: Simple Function
# Create a function called greet() that takes a name parameter
# The function should print "Hello, [name]!"
# Call the function with different names
# Expected output: Greeting messages

# Your solution here:


# Problem 2: Function with Return Value
# Create a function called add_numbers() that takes two parameters
# The function should return the sum of the two numbers
# Call the function and print the result
# Expected output: Sum of two numbers

# Your solution here:


# Problem 3: Function with Multiple Parameters
# Create a function called calculate_rectangle_area() that takes length and width
# The function should return the area of the rectangle
# Call the function with different dimensions
# Expected output: Rectangle areas

# Your solution here:


# Problem 4: Function with No Parameters
# Create a function called get_current_time() that returns the current time
# Use the datetime module to get the current time
# Call the function and print the result
# Expected output: Current time

# Your solution here:


# =============================================================================
# SECTION 2: PARAMETERS AND ARGUMENTS
# =============================================================================

# Problem 5: Positional Arguments
# Create a function called describe_person() that takes name, age, and city
# The function should return a description string
# Call the function with positional arguments
# Expected output: Person description

# Your solution here:


# Problem 6: Keyword Arguments
# Create a function called create_profile() that takes username, email, and bio
# Call the function using keyword arguments
# Show the difference between positional and keyword arguments
# Expected output: User profile

# Your solution here:


# Problem 7: Default Parameters
# Create a function called greet_user() with a default greeting message
# The function should take name and greeting (with default "Hello")
# Call the function with and without the greeting parameter
# Expected output: Different greeting variations

# Your solution here:


# Problem 8: Multiple Default Parameters
# Create a function called create_message() with multiple default parameters
# Parameters: recipient, sender="System", subject="No Subject", body=""
# Call the function with different combinations of arguments
# Expected output: Various message configurations

# Your solution here:


# Problem 9: Mixed Parameter Types
# Create a function called process_data() that takes:
# - Required positional parameters
# - Optional keyword parameters with defaults
# - Demonstrate calling with different argument combinations
# Expected output: Flexible function calls

# Your solution here:


# Problem 10: *args (Variable Arguments)
# Create a function called sum_all() that takes any number of arguments
# The function should return the sum of all arguments
# Call the function with different numbers of arguments
# Expected output: Sums of various argument counts

# Your solution here:


# Problem 11: **kwargs (Keyword Arguments)
# Create a function called create_person() that accepts any keyword arguments
# The function should return a dictionary with all the provided information
# Call the function with different keyword arguments
# Expected output: Person dictionaries

# Your solution here:


# Problem 12: Combined *args and **kwargs
# Create a function called log_event() that takes:
# - Required event_type parameter
# - Variable positional arguments for details
# - Variable keyword arguments for metadata
# Expected output: Event logging with flexible parameters

# Your solution here:


# =============================================================================
# SECTION 3: RETURN VALUES AND MULTIPLE RETURNS
# =============================================================================

# Problem 13: Single Return Value
# Create a function called calculate_square() that returns the square of a number
# Call the function and store the result in a variable
# Expected output: Squared number

# Your solution here:


# Problem 14: Multiple Return Values
# Create a function called get_name_parts() that takes a full name
# The function should return first_name, last_name as separate values
# Use tuple unpacking to receive the return values
# Expected output: Separated name parts

# Your solution here:


# Problem 15: Conditional Returns
# Create a function called check_number() that takes a number
# Return "positive" if number > 0, "negative" if < 0, "zero" if == 0
# Expected output: Number classification

# Your solution here:


# Problem 16: Early Return
# Create a function called validate_age() that takes an age
# Return "invalid" immediately if age < 0
# Otherwise, return age category based on ranges
# Expected output: Age validation with early return

# Your solution here:


# Problem 17: Return Different Types
# Create a function called process_input() that takes any input
# Return different types based on the input:
# - String for text input
# - Integer for numeric input
# - List for multiple values
# Expected output: Type-specific processing

# Your solution here:


# Problem 18: Return None Explicitly
# Create a function called find_item() that searches a list for an item
# Return the item if found, None if not found
# Demonstrate explicit None return
# Expected output: Search results with None handling

# Your solution here:


# =============================================================================
# SECTION 4: VARIABLE SCOPE
# =============================================================================

# Problem 19: Local Variables
# Create a function called calculate_tax() with local variables
# Use local variables for calculations
# Demonstrate that local variables are not accessible outside the function
# Expected output: Local variable scope demonstration

# Your solution here:


# Problem 20: Global Variables
# Create a global variable called counter
# Create a function that modifies the global variable
# Use the global keyword to access and modify the global variable
# Expected output: Global variable modification

# Your solution here:


# Problem 21: Variable Shadowing
# Create a global variable and a local variable with the same name
# Demonstrate how local variables shadow global ones
# Show how to access the global variable from within the function
# Expected output: Variable shadowing behavior

# Your solution here:


# Problem 22: Nonlocal Variables
# Create nested functions and demonstrate the nonlocal keyword
# Show how to modify variables from outer function scope
# Expected output: Nonlocal variable usage

# Your solution here:


# Problem 23: Function Parameters and Scope
# Create a function that demonstrates parameter scope
# Show how parameters are local to the function
# Demonstrate parameter modification within the function
# Expected output: Parameter scope behavior

# Your solution here:


# =============================================================================
# SECTION 5: LAMBDA FUNCTIONS
# =============================================================================

# Problem 24: Basic Lambda Function
# Create a lambda function that adds two numbers
# Assign it to a variable and call it
# Expected output: Lambda function result

# Your solution here:


# Problem 25: Lambda with Single Parameter
# Create a lambda function that squares a number
# Use it with different numbers
# Expected output: Squared numbers

# Your solution here:


# Problem 26: Lambda with Conditional Expression
# Create a lambda function that returns "even" or "odd" for a number
# Use conditional expression (ternary operator)
# Expected output: Even/odd classification

# Your solution here:


# Problem 27: Lambda with Built-in Functions
# Create lambda functions to use with map(), filter(), and sorted()
# Demonstrate each built-in function with lambda
# Expected output: Built-in function usage with lambda

# Your solution here:


# Problem 28: Lambda with Multiple Operations
# Create a lambda function that performs multiple operations
# Use it to process a list of numbers
# Expected output: Complex lambda operations

# Your solution here:


# =============================================================================
# SECTION 6: RECURSIVE FUNCTIONS
# =============================================================================

# Problem 29: Basic Recursion
# Create a recursive function called countdown() that counts down from n to 1
# Include a base case to stop recursion
# Expected output: Countdown sequence

# Your solution here:


# Problem 30: Factorial Function
# Create a recursive function called factorial() that calculates n!
# Handle base cases (0! = 1, 1! = 1)
# Expected output: Factorial calculations

# Your solution here:


# Problem 31: Fibonacci Recursion
# Create a recursive function called fibonacci() that returns the nth Fibonacci number
# Include base cases for n = 0 and n = 1
# Expected output: Fibonacci sequence numbers

# Your solution here:


# Problem 32: Recursive List Processing
# Create a recursive function called sum_list() that sums all elements in a list
# Handle empty list as base case
# Expected output: Sum of list elements

# Your solution here:


# Problem 33: Recursive String Processing
# Create a recursive function called reverse_string() that reverses a string
# Handle empty string as base case
# Expected output: Reversed strings

# Your solution here:


# Problem 34: Recursive Directory Traversal
# Create a recursive function that simulates directory traversal
# Use a nested list structure to represent directories
# Expected output: Directory structure traversal

# Your solution here:


# =============================================================================
# SECTION 7: ADVANCED FUNCTION CONCEPTS
# =============================================================================

# Problem 35: Function as Parameter
# Create a function called apply_operation() that takes a function and a value
# Apply the passed function to the value and return the result
# Pass different functions as arguments
# Expected output: Function as parameter usage

# Your solution here:


# Problem 36: Function Returning Function
# Create a function called create_multiplier() that returns a function
# The returned function should multiply its argument by a fixed number
# Expected output: Function factory pattern

# Your solution here:


# Problem 37: Decorator Pattern
# Create a simple decorator function that adds functionality
# Decorate a function to print before and after execution
# Expected output: Decorated function behavior

# Your solution here:


# Problem 38: Function with Side Effects
# Create a function that modifies a list passed as parameter
# Demonstrate the difference between mutable and immutable parameters
# Expected output: Side effect demonstration

# Your solution here:


# Problem 39: Pure Function
# Create a pure function that doesn't modify external state
# The function should only depend on its parameters
# Expected output: Pure function behavior

# Your solution here:


# Problem 40: Function Documentation
# Create a function with proper docstring documentation
# Include parameter descriptions, return value, and examples
# Use help() function to display documentation
# Expected output: Function documentation

# Your solution here:


# =============================================================================
# SECTION 8: FUNCTION DESIGN PATTERNS
# =============================================================================

# Problem 41: Function Overloading Simulation
# Create functions with the same name but different parameter patterns
# Use default parameters and type checking to simulate overloading
# Expected output: Overloaded function behavior

# Your solution here:


# Problem 42: Function Composition
# Create multiple simple functions and compose them together
# Pass the result of one function as input to another
# Expected output: Function composition results

# Your solution here:


# Problem 43: Memoization Pattern
# Create a function that caches its results to avoid repeated calculations
# Use a dictionary to store previously computed values
# Expected output: Memoized function behavior

# Your solution here:


# Problem 44: Callback Function
# Create a function that accepts a callback function
# The function should process data and call the callback with results
# Expected output: Callback function usage

# Your solution here:


# Problem 45: Function with Error Handling
# Create a function that includes try-except blocks
# Handle different types of errors gracefully
# Return appropriate error messages or default values
# Expected output: Error handling in functions

# Your solution here:


# =============================================================================
# BONUS CHALLENGES
# =============================================================================

# Bonus Problem 1: Higher-Order Functions
# Create functions that take functions as parameters and return functions
# Implement map, filter, and reduce equivalents
# Expected output: Higher-order function implementations

# Your solution here:


# Bonus Problem 2: Function Closures
# Create a function that returns a nested function
# The nested function should access variables from the outer function
# Demonstrate closure behavior
# Expected output: Closure demonstration

# Your solution here:


# Bonus Problem 3: Function Generators
# Create a function that yields values instead of returning them
# Use the function in a for loop
# Expected output: Generator function behavior

# Your solution here: 