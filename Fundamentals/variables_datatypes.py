"""
VARIABLES AND DATA TYPES - Python Fundamentals Practice

This file contains comprehensive practice problems covering all aspects of variables and data types.
Write your solutions after each problem statement.

Topics covered:
- Variable assignment and naming conventions
- Basic data types (int, float, str, bool)
- Type conversion and type checking
- Operators (arithmetic, comparison, logical, assignment)
- Variable scope basics
"""

# =============================================================================
# SECTION 1: VARIABLE ASSIGNMENT AND NAMING CONVENTIONS
# =============================================================================

# Problem 1: Basic Variable Assignment
# Create variables for a student's information:
# - student_name (string)
# - student_age (integer)
# - student_height (float in meters)
# - is_enrolled (boolean)
# Use proper naming conventions (snake_case)
# Expected output: Print all variables with descriptive labels

# Your solution here:


# Problem 2: Multiple Assignment
# Assign three different values to three variables in a single line
# Then swap the values of the first and third variables
# Expected output: Print before and after the swap

# Your solution here:


# Problem 3: Variable Naming Validation
# Create variables with the following names and explain why each is valid or invalid:
# - my_variable (should be valid)
# - 2nd_variable (should be invalid)
# - _private_var (should be valid)
# - class (should be invalid)
# - user_name123 (should be valid)
# Expected output: Comments explaining each naming choice

# Your solution here:


# Problem 4: Constants and Magic Numbers
# Create constants for:
# - PI (3.14159)
# - MAX_ATTEMPTS (3)
# - DEFAULT_TIMEOUT (30)
# Then use these constants in a simple calculation
# Expected output: Use constants in a meaningful calculation

# Your solution here:


# =============================================================================
# SECTION 2: BASIC DATA TYPES
# =============================================================================

# Problem 5: Integer Operations
# Create variables for:
# - A large number (at least 6 digits)
# - A negative number
# - Zero
# Perform basic arithmetic operations and demonstrate integer division vs float division
# Expected output: Show the difference between // and / operators

# Your solution here:


# Problem 6: Float Precision and Scientific Notation
# Create variables for:
# - A very small number (use scientific notation)
# - A very large number (use scientific notation)
# - A number with many decimal places
# Demonstrate float precision issues and rounding
# Expected output: Show float precision limitations

# Your solution here:


# Problem 7: String Manipulation
# Create a string variable with your full name
# Demonstrate:
# - String concatenation
# - String repetition
# - String length
# - Accessing individual characters
# Expected output: Various string operations

# Your solution here:


# Problem 8: Boolean Logic
# Create boolean variables for different conditions:
# - is_adult (age >= 18)
# - has_permission (True/False)
# - is_weekend (True/False)
# Demonstrate boolean operations and truthiness
# Expected output: Boolean logic examples

# Your solution here:


# =============================================================================
# SECTION 3: TYPE CONVERSION AND TYPE CHECKING
# =============================================================================

# Problem 9: Type Conversion Functions
# Create variables of different types and convert them:
# - Convert string "123" to integer
# - Convert float 3.14 to string
# - Convert integer 0 to boolean
# - Convert string "True" to boolean
# Expected output: Demonstrate safe and unsafe conversions

# Your solution here:


# Problem 10: Type Checking
# Use type() function to check the type of various variables
# Create a function that accepts any input and returns its type
# Test with different data types
# Expected output: Type checking results

# Your solution here:


# Problem 11: Safe Type Conversion
# Create a function that safely converts a string to integer
# Handle cases where conversion might fail
# Return None if conversion is not possible
# Expected output: Safe conversion with error handling

# Your solution here:


# Problem 12: Complex Type Conversions
# Create a list of mixed data types: ["123", 456, 7.89, "True", "False"]
# Convert each element to its most appropriate type
# Expected output: List with properly typed elements

# Your solution here:


# =============================================================================
# SECTION 4: OPERATORS
# =============================================================================

# Problem 13: Arithmetic Operators
# Create two numeric variables and demonstrate all arithmetic operators:
# - Addition (+)
# - Subtraction (-)
# - Multiplication (*)
# - Division (/)
# - Floor division (//)
# - Modulus (%)
# - Exponentiation (**)
# Expected output: Results of all arithmetic operations

# Your solution here:


# Problem 14: Comparison Operators
# Create variables and demonstrate all comparison operators:
# - Equal (==)
# - Not equal (!=)
# - Greater than (>)
# - Less than (<)
# - Greater than or equal (>=)
# - Less than or equal (<=)
# Test with different data types
# Expected output: Boolean results of comparisons

# Your solution here:


# Problem 15: Logical Operators
# Create boolean variables and demonstrate:
# - AND operator (and)
# - OR operator (or)
# - NOT operator (not)
# - Short-circuit evaluation
# Expected output: Logical operation results

# Your solution here:


# Problem 16: Assignment Operators
# Create a variable and demonstrate all assignment operators:
# - Basic assignment (=)
# - Add and assign (+=)
# - Subtract and assign (-=)
# - Multiply and assign (*=)
# - Divide and assign (/=)
# - Modulus and assign (%=)
# - Exponent and assign (**=)
# Expected output: Variable values after each operation

# Your solution here:


# Problem 17: Operator Precedence
# Create expressions that demonstrate operator precedence:
# - Arithmetic precedence
# - Comparison vs logical operators
# - Parentheses to override precedence
# Expected output: Results showing precedence rules

# Your solution here:


# =============================================================================
# SECTION 5: VARIABLE SCOPE BASICS
# =============================================================================

# Problem 18: Local vs Global Variables
# Create a function that demonstrates local variable scope
# Use the global keyword to modify a global variable
# Show the difference between local and global variables
# Expected output: Demonstrate scope differences

# Your solution here:


# Problem 19: Variable Shadowing
# Create a global variable and a local variable with the same name
# Demonstrate how local variables shadow global ones
# Show how to access the global variable from within the function
# Expected output: Demonstrate shadowing behavior

# Your solution here:


# Problem 20: Nonlocal Variables
# Create nested functions and demonstrate the nonlocal keyword
# Show how to modify variables from outer function scope
# Expected output: Demonstrate nonlocal variable usage

# Your solution here:


# =============================================================================
# SECTION 6: ADVANCED PRACTICE PROBLEMS
# =============================================================================

# Problem 21: Data Type Calculator
# Create a function that takes two values and an operation
# The function should determine the appropriate data types
# and perform the operation safely
# Handle type conversion automatically
# Expected output: Safe calculation with proper typing

# Your solution here:


# Problem 22: Type Validator
# Create a function that validates if a value can be converted to a specific type
# The function should return True if conversion is possible, False otherwise
# Test with various data types and edge cases
# Expected output: Validation results for different conversions

# Your solution here:


# Problem 23: Variable Inspector
# Create a function that takes any variable and returns a dictionary with:
# - Variable name (as string)
# - Variable type
# - Variable value
# - Whether it's mutable or immutable
# Expected output: Detailed variable information

# Your solution here:


# Problem 24: Expression Evaluator
# Create a function that safely evaluates mathematical expressions
# The function should handle different data types and operators
# Include error handling for invalid operations
# Expected output: Safe expression evaluation

# Your solution here:


# Problem 25: Data Type Converter
# Create a function that converts a value to the most appropriate type
# The function should be smart about choosing the best type
# Handle edge cases like empty strings, None values, etc.
# Expected output: Intelligent type conversion

# Your solution here:


# =============================================================================
# BONUS CHALLENGES
# =============================================================================

# Bonus Problem 1: Type-Safe Calculator
# Create a calculator that maintains type safety throughout calculations
# The calculator should handle mixed types intelligently
# Include comprehensive error handling
# Expected output: Type-safe mathematical operations

# Your solution here:


# Bonus Problem 2: Variable Memory Analyzer
# Create a function that analyzes the memory usage of different data types
# Use sys.getsizeof() to measure memory consumption
# Compare memory usage across different types
# Expected output: Memory analysis of various data types

# Your solution here:


# Bonus Problem 3: Dynamic Type System
# Create a simple type system that can track variable types dynamically
# Implement type checking and conversion rules
# Allow for custom type definitions
# Expected output: Basic type system implementation

# Your solution here: 