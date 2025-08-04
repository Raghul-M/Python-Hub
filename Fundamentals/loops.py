"""
LOOPS - Python Fundamentals Practice

This file contains comprehensive practice problems covering all aspects of loops and iteration.
Write your solutions after each problem statement.

Topics covered:
- for loops with range(), enumerate(), zip()
- while loops and loop control
- break and continue statements
- Nested loops
- Loop with else clause
- Iterating over different data structures
"""

# =============================================================================
# SECTION 1: BASIC FOR LOOPS
# =============================================================================

# Problem 1: Simple For Loop with Range
# Create a for loop that prints numbers from 1 to 10
# Use range() function
# Expected output: Numbers 1 through 10

# Your solution here:


# Problem 2: For Loop with Custom Range
# Create a for loop that prints even numbers from 2 to 20
# Use range() with step parameter
# Expected output: Even numbers 2, 4, 6, ..., 20

# Your solution here:


# Problem 3: For Loop with Negative Step
# Create a for loop that counts down from 10 to 1
# Use range() with negative step
# Expected output: Numbers 10, 9, 8, ..., 1

# Your solution here:


# Problem 4: For Loop with String
# Create a for loop that iterates through each character in a string
# Print each character and its position
# Expected output: Character and index pairs

# Your solution here:


# =============================================================================
# SECTION 2: FOR LOOPS WITH ENUMERATE
# =============================================================================

# Problem 5: Basic Enumerate
# Create a list of fruits and use enumerate() to print each fruit with its index
# Expected output: Index and fruit pairs

# Your solution here:


# Problem 6: Enumerate with Custom Start
# Create a list of colors and use enumerate() starting from 1
# Print "Color 1: red", "Color 2: blue", etc.
# Expected output: Numbered color list

# Your solution here:


# Problem 7: Enumerate with Conditions
# Create a list of numbers and use enumerate() to find and print only even numbers
# Print both the index and the even number
# Expected output: Even numbers with their positions

# Your solution here:


# Problem 8: Enumerate with String Processing
# Create a string and use enumerate() to find vowels
# Print the position and vowel for each vowel found
# Expected output: Vowel positions and characters

# Your solution here:


# =============================================================================
# SECTION 3: FOR LOOPS WITH ZIP
# =============================================================================

# Problem 9: Basic Zip
# Create two lists: names and ages
# Use zip() to pair them together and print each pair
# Expected output: Name-age pairs

# Your solution here:


# Problem 10: Zip with Different Length Lists
# Create lists of different lengths and use zip()
# Observe what happens when lists have different lengths
# Expected output: Zipped pairs (limited by shortest list)

# Your solution here:


# Problem 11: Zip with Three Lists
# Create three lists: first_names, last_names, and scores
# Use zip() to create tuples of all three values
# Expected output: Three-element tuples

# Your solution here:


# Problem 12: Zip with String Processing
# Create two strings of equal length
# Use zip() to compare characters at the same positions
# Print matching and non-matching characters
# Expected output: Character comparison results

# Your solution here:


# =============================================================================
# SECTION 4: WHILE LOOPS
# =============================================================================

# Problem 13: Basic While Loop
# Create a while loop that prints numbers from 1 to 5
# Use a counter variable
# Expected output: Numbers 1 through 5

# Your solution here:


# Problem 14: While Loop with Condition
# Create a while loop that continues until a specific condition is met
# Use a variable that changes during the loop
# Expected output: Loop until condition is satisfied

# Your solution here:


# Problem 15: While Loop with User Input
# Create a while loop that asks for user input until "quit" is entered
# Use input() function (you can simulate this with a list of inputs)
# Expected output: Input processing until quit

# Your solution here:


# Problem 16: While Loop with Counter
# Create a while loop that counts down from a given number to zero
# Print each number during the countdown
# Expected output: Countdown sequence

# Your solution here:


# =============================================================================
# SECTION 5: BREAK AND CONTINUE STATEMENTS
# =============================================================================

# Problem 17: Break Statement
# Create a for loop that breaks when it encounters a specific value
# Use a list of numbers and break when you find a negative number
# Expected output: Numbers until negative value is found

# Your solution here:


# Problem 18: Continue Statement
# Create a for loop that skips even numbers using continue
# Print only odd numbers from 1 to 10
# Expected output: Odd numbers only

# Your solution here:


# Problem 19: Break and Continue Together
# Create a loop that processes a list of strings
# Skip empty strings with continue
# Break when encountering "stop"
# Expected output: Processed strings with skipping and breaking

# Your solution here:


# Problem 20: Break in While Loop
# Create a while loop that breaks when a condition is met
# Use a random number or counter to simulate the condition
# Expected output: Loop until break condition

# Your solution here:


# =============================================================================
# SECTION 6: NESTED LOOPS
# =============================================================================

# Problem 21: Basic Nested Loops
# Create nested for loops to print a multiplication table
# Print table for numbers 1 to 5
# Expected output: 5x5 multiplication table

# Your solution here:


# Problem 22: Nested Loops with Lists
# Create two lists and use nested loops to find common elements
# Print each common element found
# Expected output: Common elements between lists

# Your solution here:


# Problem 23: Nested Loops with Strings
# Create nested loops to find all possible two-letter combinations
# Use a string of letters (e.g., "ABC")
# Expected output: All two-letter combinations

# Your solution here:


# Problem 24: Nested Loops with Conditions
# Create nested loops to process a 2D list (matrix)
# Find and print the maximum value in each row
# Expected output: Maximum values for each row

# Your solution here:


# =============================================================================
# SECTION 7: LOOP WITH ELSE CLAUSE
# =============================================================================

# Problem 25: For Loop with Else
# Create a for loop that searches for a number in a list
# Use else clause to print "Number not found" if loop completes without break
# Expected output: Search result with else clause

# Your solution here:


# Problem 26: While Loop with Else
# Create a while loop that tries to find a condition
# Use else clause to handle the case when condition is never met
# Expected output: Loop result with else handling

# Your solution here:


# Problem 27: Loop Else with Break
# Create a loop that breaks when finding a specific value
# Demonstrate how else clause behaves with and without break
# Expected output: Different else behaviors

# Your solution here:


# Problem 28: Nested Loop with Else
# Create nested loops with else clauses
# Show how else behaves in nested loop scenarios
# Expected output: Nested loop else behavior

# Your solution here:


# =============================================================================
# SECTION 8: ITERATING OVER DATA STRUCTURES
# =============================================================================

# Problem 29: Iterating Over Lists
# Create a list of mixed data types and iterate over it
# Perform different operations based on the data type
# Expected output: Type-specific processing

# Your solution here:


# Problem 30: Iterating Over Tuples
# Create a tuple of coordinates and iterate over it
# Calculate distances or perform other tuple operations
# Expected output: Tuple processing results

# Your solution here:


# Problem 31: Iterating Over Sets
# Create a set of numbers and iterate over it
# Note that sets don't maintain order
# Expected output: Set iteration results

# Your solution here:


# Problem 32: Iterating Over Dictionaries
# Create a dictionary and iterate over:
# - Keys only
# - Values only
# - Key-value pairs
# Expected output: Different dictionary iteration methods

# Your solution here:


# Problem 33: Iterating Over String
# Create a string and iterate over it in different ways:
# - Character by character
# - Word by word (split)
# - Reverse order
# Expected output: Different string iteration methods

# Your solution here:


# Problem 34: Iterating Over Range Objects
# Create different range objects and iterate over them
# Demonstrate range properties and methods
# Expected output: Range iteration examples

# Your solution here:


# =============================================================================
# SECTION 9: ADVANCED LOOP PROBLEMS
# =============================================================================

# Problem 35: Pattern Printing
# Create nested loops to print patterns:
# - Right triangle of asterisks
# - Inverted triangle
# - Diamond pattern
# Expected output: Various patterns

# Your solution here:


# Problem 36: Number Guessing Game
# Create a while loop that implements a number guessing game
# Use random number generation and user input simulation
# Expected output: Interactive guessing game

# Your solution here:


# Problem 37: Prime Number Generator
# Create a loop that generates prime numbers up to a given limit
# Use nested loops and conditions
# Expected output: List of prime numbers

# Your solution here:


# Problem 38: Fibonacci Sequence
# Create a loop that generates Fibonacci numbers
# Use while loop and break when reaching a limit
# Expected output: Fibonacci sequence

# Your solution here:


# Problem 39: Data Processing Pipeline
# Create a loop that processes a list of data through multiple steps:
# - Filter out invalid data
# - Transform data
# - Aggregate results
# Expected output: Processed data pipeline

# Your solution here:


# Problem 40: Matrix Operations
# Create nested loops to perform matrix operations:
# - Transpose a matrix
# - Find diagonal elements
# - Calculate row and column sums
# Expected output: Matrix operation results

# Your solution here:


# =============================================================================
# SECTION 10: LOOP OPTIMIZATION AND BEST PRACTICES
# =============================================================================

# Problem 41: Loop Efficiency
# Compare different ways to iterate over a large range
# Measure performance differences
# Expected output: Performance comparison

# Your solution here:


# Problem 42: List Comprehension vs Loops
# Create the same result using both loops and list comprehensions
# Compare readability and performance
# Expected output: Comparison of approaches

# Your solution here:


# Problem 43: Generator Expressions
# Create generator expressions and compare with regular loops
# Show memory efficiency benefits
# Expected output: Generator vs loop comparison

# Your solution here:


# Problem 44: Loop with Exception Handling
# Create a loop that handles exceptions gracefully
# Continue processing even when errors occur
# Expected output: Error handling in loops

# Your solution here:


# Problem 45: Infinite Loop Prevention
# Create a loop with safeguards to prevent infinite execution
# Use counters, timeouts, or other safety measures
# Expected output: Safe loop execution

# Your solution here:


# =============================================================================
# BONUS CHALLENGES
# =============================================================================

# Bonus Problem 1: Custom Iterator
# Create a custom iterator class that implements __iter__ and __next__
# Make it iterate over a custom data structure
# Expected output: Custom iteration behavior

# Your solution here:


# Bonus Problem 2: Recursive Loop Implementation
# Implement a loop-like behavior using recursion
# Create functions that simulate loop operations
# Expected output: Recursive loop equivalents

# Your solution here:


# Bonus Problem 3: Async Loop Simulation
# Create a simulation of asynchronous loop behavior
# Use time delays and state management
# Expected output: Async-like loop behavior

# Your solution here: 