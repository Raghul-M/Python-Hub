"""
STRINGS - Python Fundamentals Practice

This file contains practice problems covering string manipulation in Python.
Write your solutions after each problem statement.

Topics covered:
- String creation and indexing
- String slicing and negative indexing
- String methods (split, join, replace, strip, etc.)
- String formatting (%, .format(), f-strings)
- Escape characters and raw strings
- String comparison and searching
"""

# Problem 1: String Creation and Indexing
# Create strings using different methods and demonstrate indexing
# Use single quotes, double quotes, triple quotes, and str()
# Access characters using positive and negative indices
# Expected output: String creation and indexing examples

# Your solution here:
name = 'Raghul M'
company = "RedHat"
content = """
Note: You're not required to solve it yet—just understand 
that the question wants you to show how different string definitions and
indexing work in Python.
"""
values = 10
str_value = str(values)
print(name[1])
print(name[-1])
print(name[0])


# Problem 2: String Slicing
# Demonstrate string slicing with different parameters
# Use start:end, start:end:step, negative slicing
# Expected output: Various sliced substrings

# Your solution here:

name = "Careerpod Community"
print(name[0:3])
print(name[0:9:1])
print(name[0:-3])
print(name[::-1])


# Problem 3: Basic String Methods
# Use common string methods: upper(), lower(), title(), capitalize()
# Apply methods to transform string case
# Expected output: Case transformation results

# Your solution here:
name = "Careerpod Community"
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())



# Problem 4: String Search and Replace
# Use find(), index(), replace(), count() methods
# Search for substrings and replace content
# Expected output: Search and replace results

# Your solution here:
name = "Careerpod Community"
value1 = name.find("Community")
value2 = name.index("Community")
value3 = name.replace("Community","Students")
value4 = name.count("e")
print(f'{value1}\n{value2}\n{value3}\n{value4}')


# Problem 5: String Splitting and Joining
# Use split() to break strings and join() to combine
# Handle different delimiters and join characters
# Expected output: Split and join operations

# Your solution here:
name = "Careerpod Community"
splitting = name.split(" ")
joining = "-".join(splitting)
print(splitting)
print(joining)


# Problem 6: String Cleaning
# Use strip(), lstrip(), rstrip() to remove whitespace
# Clean strings from unwanted characters
# Expected output: Cleaned strings

# Your solution here:
text = "   Careerpod Community   "
left_cleaned = text.lstrip()    # Removes leading (left-side) spaces
right_cleaned = text.rstrip()   # Removes trailing (right-side) spaces
fully_cleaned = text.strip()    # Removes both leading and trailing spaces

print(f"Original: '{text}'")
print(f"Left cleaned: '{left_cleaned}'")
print(f"Right cleaned: '{right_cleaned}'")
print(f"Fully cleaned: '{fully_cleaned}'")

messy = "@@Welcome!!"
print(messy.strip("@!"))  # Output: "Welcome"



# Problem 7: String Formatting Methods
# Use % formatting, .format(), and f-strings
# Format strings with variables and expressions
# Expected output: Formatted strings

# Your solution here:

name = "Raghul"
company = "Careerpod"
experience = 2

# 1. Using % formatting (old style)
formatted1 = "My name is %s. I work at %s and have %d years of experience." % (name, company, experience)

# 2. Using str.format() method
formatted2 = "My name is {}. I work at {} and have {} years of experience.".format(name, company, experience)

# 3. Using f-strings (modern and recommended)
formatted3 = f"My name is {name}. I work at {company} and have {experience} years of experience."

print(formatted1)
print(formatted2)
print(formatted3)



# Problem 8: Escape Characters and Raw Strings
# Use escape characters (\n, \t, \", \')
# Create raw strings with r"" prefix
# Expected output: Escape character usage

# Your solution here:
print("Line1\nLine2")
print("Column1\tColumn2")
print("He said, \"Hello!\"")
print('It\'s a sunny day.')

raw_str = r"C:\Users\Raghul\Documents\new_folder"
print(raw_str)



# Problem 9: String Validation
# Check if strings start/end with specific patterns
# Validate string content (isalpha, isdigit, isalnum)
# Expected output: String validation results

# Your solution here:
def string_validation(s):
    results = {
        "Starts with 'Hello'": s.startswith("Hello"),
        "Ends with 'World'": s.endswith("World"),
        "Is alphabet": s.isalpha(),
        "Is digit": s.isdigit(),
        "Is alphanumeric": s.isalnum()
    }
    return results

print(string_validation("HelloWorld"))
print(string_validation("Hello123"))
print(string_validation("12345"))
print(string_validation("JustText"))
print(string_validation("Hello World"))




# Problem 10: String Manipulation
# Combine multiple string operations
# Create a function that processes text (remove extra spaces, capitalize)
# Expected output: Complex string manipulation

# Your solution here: 

def process_text(text):
    # Remove leading and trailing spaces
    cleaned = text.strip()
    
    # Replace multiple internal spaces with a single space
    cleaned = " ".join(cleaned.split())
    
    # Capitalize the first letter of the sentence
    capitalized = cleaned.capitalize()
    
    return capitalized

# Example usage
raw_text = "   hello   from   the   Careerpod    community   "
result = process_text(raw_text)
print(f"Processed Text: '{result}'")
