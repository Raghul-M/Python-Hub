"""
STRINGS - Python Fundamentals Practice

This file contains comprehensive practice problems covering all aspects of string manipulation.
Write your solutions after each problem statement.

Topics covered:
- String creation and indexing
- String slicing and negative indexing
- String methods (split, join, replace, strip, etc.)
- String formatting (%, .format(), f-strings)
- Escape characters and raw strings
- String comparison and searching
"""

# =============================================================================
# SECTION 1: STRING CREATION AND INDEXING
# =============================================================================

# Problem 1: String Creation
# Create strings using different methods:
# - Single quotes
# - Double quotes
# - Triple quotes for multi-line strings
# - String constructor str()
# Expected output: Various string creation methods

# Your solution here:


# Problem 2: String Indexing
# Create a string and demonstrate positive indexing
# Access individual characters at different positions
# Expected output: Characters at specific indices

# Your solution here:


# Problem 3: Negative Indexing
# Create a string and demonstrate negative indexing
# Access characters from the end of the string
# Expected output: Characters using negative indices

# Your solution here:


# Problem 4: String Length
# Create strings of different lengths and find their lengths
# Use the len() function
# Expected output: String lengths

# Your solution here:


# Problem 5: String Immutability
# Create a string and demonstrate that strings are immutable
# Try to modify a character and handle the error
# Expected output: Immutability demonstration

# Your solution here:


# =============================================================================
# SECTION 2: STRING SLICING
# =============================================================================

# Problem 6: Basic Slicing
# Create a string and demonstrate basic slicing
# Use start:end syntax to extract substrings
# Expected output: Various substrings

# Your solution here:


# Problem 7: Slicing with Step
# Create a string and demonstrate slicing with step
# Use start:end:step syntax
# Expected output: Stepped substrings

# Your solution here:


# Problem 8: Negative Slicing
# Create a string and demonstrate negative slicing
# Use negative indices in slice operations
# Expected output: Negative slice results

# Your solution here:


# Problem 9: Omitting Slice Parameters
# Create a string and demonstrate omitting slice parameters
# Use :, start:, :end, ::step variations
# Expected output: Default slice behaviors

# Your solution here:


# Problem 10: Reverse String with Slicing
# Create a string and reverse it using slicing
# Use the [::-1] slice
# Expected output: Reversed string

# Your solution here:


# =============================================================================
# SECTION 3: STRING METHODS - SEARCHING AND REPLACING
# =============================================================================

# Problem 11: find() and index() Methods
# Create a string and use find() and index() methods
# Demonstrate the difference between them
# Expected output: Search results and error handling

# Your solution here:


# Problem 12: count() Method
# Create a string and count occurrences of specific characters
# Use the count() method with different parameters
# Expected output: Character counts

# Your solution here:


# Problem 13: replace() Method
# Create a string and use replace() to substitute text
# Demonstrate different replacement scenarios
# Expected output: Replaced strings

# Your solution here:


# Problem 14: startswith() and endswith() Methods
# Create strings and check if they start or end with specific patterns
# Use these methods with different parameters
# Expected output: Pattern matching results

# Your solution here:


# Problem 15: in Operator
# Create strings and use the 'in' operator to check for substrings
# Demonstrate membership testing
# Expected output: Membership test results

# Your solution here:


# =============================================================================
# SECTION 4: STRING METHODS - CASE MANIPULATION
# =============================================================================

# Problem 16: Case Conversion Methods
# Create a string and demonstrate case conversion methods:
# - upper()
# - lower()
# - capitalize()
# - title()
# - swapcase()
# Expected output: Various case conversions

# Your solution here:


# Problem 17: Case Checking Methods
# Create strings and use case checking methods:
# - isupper()
# - islower()
# - istitle()
# - isalpha()
# - isdigit()
# Expected output: Case checking results

# Your solution here:


# Problem 18: Mixed Case Operations
# Create a string with mixed case and perform various operations
# Combine multiple case methods
# Expected output: Complex case manipulations

# Your solution here:


# =============================================================================
# SECTION 5: STRING METHODS - SPLITTING AND JOINING
# =============================================================================

# Problem 19: split() Method
# Create a string and use split() to break it into parts
# Demonstrate different split parameters
# Expected output: Split string parts

# Your solution here:


# Problem 20: join() Method
# Create a list of strings and join them together
# Use different separators
# Expected output: Joined strings

# Your solution here:


# Problem 21: splitlines() Method
# Create a multi-line string and use splitlines()
# Handle different line ending scenarios
# Expected output: Line-by-line splitting

# Your solution here:


# Problem 22: partition() and rpartition() Methods
# Create a string and use partition() methods
# Demonstrate splitting into three parts
# Expected output: Partitioned strings

# Your solution here:


# =============================================================================
# SECTION 6: STRING METHODS - CLEANING AND FORMATTING
# =============================================================================

# Problem 23: strip(), lstrip(), rstrip() Methods
# Create a string with whitespace and use strip methods
# Remove leading, trailing, and both whitespace
# Expected output: Cleaned strings

# Your solution here:


# Problem 24: center(), ljust(), rjust() Methods
# Create a string and use alignment methods
# Demonstrate different alignment options
# Expected output: Aligned strings

# Your solution here:


# Problem 25: zfill() Method
# Create numbers as strings and use zfill() for zero-padding
# Demonstrate different padding scenarios
# Expected output: Zero-padded strings

# Your solution here:


# Problem 26: expandtabs() Method
# Create a string with tabs and use expandtabs()
# Demonstrate different tab sizes
# Expected output: Tab-expanded strings

# Your solution here:


# =============================================================================
# SECTION 7: STRING FORMATTING
# =============================================================================

# Problem 27: % Formatting (Old Style)
# Create strings using % formatting
# Include different format specifiers for various data types
# Expected output: %-formatted strings

# Your solution here:


# Problem 28: .format() Method
# Create strings using the .format() method
# Demonstrate positional and keyword arguments
# Expected output: .format() formatted strings

# Your solution here:


# Problem 29: F-Strings (Formatted String Literals)
# Create strings using f-strings
# Include variables, expressions, and format specifiers
# Expected output: F-string formatted output

# Your solution here:


# Problem 30: Format Specifiers
# Create strings with various format specifiers:
# - Width and precision
# - Alignment and padding
# - Number formatting
# Expected output: Specified format strings

# Your solution here:


# =============================================================================
# SECTION 8: ESCAPE CHARACTERS AND RAW STRINGS
# =============================================================================

# Problem 31: Common Escape Characters
# Create strings with common escape characters:
# - \n (newline)
# - \t (tab)
# - \r (carriage return)
# - \\ (backslash)
# - \" and \' (quotes)
# Expected output: Escaped character strings

# Your solution here:


# Problem 32: Raw Strings
# Create raw strings using the r prefix
# Demonstrate when raw strings are useful
# Expected output: Raw string behavior

# Your solution here:


# Problem 33: Unicode Escape Sequences
# Create strings with Unicode escape sequences
# Use \u and \U for Unicode characters
# Expected output: Unicode character strings

# Your solution here:


# Problem 34: Octal and Hexadecimal Escapes
# Create strings with octal and hexadecimal escape sequences
# Use \ooo and \xhh formats
# Expected output: Numeric escape sequences

# Your solution here:


# =============================================================================
# SECTION 9: STRING COMPARISON AND SEARCHING
# =============================================================================

# Problem 35: String Comparison
# Create strings and compare them using comparison operators
# Demonstrate alphabetical and lexicographical ordering
# Expected output: Comparison results

# Your solution here:


# Problem 36: String Equality
# Create strings and check for equality
# Demonstrate == and != operators
# Expected output: Equality test results

# Your solution here:


# Problem 37: Advanced String Searching
# Create a string and implement advanced search patterns
# Use multiple search methods together
# Expected output: Complex search results

# Your solution here:


# Problem 38: String Validation
# Create functions to validate different string patterns
# Check for specific formats (email, phone, etc.)
# Expected output: Validation results

# Your solution here:


# =============================================================================
# SECTION 10: STRING OPERATIONS AND CONCATENATION
# =============================================================================

# Problem 39: String Concatenation
# Create strings and concatenate them using different methods:
# - + operator
# - += operator
# - join() method
# Expected output: Concatenated strings

# Your solution here:


# Problem 40: String Repetition
# Create a string and use the * operator for repetition
# Demonstrate different repetition scenarios
# Expected output: Repeated strings

# Your solution here:


# Problem 41: String Interpolation
# Create strings using different interpolation methods
# Combine variables and expressions in strings
# Expected output: Interpolated strings

# Your solution here:


# Problem 42: String Templates
# Create string templates and substitute values
# Use the string.Template class
# Expected output: Template substitution

# Your solution here:


# =============================================================================
# SECTION 11: ADVANCED STRING MANIPULATION
# =============================================================================

# Problem 43: String Reversal Techniques
# Create a string and reverse it using different methods:
# - Slicing
# - Loop
# - join() with reversed()
# Expected output: Various reversal methods

# Your solution here:


# Problem 44: Palindrome Check
# Create a function to check if a string is a palindrome
# Handle case sensitivity and spaces
# Expected output: Palindrome test results

# Your solution here:


# Problem 45: Anagram Detection
# Create a function to check if two strings are anagrams
# Handle case sensitivity and spaces
# Expected output: Anagram test results

# Your solution here:


# Problem 46: String Compression
# Create a function to compress repeated characters
# Example: "aaabbc" becomes "a3b2c1"
# Expected output: Compressed strings

# Your solution here:


# Problem 47: String Encryption
# Create a simple string encryption function
# Use character shifting or substitution
# Expected output: Encrypted and decrypted strings

# Your solution here:


# Problem 48: Word Count
# Create a function to count words in a string
# Handle various word separators and edge cases
# Expected output: Word count results

# Your solution here:


# Problem 49: String Statistics
# Create a function to analyze string statistics
# Count characters, words, lines, etc.
# Expected output: String analysis results

# Your solution here:


# Problem 50: Text Processing Pipeline
# Create a text processing pipeline that:
# - Cleans the text
# - Normalizes case
# - Removes extra spaces
# - Counts frequencies
# Expected output: Processed text statistics

# Your solution here:


# =============================================================================
# SECTION 12: STRING REGULAR EXPRESSIONS (BASIC)
# =============================================================================

# Problem 51: Basic Pattern Matching
# Use the re module for basic pattern matching
# Search for simple patterns in strings
# Expected output: Pattern matching results

# Your solution here:


# Problem 52: String Substitution with re
# Use re.sub() to replace patterns in strings
# Demonstrate different substitution scenarios
# Expected output: Pattern substitution results

# Your solution here:


# Problem 53: String Splitting with re
# Use re.split() to split strings based on patterns
# Demonstrate complex splitting scenarios
# Expected output: Pattern-based splitting

# Your solution here:


# Problem 54: String Validation with re
# Use regular expressions to validate string formats
# Check for email, phone, date formats
# Expected output: Format validation results

# Your solution here:


# Problem 55: String Extraction with re
# Use regular expressions to extract specific patterns
# Extract information from structured text
# Expected output: Extracted information

# Your solution here:


# =============================================================================
# BONUS CHALLENGES
# =============================================================================

# Bonus Problem 1: String Diff Algorithm
# Create a simple string difference algorithm
# Highlight differences between two strings
# Expected output: String difference visualization

# Your solution here:


# Bonus Problem 2: String Similarity
# Create a function to calculate string similarity
# Use techniques like Levenshtein distance
# Expected output: Similarity scores

# Your solution here:


# Bonus Problem 3: String Tokenization
# Create a custom string tokenizer
# Handle various tokenization scenarios
# Expected output: Tokenized strings

# Your solution here: 