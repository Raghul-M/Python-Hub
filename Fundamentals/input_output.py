"""
INPUT/OUTPUT - Python Fundamentals Practice

This file contains comprehensive practice problems covering all aspects of input and output operations.
Write your solutions after each problem statement.

Topics covered:
- input() function and type conversion
- print() function with formatting
- f-strings and string formatting
- File I/O (open, read, write, close)
- Command line arguments (basic)
"""

# =============================================================================
# SECTION 1: INPUT FUNCTION AND TYPE CONVERSION
# =============================================================================

# Problem 1: Basic Input
# Use input() to get a user's name and print a greeting
# Note: For practice, you can simulate user input by setting variables
# Expected output: Personalized greeting

# Your solution here:


# Problem 2: Input with Prompt
# Use input() with a descriptive prompt to get user's age
# Convert the input to an integer and perform calculations
# Expected output: Age-based calculations

# Your solution here:


# Problem 3: Multiple Inputs
# Get multiple pieces of information from the user:
# - Name, age, city, and favorite color
# Store each in separate variables
# Expected output: Collected user information

# Your solution here:


# Problem 4: Input Validation
# Get a number from the user and validate it's within a range (1-100)
# Use a loop to keep asking until valid input is received
# Expected output: Validated number input

# Your solution here:


# Problem 5: Type Conversion with Input
# Get different types of input and convert them appropriately:
# - String input (keep as string)
# - Numeric input (convert to int or float)
# - Boolean input (convert "yes"/"no" to True/False)
# Expected output: Properly typed input data

# Your solution here:


# Problem 6: Safe Input Conversion
# Create a function that safely converts user input to different types
# Handle conversion errors gracefully
# Return appropriate default values if conversion fails
# Expected output: Safe type conversion

# Your solution here:


# =============================================================================
# SECTION 2: PRINT FUNCTION WITH FORMATTING
# =============================================================================

# Problem 7: Basic Print
# Use print() to display different types of data:
# - Strings, numbers, lists, dictionaries
# Expected output: Various data types printed

# Your solution here:


# Problem 8: Print with Separator
# Use print() with custom separators between multiple values
# Try different separators: comma, dash, arrow, etc.
# Expected output: Custom-separated output

# Your solution here:


# Problem 9: Print with End Parameter
# Use print() with custom end characters
# Print multiple lines without automatic newlines
# Expected output: Custom line endings

# Your solution here:


# Problem 10: Print with Format Method
# Use the .format() method to format strings
# Include positional and keyword arguments
# Expected output: Formatted string output

# Your solution here:


# Problem 11: Print with % Formatting
# Use % formatting (old-style) to format strings
# Include different format specifiers for numbers and strings
# Expected output: %-formatted strings

# Your solution here:


# Problem 12: Print with Multiple Lines
# Use print() to create multi-line output
# Use triple quotes for multi-line strings
# Expected output: Multi-line formatted output

# Your solution here:


# =============================================================================
# SECTION 3: F-STRINGS AND STRING FORMATTING
# =============================================================================

# Problem 13: Basic F-Strings
# Use f-strings to format strings with variables
# Include different data types in the f-string
# Expected output: F-string formatted output

# Your solution here:


# Problem 14: F-Strings with Expressions
# Use f-strings with expressions and calculations
# Include mathematical operations within the f-string
# Expected output: F-strings with expressions

# Your solution here:


# Problem 15: F-Strings with Format Specifiers
# Use f-strings with format specifiers for numbers
# Include precision, width, and alignment
# Expected output: Formatted numbers in f-strings

# Your solution here:


# Problem 16: F-Strings with Conditional Logic
# Use f-strings with conditional expressions
# Include if-else logic within the f-string
# Expected output: Conditional f-string output

# Your solution here:


# Problem 17: F-Strings with Functions
# Use f-strings with function calls
# Include method calls and built-in functions
# Expected output: F-strings with function results

# Your solution here:


# Problem 18: F-Strings with Dictionaries
# Use f-strings to access dictionary values
# Include nested dictionary access
# Expected output: Dictionary values in f-strings

# Your solution here:


# =============================================================================
# SECTION 4: FILE I/O OPERATIONS
# =============================================================================

# Problem 19: Writing to a File
# Create a text file and write some content to it
# Use the 'w' mode to write data
# Expected output: File created with content

# Your solution here:


# Problem 20: Reading from a File
# Read content from a text file
# Use the 'r' mode to read data
# Print the content to the console
# Expected output: File content displayed

# Your solution here:


# Problem 21: Appending to a File
# Open an existing file and append new content
# Use the 'a' mode to add data without overwriting
# Expected output: File with appended content

# Your solution here:


# Problem 22: Reading File Line by Line
# Read a file line by line using a loop
# Process each line individually
# Expected output: Line-by-line file processing

# Your solution here:


# Problem 23: Using 'with' Statement
# Use the 'with' statement for file operations
# Demonstrate automatic file closing
# Expected output: Safe file handling

# Your solution here:


# Problem 24: File Modes
# Demonstrate different file modes:
# - 'r' (read), 'w' (write), 'a' (append)
# - 'r+' (read and write), 'w+' (write and read)
# Expected output: Different file mode behaviors

# Your solution here:


# Problem 25: Binary File Operations
# Create and read a binary file
# Use 'wb' and 'rb' modes for binary data
# Expected output: Binary file operations

# Your solution here:


# Problem 26: File Error Handling
# Create file operations with proper error handling
# Handle FileNotFoundError and PermissionError
# Expected output: Error-safe file operations

# Your solution here:


# Problem 27: File Path Operations
# Use os.path or pathlib to work with file paths
# Create, join, and manipulate file paths
# Expected output: Path manipulation results

# Your solution here:


# =============================================================================
# SECTION 5: CSV FILE OPERATIONS
# =============================================================================

# Problem 28: Writing CSV Data
# Create a CSV file with some data
# Use the csv module to write structured data
# Expected output: CSV file with data

# Your solution here:


# Problem 29: Reading CSV Data
# Read data from a CSV file
# Parse the CSV data into Python structures
# Expected output: Parsed CSV data

# Your solution here:


# Problem 30: CSV with Headers
# Create a CSV file with headers
# Read and process CSV data with column names
# Expected output: CSV data with headers

# Your solution here:


# Problem 31: CSV Dictionary Reader
# Use DictReader to read CSV data as dictionaries
# Access data by column names
# Expected output: Dictionary-based CSV processing

# Your solution here:


# =============================================================================
# SECTION 6: JSON FILE OPERATIONS
# =============================================================================

# Problem 32: Writing JSON Data
# Create a JSON file with structured data
# Use the json module to serialize Python objects
# Expected output: JSON file with data

# Your solution here:


# Problem 33: Reading JSON Data
# Read and parse JSON data from a file
# Convert JSON back to Python objects
# Expected output: Parsed JSON data

# Your solution here:


# Problem 34: JSON with Custom Objects
# Serialize and deserialize custom Python objects
# Handle complex data structures
# Expected output: Custom object JSON operations

# Your solution here:


# Problem 35: JSON Error Handling
# Handle JSON encoding and decoding errors
# Provide fallback values for invalid JSON
# Expected output: Error-safe JSON operations

# Your solution here:


# =============================================================================
# SECTION 7: COMMAND LINE ARGUMENTS
# =============================================================================

# Problem 36: Basic Command Line Arguments
# Use sys.argv to access command line arguments
# Print all arguments passed to the script
# Expected output: Command line argument processing

# Your solution here:


# Problem 37: Argument Parsing with argparse
# Use argparse module to parse command line arguments
# Create a simple script with required and optional arguments
# Expected output: Structured argument parsing

# Your solution here:


# Problem 38: Argument Types and Validation
# Use argparse with different argument types
# Add validation for numeric arguments
# Expected output: Type-validated arguments

# Your solution here:


# Problem 39: Help and Usage Information
# Create a script with help information
# Use argparse to generate usage documentation
# Expected output: Help system implementation

# Your solution here:


# Problem 40: Subcommands with argparse
# Create a script with multiple subcommands
# Use argparse subparsers for different operations
# Expected output: Multi-command script structure

# Your solution here:


# =============================================================================
# SECTION 8: ADVANCED I/O OPERATIONS
# =============================================================================

# Problem 41: File Copying
# Create a function to copy files
# Handle different file types and sizes
# Expected output: File copying functionality

# Your solution here:


# Problem 42: Directory Operations
# Create and manipulate directories
# List directory contents
# Expected output: Directory management

# Your solution here:


# Problem 43: File Searching
# Create a function to search for files
# Implement pattern matching and filtering
# Expected output: File search results

# Your solution here:


# Problem 44: Logging to File
# Set up logging to write to a file
# Include different log levels and formatting
# Expected output: File-based logging

# Your solution here:


# Problem 45: Configuration File Handling
# Read and write configuration files
# Use different formats (INI, JSON, YAML)
# Expected output: Configuration management

# Your solution here:


# =============================================================================
# SECTION 9: STREAM PROCESSING
# =============================================================================

# Problem 46: Reading Large Files
# Process large files efficiently
# Use generators to handle memory constraints
# Expected output: Memory-efficient file processing

# Your solution here:


# Problem 47: Data Streaming
# Create a data streaming pipeline
# Process data as it's being read
# Expected output: Streaming data processing

# Your solution here:


# Problem 48: File Compression
# Work with compressed files (gzip, zip)
# Read and write compressed data
# Expected output: Compression operations

# Your solution here:


# Problem 49: Network I/O Simulation
# Simulate network I/O operations
# Handle connection timeouts and retries
# Expected output: Network I/O patterns

# Your solution here:


# Problem 50: Database-like File Operations
# Create simple database-like file operations
# Implement CRUD operations on file-based data
# Expected output: File-based data management

# Your solution here:


# =============================================================================
# BONUS CHALLENGES
# =============================================================================

# Bonus Problem 1: Interactive Console Application
# Create an interactive console application
# Use input() and print() to create a menu-driven interface
# Expected output: Interactive application

# Your solution here:


# Bonus Problem 2: File Synchronization
# Create a simple file synchronization system
# Compare and update files based on timestamps
# Expected output: File synchronization

# Your solution here:


# Bonus Problem 3: Data Export/Import System
# Create a system that can export/import data in multiple formats
# Support CSV, JSON, and custom formats
# Expected output: Multi-format data handling

# Your solution here: 