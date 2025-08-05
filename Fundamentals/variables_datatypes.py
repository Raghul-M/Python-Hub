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
student_name = "Raghul M"
student_age = 22
student_height = 1.75
is_enrolled = True

print(student_name)
print(student_age)
print(student_height)
print(is_enrolled)

print("=============================================================================")



# Problem 2: Multiple Assignment
# Assign three different values to three variables in a single line
# Then swap the values of the first and third variables
# Expected output: Print before and after the swap

# Your solution here:

a,b,c = 1 , 2 ,3
print("Before swap :")
print(f"a: {a}, b: {b}, c: {c}")
a,c=3,1
print("After swap :")
print(f"a: {a}, b: {b}, c: {c}")

print("=============================================================================")
# Problem 3: Variable Naming Validation
# Create variables with the following names and explain why each is valid or invalid:
# - my_variable (should be valid)
# - 2nd_variable (should be invalid)
# - _private_var (should be valid)
# - class (should be invalid)
# - user_name123 (should be valid)
# Expected output: Comments explaining each naming choice

# Your solution here:
print("""
# my_variable - Valid: Variable names can start with a letter, and underscores are allowed between words.
# 2nd_variable - Invalid: Variable names cannot start with a digit in Python.
# _private_var - Valid: Variable names can start with an underscore; often used to indicate 'private' variables by convention.
# class - Invalid: 'class' is a reserved keyword in Python and cannot be used as a variable name.
# user_name123 - Valid: Variable names can include letters, numbers, and underscores, as long as they don’t start with a number.
""")

print("=============================================================================")


# Problem 4: Constants and Magic Numbers
# Create constants for:
# - PI (3.14159)
# - MAX_ATTEMPTS (3)
# - DEFAULT_TIMEOUT (30)
# Then use these constants in a simple calculation
# Expected output: Use constants in a meaningful calculation

# Your solution here:
import time
PI = 3.14159
MAX_ATTEMPTS = 3
DEFAULT_TIMEOUT = 3

for i in range(MAX_ATTEMPTS) :
    print(PI *1)
    time.sleep(DEFAULT_TIMEOUT)
    
print("=============================================================================")

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

a = 123456
b = -100
c = 0
print("a / b : ",a/b)  # Float division
print("a // b : ",a//b) # Integer division
print("a / c : ",a/c) # ❌ ZeroDivisionError
print("b // c : ",b//c) # ❌ ZeroDivisionError

print("=============================================================================")

# Problem 6: Float Precision and Scientific Notation
# Create variables for:
# - A very small number (use scientific notation)
# - A very large number (use scientific notation)
# - A number with many decimal places
# Demonstrate float precision issues and rounding
# Expected output: Show float precision limitations

# Your solution here:
# Float values
very_small = 1e-10            # Scientific notation for 0.0000000001
very_large = 9.87e+20         # Scientific notation for 987,000,000,000,000,000,000
many_decimals = 0.123456789123456789  # More precision than float supports

# Print values as-is
print("Very small number:", very_small)
print("Very large number:", very_large)
print("Number with many decimals:", many_decimals)

# Demonstrate float precision loss
result = 0.1 + 0.2
print("0.1 + 0.2 =", result)

# Demonstrate rounding
print("Rounded to 10 decimal places:", round(result, 10)) #round(number, ndigits)

# Format using f-string
print(f"Formatted (15 decimal places): {result:.15f}")

print("=============================================================================")

# Problem 7: String Manipulation
# Create a string variable with your full name
# Demonstrate:
# - String concatenation
# - String repetition
# - String length
# - Accessing individual characters
# Expected output: Various string operations

# Your solution here:
f_name = "Raghul"
l_name = "M"
print("String concatenation : ",f_name + l_name)
print("String repetition : ",f_name * 2)
print("Length of name : ", len(f_name+l_name))

for char in f_name:
    print(char)


print("=============================================================================")
# Problem 8: Boolean Logic
# Create boolean variables for different conditions:
# - is_adult (age >= 18)
# - has_permission (True/False)
# - is_weekend (True/False)
# Demonstrate boolean operations and truthiness
# Expected output: Boolean logic examples

# Your solution here:

# Input from user
age = int(input("Enter your age: "))

# Boolean variables based on logic
is_adult = age >= 18         
has_permission = True        
is_weekend = False           

# Show individual boolean states
print("Is adult:", is_adult)
print("Has permission:", has_permission)
print("Is weekend:", is_weekend)

# Demonstrate boolean logic
print("Can access service (adult and has permission):", is_adult and has_permission)
print("Free to go out (weekend or has permission):", is_weekend or has_permission)
print("Restricted (not an adult):", not is_adult)

print("=============================================================================")


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

str_val = "123"
str_val2 = "True"
int_val = 0
float_val = 3.14
bool_val = True

print("String to integer : ",int(str_val))
print("Float to String : ",str(float_val))
print("Integer to boolean : ",bool(int_val))
print("String to boolean : ",bool(str_val2)) #False also consider as True beacuse string is non-empty bool("False") → True

print("=============================================================================")

# Problem 10: Type Checking
# Use type() function to check the type of various variables
# Create a function that accepts any input and returns its type
# Test with different data types
# Expected output: Type checking results

# Your solution here:

def type_check(val):
    return (type(val))

print(type_check("Raghul"))
print(type_check(22))
print(type_check(1.7))
print(type_check(True))

print("=============================================================================")

# Problem 11: Safe Type Conversion
# Create a function that safely converts a string to integer
# Handle cases where conversion might fail
# Return None if conversion is not possible
# Expected output: Safe conversion with error handling

# Your solution here:

def safe_typecheck(val):   
    try:
        conversion = int(val)
        print("Conversion of String to int done : ",conversion)
        return conversion   
    except (ValueError, TypeError):
        print("Conversion failed ")
        return None

safe_typecheck("123")      # Valid string → 123
safe_typecheck("abc")      # Invalid string → None
safe_typecheck(123e-5)     # Float → converted to int → 0
safe_typecheck(None)       # TypeError → None
        
print("=============================================================================")

# Problem 12: Complex Type Conversions
# Create a list of mixed data types: ["123", 456, 7.89, "True", "False"]
# Convert each element to its most appropriate type
# Expected output: List with properly typed elements

# Your solution here:

my_list = ["123", 456, 7.89, "True", "False"]

converted_list = []

for item in my_list:
    if isinstance(item, str): #isinstance(variable, type)
         if item.isdigit():
            converted_list.append(int(item)) 
            # Try to convert to boolean
         elif item.lower() == "true":
            converted_list.append(True)
         elif item.lower() == "false":
            converted_list.append(False)   
         else:
            converted_list.append(item)
    else:
        converted_list.append(item)  # already int or float

print("Converted list:", converted_list)       

print("=============================================================================")

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
# Create two numeric variables
a = 15
b = 4

# Perform arithmetic operations
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Floor Division (a // b):", a // b)
print("Modulus (a % b):", a % b)
print("Exponentiation (a ** b):", a ** b)

print("=============================================================================")


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

# Integer comparisons
a = 10
b = 20

print("a == b:", a == b)           # Equal
print("a != b:", a != b)           # Not equal
print("a > b:", a > b)             # Greater than
print("a < b:", a < b)             # Less than
print("a >= b:", a >= b)           # Greater than or equal
print("a <= b:", a <= b)           # Less than or equal

# String comparisons
x = "hello"
y = "world"

print("x == y:", x == y)           # Equal
print("x != y:", x != y)           # Not equal
print("x > y:", x > y)             # Lexicographic comparison (In Python, strings are compared character by character, based on the Unicode (ASCII) values of the characters)
print("x < y:", x < y)

# Mixed comparisons (int vs float)
print("10 == 10.0:", 10 == 10.0)   # True (int and float comparison)
print("10 != 10.0:", 10 != 10.0)   # False

print("=============================================================================")

# Problem 15: Logical Operators
# Create boolean variables and demonstrate:
# - AND operator (and)
# - OR operator (or)
# - NOT operator (not)
# - Short-circuit evaluation
# Expected output: Logical operation results

# Your solution here:

# Boolean variables
is_logged_in = True
is_admin = True
has_access = True

# AND operator
print("AND example:", is_logged_in and has_access)  # True and True → True

# OR operator
print("OR example:", is_logged_in or is_admin)      # True or False → True

# NOT operator
print("NOT example:", not is_admin)                 # not False → True

# Short-circuit evaluation
def check():
    print("Function check() is called")
    return True

# Short-circuit with OR: If first is True, second is NOT evaluated
print("\nShort-circuit OR:")
print(is_logged_in or check())  # check() won't be called

# Short-circuit with AND: If first is False, second is NOT evaluated
print("\nShort-circuit AND:")
print(is_admin and check())     # check() won't be called

print("=============================================================================")

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
# Start with a base value
x = 10
print("Initial value of x:", x)

# Add and assign
x += 5  # x = x + 5
print("After += 5:", x)

# Subtract and assign
x -= 3  # x = x - 3
print("After -= 3:", x)

# Multiply and assign
x *= 2  # x = x * 2
print("After *= 2:", x)

# Divide and assign
x /= 4  # x = x / 4 → Note: Result becomes float
print("After /= 4:", x)

# Modulus and assign
x %= 3  # x = x % 3
print("After %= 3:", x)

# Exponent and assign
x **= 4  # x = x ** 4
print("After **= 4:", x)

print("=============================================================================")

# Problem 17: Operator Precedence
# Create expressions that demonstrate operator precedence:
# - Arithmetic precedence
# - Comparison vs logical operators
# - Parentheses to override precedence
# Expected output: Results showing precedence rules

# Your solution here:

result1 = 10 + 2 * 3
print("10 + 2 * 3 =", result1)

result2 = (10 + 2) * 3
print("(10 + 2) * 3 =", result2)

a = 5
b = 10
c = 15

result3 = a < b and b < c
print("a < b and b < c:", result3)

result4 = a < (b and c)
print("a < (b and c):", result4)

result5 = 3 + 2 > 4 and not False
print("3 + 2 > 4 and not False:", result5)

print("=============================================================================")

# =============================================================================
# SECTION 5: VARIABLE SCOPE BASICS
# =============================================================================

# Problem 18: Local vs Global Variables
# Create a function that demonstrates local variable scope
# Use the global keyword to modify a global variable
# Show the difference between local and global variables
# Expected output: Demonstrate scope differences

# Your solution here:

x = 10

def local_scope_example():
    x = 5
    print("Inside local_scope_example, x =", x)

def global_scope_example():
    global x
    x = 20
    print("Inside global_scope_example, x =", x)

print("Before any function call, global x =", x)
local_scope_example()
print("After local_scope_example, global x =", x)
global_scope_example()
print("After global_scope_example, global x =", x)

print("=============================================================================")

# Problem 19: Variable Shadowing
# Create a global variable and a local variable with the same name
# Demonstrate how local variables shadow global ones
# Show how to access the global variable from within the function
# Expected output: Demonstrate shadowing behavior

# Your solution here:
x = "Global Variable"

def shadow_example():
    x = "Local Variable"
    print("Inside function (local):", x)
    print("Accessing global inside function:", globals()['x']) #globals()['x'] looks up the global value of the variable named 'x', ignoring any local variable named x inside the function.

shadow_example()
print("Outside function (global):", x)

print("=============================================================================")

# Problem 20: Nonlocal Variables
# Create nested functions and demonstrate the nonlocal keyword
# Show how to modify variables from outer function scope
# Expected output: Demonstrate nonlocal variable usage

# Your solution here:

def outer():
    msg = "Hello"

    def inner():
        nonlocal msg
        msg = "Hi"

    inner()
    print(msg)

outer()

print("=============================================================================")
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
def calculator(val1, val2, operation):
    try:
        if isinstance(val1, str) and val1.isdigit():
            val1 = int(val1)
        elif isinstance(val1, str):
            val1 = float(val1)

        if isinstance(val2, str) and val2.isdigit():
            val2 = int(val2)
        elif isinstance(val2, str):
            val2 = float(val2)

        if operation == '+':
            return val1 + val2
        elif operation == '-':
            return val1 - val2
        elif operation == '*':
            return val1 * val2
        elif operation == '/':
            return val1 / val2
        elif operation == '//':
            return val1 // val2
        elif operation == '%':
            return val1 % val2
        elif operation == '**':
            return val1 ** val2
        else:
            return "Unsupported operation"
    except Exception as e:
        return f"Error: {str(e)}"

print(calculator("12", 3, "+"))
print(calculator("10.5", "2", "*"))
print(calculator(10, "0", "/"))  # Will raise ZeroDivisionError

print("=============================================================================")

# Problem 22: Type Validator
# Create a function that validates if a value can be converted to a specific type
# The function should return True if conversion is possible, False otherwise
# Test with various data types and edge cases
# Expected output: Validation results for different conversions

# Your solution here:
def validate_type(value, target_type):
    try:
        target_type(value)
        return True
    except:
        return False

print(validate_type("123", int))       # True
print(validate_type("abc", int))       # False
print(validate_type("3.14", float))    # True
print(validate_type("True", bool))     # True
print(validate_type("hello", list))    # False
print(validate_type(100, str))         # True
print(validate_type(None, int))        # False

print("=============================================================================")

# Problem 23: Variable Inspector
# Create a function that takes any variable and returns a dictionary with:
# - Variable name (as string)
# - Variable type
# - Variable value
# - Whether it's mutable or immutable
# Expected output: Detailed variable information

# Your solution here:

def variable_inspector(value):
    info = {}
    info['name'] = str(value)
    info['type'] = type(value)
    info['value'] = value

    # Mutable types
    mutable_types = (list, dict, set, bytearray)

    if isinstance(value, mutable_types):
        info['mutability'] = "Mutable"
    else:
        info['mutability'] = "Immutable"

    return info

# Example
result = variable_inspector(123)
print(result)
print("=============================================================================")


