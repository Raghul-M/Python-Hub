"""
LIST COMPREHENSIONS - Python Fundamentals Practice

This file contains comprehensive practice problems covering all aspects of comprehensions and generator expressions.
Write your solutions after each problem statement.

Topics covered:
- Basic list comprehensions
- List comprehensions with conditions
- Nested list comprehensions
- Dictionary comprehensions
- Set comprehensions
- Generator expressions
"""

# =============================================================================
# SECTION 1: BASIC LIST COMPREHENSIONS
# =============================================================================

# Problem 1: Simple List Comprehension
# Create a list comprehension that generates numbers from 1 to 10
# Use range() function in the comprehension
# Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Your solution here:


# Problem 2: List Comprehension with Transformation
# Create a list comprehension that squares numbers from 1 to 10
# Transform each number using mathematical operation
# Expected output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Your solution here:


# Problem 3: List Comprehension from String
# Create a list comprehension that converts each character in a string to uppercase
# Use a string like "hello world"
# Expected output: ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

# Your solution here:


# Problem 4: List Comprehension with Function Calls
# Create a list comprehension that applies len() to a list of strings
# Use a list of words like ["apple", "banana", "cherry"]
# Expected output: [5, 6, 6]

# Your solution here:


# Problem 5: List Comprehension from Existing List
# Create a list comprehension that doubles each element in an existing list
# Start with [1, 2, 3, 4, 5]
# Expected output: [2, 4, 6, 8, 10]

# Your solution here:


# =============================================================================
# SECTION 2: LIST COMPREHENSIONS WITH CONDITIONS
# =============================================================================

# Problem 6: List Comprehension with if Condition
# Create a list comprehension that generates even numbers from 1 to 20
# Use if condition to filter even numbers
# Expected output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Your solution here:


# Problem 7: List Comprehension with if-else Condition
# Create a list comprehension that converts numbers to "even" or "odd" strings
# Use if-else condition for transformation
# Expected output: ['odd', 'even', 'odd', 'even', 'odd']

# Your solution here:


# Problem 8: List Comprehension with Multiple Conditions
# Create a list comprehension that filters numbers divisible by both 3 and 5
# Use range(1, 101) and multiple conditions
# Expected output: [15, 30, 45, 60, 75, 90]

# Your solution here:


# Problem 9: List Comprehension with String Conditions
# Create a list comprehension that filters words longer than 3 characters
# Use a list of words like ["cat", "dog", "elephant", "bird"]
# Expected output: ['elephant', 'bird']

# Your solution here:


# Problem 10: List Comprehension with Type Checking
# Create a list comprehension that filters integers from a mixed list
# Use isinstance() function for type checking
# Expected output: [1, 2, 3, 4, 5]

# Your solution here:


# =============================================================================
# SECTION 3: NESTED LIST COMPREHENSIONS
# =============================================================================

# Problem 11: Basic Nested List Comprehension
# Create a nested list comprehension that generates a 3x3 matrix
# Each element should be the product of row and column indices
# Expected output: [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Your solution here:


# Problem 12: Nested List Comprehension with Conditions
# Create a nested list comprehension that generates a multiplication table
# Only include products that are less than 20
# Expected output: Filtered multiplication table

# Your solution here:


# Problem 13: Flattening Nested Lists
# Create a list comprehension that flattens a nested list
# Convert [[1, 2, 3], [4, 5, 6], [7, 8, 9]] to [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected output: Flattened list

# Your solution here:


# Problem 14: Nested List Comprehension with String Operations
# Create a nested list comprehension that generates word combinations
# Combine words from two lists
# Expected output: Word combinations

# Your solution here:


# Problem 15: Complex Nested List Comprehension
# Create a nested list comprehension that generates coordinates
# Generate all (x, y) pairs where x and y are in range(3)
# Expected output: Coordinate pairs

# Your solution here:


# =============================================================================
# SECTION 4: DICTIONARY COMPREHENSIONS
# =============================================================================

# Problem 16: Basic Dictionary Comprehension
# Create a dictionary comprehension that maps numbers to their squares
# Use range(1, 6) for keys
# Expected output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Your solution here:


# Problem 17: Dictionary Comprehension from Lists
# Create a dictionary comprehension from two lists
# Use zip() to pair keys and values
# Expected output: Dictionary from paired lists

# Your solution here:


# Problem 18: Dictionary Comprehension with Conditions
# Create a dictionary comprehension that only includes even numbers
# Map numbers to their squares, but only for even numbers
# Expected output: Dictionary with even number mappings

# Your solution here:


# Problem 19: Dictionary Comprehension with String Keys
# Create a dictionary comprehension that maps words to their lengths
# Use a list of words
# Expected output: Word-to-length mapping

# Your solution here:


# Problem 20: Dictionary Comprehension with Value Transformation
# Create a dictionary comprehension that transforms values
# Convert string values to uppercase
# Expected output: Dictionary with transformed values

# Your solution here:


# =============================================================================
# SECTION 5: SET COMPREHENSIONS
# =============================================================================

# Problem 21: Basic Set Comprehension
# Create a set comprehension that generates unique squares
# Use range(1, 6) and square each number
# Expected output: {1, 4, 9, 16, 25}

# Your solution here:


# Problem 22: Set Comprehension with Conditions
# Create a set comprehension that filters unique even numbers
# Use range(1, 21) and filter even numbers
# Expected output: Set of even numbers

# Your solution here:


# Problem 23: Set Comprehension from String
# Create a set comprehension that extracts unique vowels from a string
# Use a string with repeated vowels
# Expected output: Set of unique vowels

# Your solution here:


# Problem 24: Set Comprehension with Multiple Sources
# Create a set comprehension that combines elements from multiple lists
# Flatten and deduplicate elements
# Expected output: Combined unique elements

# Your solution here:


# Problem 25: Set Comprehension with Type Filtering
# Create a set comprehension that filters unique integers
# Use a mixed list with different data types
# Expected output: Set of unique integers

# Your solution here:


# =============================================================================
# SECTION 6: GENERATOR EXPRESSIONS
# =============================================================================

# Problem 26: Basic Generator Expression
# Create a generator expression that yields squares of numbers
# Use range(1, 6) and convert to list for display
# Expected output: [1, 4, 9, 16, 25]

# Your solution here:


# Problem 27: Generator Expression with Conditions
# Create a generator expression that yields even numbers
# Use range(1, 11) and filter even numbers
# Expected output: [2, 4, 6, 8, 10]

# Your solution here:


# Problem 28: Generator Expression with Functions
# Create a generator expression that yields lengths of words
# Use a list of words and apply len() function
# Expected output: Word lengths

# Your solution here:


# Problem 29: Generator Expression Memory Efficiency
# Create a generator expression for large range
# Compare memory usage with list comprehension
# Expected output: Memory-efficient iteration

# Your solution here:


# Problem 30: Generator Expression with sum()
# Create a generator expression that sums squares of numbers
# Use sum() function with generator expression
# Expected output: Sum of squares

# Your solution here:


# =============================================================================
# SECTION 7: COMPREHENSIONS WITH BUILT-IN FUNCTIONS
# =============================================================================

# Problem 31: List Comprehension with map()
# Create a list comprehension that replicates map() functionality
# Apply a function to each element in a list
# Expected output: Transformed list

# Your solution here:


# Problem 32: List Comprehension with filter()
# Create a list comprehension that replicates filter() functionality
# Filter elements based on a condition
# Expected output: Filtered list

# Your solution here:


# Problem 33: List Comprehension with enumerate()
# Create a list comprehension that uses enumerate()
# Generate index-value pairs
# Expected output: Indexed elements

# Your solution here:


# Problem 34: List Comprehension with zip()
# Create a list comprehension that uses zip()
# Combine elements from multiple lists
# Expected output: Combined elements

# Your solution here:


# Problem 35: List Comprehension with range()
# Create a list comprehension that uses range() with step
# Generate sequences with different steps
# Expected output: Stepped sequences

# Your solution here:


# =============================================================================
# SECTION 8: ADVANCED COMPREHENSION PATTERNS
# =============================================================================

# Problem 36: Conditional Expression in Comprehension
# Create a list comprehension with conditional expression
# Use ternary operator for complex conditions
# Expected output: Conditionally transformed list

# Your solution here:


# Problem 37: Multiple Iterables in Comprehension
# Create a list comprehension with multiple iterables
# Use nested loops in comprehension
# Expected output: Cartesian product or similar

# Your solution here:


# Problem 38: Comprehension with Local Variables
# Create a list comprehension that uses local variables
# Calculate intermediate values within comprehension
# Expected output: Computed results

# Your solution here:


# Problem 39: Comprehension with Function Calls
# Create a list comprehension that calls custom functions
# Apply user-defined functions to elements
# Expected output: Function results

# Your solution here:


# Problem 40: Comprehension with Error Handling
# Create a list comprehension that handles potential errors
# Use try-except within comprehension (if possible)
# Expected output: Safe computation results

# Your solution here:


# =============================================================================
# SECTION 9: COMPREHENSIONS VS TRADITIONAL LOOPS
# =============================================================================

# Problem 41: Performance Comparison
# Compare performance of list comprehension vs traditional for loop
# Measure execution time for same operation
# Expected output: Performance comparison

# Your solution here:


# Problem 42: Readability Comparison
# Write the same logic using both comprehension and traditional loop
# Compare readability and maintainability
# Expected output: Both implementations

# Your solution here:


# Problem 43: Memory Usage Comparison
# Compare memory usage of comprehension vs traditional loop
# Measure memory consumption for large operations
# Expected output: Memory usage analysis

# Your solution here:


# Problem 44: Debugging Comparison
# Create examples that are easier to debug with traditional loops
# Show when loops might be preferred over comprehensions
# Expected output: Debugging considerations

# Your solution here:


# Problem 45: Complexity Comparison
# Create complex logic using both approaches
# Compare complexity and clarity
# Expected output: Complexity analysis

# Your solution here:


# =============================================================================
# SECTION 10: PRACTICAL COMPREHENSION APPLICATIONS
# =============================================================================

# Problem 46: Data Processing Pipeline
# Create a data processing pipeline using comprehensions
# Transform, filter, and aggregate data
# Expected output: Processed data

# Your solution here:


# Problem 47: Configuration Parsing
# Create a configuration parser using comprehensions
# Parse and transform configuration data
# Expected output: Parsed configuration

# Your solution here:


# Problem 48: Text Analysis
# Create text analysis functions using comprehensions
# Analyze word frequencies, lengths, etc.
# Expected output: Text analysis results

# Your solution here:


# Problem 49: Matrix Operations
# Create matrix operations using nested comprehensions
# Perform matrix transformations and calculations
# Expected output: Matrix operation results

# Your solution here:


# Problem 50: API Data Processing
# Create API data processing using comprehensions
# Transform and filter API response data
# Expected output: Processed API data

# Your solution here:


# =============================================================================
# SECTION 11: COMPREHENSIONS WITH EXTERNAL LIBRARIES
# =============================================================================

# Problem 51: File Processing with Comprehensions
# Create file processing operations using comprehensions
# Read, filter, and transform file data
# Expected output: Processed file data

# Your solution here:


# Problem 52: JSON Data Processing
# Create JSON data processing using comprehensions
# Parse and transform JSON structures
# Expected output: Processed JSON data

# Your solution here:


# Problem 53: CSV Data Processing
# Create CSV data processing using comprehensions
# Parse and transform CSV data
# Expected output: Processed CSV data

# Your solution here:


# Problem 54: Database Query Results
# Create database query result processing using comprehensions
# Transform and filter query results
# Expected output: Processed query results

# Your solution here:


# Problem 55: Web Scraping Data
# Create web scraping data processing using comprehensions
# Clean and transform scraped data
# Expected output: Processed web data

# Your solution here:


# =============================================================================
# SECTION 12: OPTIMIZATION AND BEST PRACTICES
# =============================================================================

# Problem 56: Comprehension Optimization
# Create optimized versions of comprehensions
# Use efficient algorithms and data structures
# Expected output: Optimized comprehensions

# Your solution here:


# Problem 57: Memory-Efficient Comprehensions
# Create memory-efficient comprehensions
# Use generators and lazy evaluation
# Expected output: Memory-efficient solutions

# Your solution here:


# Problem 58: Readable Comprehensions
# Create highly readable comprehensions
# Use clear variable names and structure
# Expected output: Readable code

# Your solution here:


# Problem 59: Maintainable Comprehensions
# Create maintainable comprehensions
# Use modular approach and documentation
# Expected output: Maintainable code

# Your solution here:


# Problem 60: Testing Comprehensions
# Create test cases for comprehensions
# Verify correctness and edge cases
# Expected output: Test results

# Your solution here:


# =============================================================================
# BONUS CHALLENGES
# =============================================================================

# Bonus Problem 1: Custom Comprehension-like Functions
# Create custom functions that mimic comprehension behavior
# Implement your own comprehension-like functionality
# Expected output: Custom comprehension functions

# Your solution here:


# Bonus Problem 2: Comprehension Performance Profiling
# Create comprehensive performance profiling for comprehensions
# Measure various aspects of comprehension performance
# Expected output: Performance profiles

# Your solution here:


# Bonus Problem 3: Advanced Comprehension Patterns
# Create advanced comprehension patterns and techniques
# Implement complex data transformations
# Expected output: Advanced comprehension examples

# Your solution here: 