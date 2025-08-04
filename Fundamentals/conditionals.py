"""
CONDITIONALS - Python Fundamentals Practice

This file contains comprehensive practice problems covering all aspects of conditional statements.
Write your solutions after each problem statement.

Topics covered:
- if, elif, else statements
- Nested conditionals
- Comparison operators in conditions
- Logical operators (and, or, not)
- Ternary operator
- Match-case statements (Python 3.10+)
"""

# =============================================================================
# SECTION 1: BASIC IF STATEMENTS
# =============================================================================

# Problem 1: Simple If Statement
# Create a variable for age and write an if statement to check if someone is an adult
# If they are 18 or older, print "You are an adult"
# Expected output: Conditional message based on age

# Your solution here:


# Problem 2: If-Else Statement
# Create a variable for temperature and write an if-else statement
# If temperature is above 25°C, print "It's hot"
# Otherwise, print "It's not hot"
# Expected output: Temperature-based message

# Your solution here:


# Problem 3: If-Elif-Else Statement
# Create a variable for grade (0-100) and write an if-elif-else statement
# - 90-100: "A"
# - 80-89: "B"
# - 70-79: "C"
# - 60-69: "D"
# - Below 60: "F"
# Expected output: Letter grade based on numeric score

# Your solution here:


# Problem 4: Multiple Conditions
# Create variables for username and password
# Write an if statement that checks if both username and password are correct
# Print appropriate messages for different scenarios
# Expected output: Authentication status messages

# Your solution here:


# =============================================================================
# SECTION 2: COMPARISON OPERATORS IN CONDITIONS
# =============================================================================

# Problem 5: Numeric Comparisons
# Create variables for two numbers and demonstrate all comparison operators:
# - Equal (==)
# - Not equal (!=)
# - Greater than (>)
# - Less than (<)
# - Greater than or equal (>=)
# - Less than or equal (<=)
# Expected output: Results of all comparisons

# Your solution here:


# Problem 6: String Comparisons
# Create string variables and demonstrate string comparison
# Compare strings alphabetically and check for equality
# Show how case sensitivity affects comparisons
# Expected output: String comparison results

# Your solution here:


# Problem 7: Complex Comparisons
# Create variables for a person's age, income, and credit_score
# Write conditions that check multiple criteria:
# - Age >= 18 AND income >= 30000
# - Age >= 21 OR credit_score >= 700
# - NOT (age < 18)
# Expected output: Complex condition results

# Your solution here:


# Problem 8: Range Checking
# Create a variable for a test score and check if it's within valid ranges:
# - Valid range: 0-100
# - Passing range: 60-100
# - Excellent range: 90-100
# Expected output: Range validation results

# Your solution here:


# =============================================================================
# SECTION 3: LOGICAL OPERATORS
# =============================================================================

# Problem 9: AND Operator
# Create variables for user permissions:
# - has_read_permission (boolean)
# - has_write_permission (boolean)
# - has_admin_permission (boolean)
# Write conditions using AND operator for different access levels
# Expected output: Permission-based access control

# Your solution here:


# Problem 10: OR Operator
# Create variables for different conditions:
# - is_weekend (boolean)
# - is_holiday (boolean)
# - is_vacation (boolean)
# Write conditions using OR operator for free time scenarios
# Expected output: Free time detection logic

# Your solution here:


# Problem 11: NOT Operator
# Create boolean variables and demonstrate NOT operator:
# - is_busy (boolean)
# - is_available (boolean)
# - is_offline (boolean)
# Write conditions using NOT to invert logic
# Expected output: Inverted boolean logic

# Your solution here:


# Problem 12: Complex Logical Expressions
# Create variables for a loan application:
# - age (integer)
# - income (float)
# - credit_score (integer)
# - employment_years (integer)
# Write complex conditions for loan approval:
# - Must be 18+ AND have income >= 25000
# - Must have credit_score >= 650 OR employment_years >= 2
# Expected output: Loan approval logic

# Your solution here:


# Problem 13: Short-Circuit Evaluation
# Create functions that demonstrate short-circuit evaluation:
# - A function that returns True and prints a message
# - A function that returns False and prints a message
# - A function that raises an exception
# Show how AND and OR operators short-circuit
# Expected output: Short-circuit behavior demonstration

# Your solution here:


# =============================================================================
# SECTION 4: NESTED CONDITIONALS
# =============================================================================

# Problem 14: Simple Nested If
# Create variables for weather conditions:
# - temperature (float)
# - is_raining (boolean)
# Write nested conditions:
# - If temperature > 20: check if it's raining
# - If raining: "Warm but wet"
# - If not raining: "Nice weather"
# - If temperature <= 20: "Cold weather"
# Expected output: Weather-based recommendations

# Your solution here:


# Problem 15: Multiple Nested Levels
# Create variables for a shopping scenario:
# - has_money (boolean)
# - money_amount (float)
# - item_price (float)
# - is_on_sale (boolean)
# Write nested conditions for purchase decisions
# Expected output: Shopping decision logic

# Your solution here:


# Problem 16: Nested If-Elif-Else
# Create variables for a game character:
# - level (integer)
# - health (integer)
# - mana (integer)
# Write nested conditions for character status:
# - Check level first (1-10, 11-20, 21+)
# - Within each level range, check health and mana
# Expected output: Character status assessment

# Your solution here:


# Problem 17: Complex Nested Logic
# Create variables for a travel booking system:
# - destination (string)
# - budget (float)
# - travel_time (integer in hours)
# - is_peak_season (boolean)
# Write nested conditions for travel recommendations
# Expected output: Travel booking logic

# Your solution here:


# =============================================================================
# SECTION 5: TERNARY OPERATOR
# =============================================================================

# Problem 18: Basic Ternary Operator
# Create a variable for age and use ternary operator to assign:
# - "adult" if age >= 18
# - "minor" if age < 18
# Expected output: Age category using ternary operator

# Your solution here:


# Problem 19: Nested Ternary Operator
# Create variables for test scores and use nested ternary operators:
# - "excellent" if score >= 90
# - "good" if score >= 80
# - "pass" if score >= 60
# - "fail" if score < 60
# Expected output: Grade using nested ternary

# Your solution here:


# Problem 20: Ternary with Functions
# Create a function that returns different values based on a condition
# Use ternary operator to return:
# - "positive" for positive numbers
# - "negative" for negative numbers
# - "zero" for zero
# Expected output: Function with ternary return

# Your solution here:


# =============================================================================
# SECTION 6: MATCH-CASE STATEMENTS (Python 3.10+)
# =============================================================================

# Problem 21: Basic Match-Case
# Create a variable for day of week (1-7) and use match-case:
# - 1: "Monday"
# - 2: "Tuesday"
# - 3: "Wednesday"
# - 4: "Thursday"
# - 5: "Friday"
# - 6: "Saturday"
# - 7: "Sunday"
# - _: "Invalid day"
# Expected output: Day name using match-case

# Your solution here:


# Problem 22: Match-Case with Patterns
# Create a variable that can be different types and use match-case:
# - If it's an integer: "Integer: {value}"
# - If it's a float: "Float: {value}"
# - If it's a string: "String: {value}"
# - If it's None: "None value"
# - If it's anything else: "Unknown type"
# Expected output: Type-based pattern matching

# Your solution here:


# Problem 23: Match-Case with Guards
# Create a variable for age and use match-case with guards:
# - If age < 0: "Invalid age"
# - If 0 <= age < 13: "Child"
# - If 13 <= age < 20: "Teenager"
# - If 20 <= age < 65: "Adult"
# - If age >= 65: "Senior"
# Expected output: Age category with guards

# Your solution here:


# Problem 24: Match-Case with Multiple Patterns
# Create a variable for HTTP status codes and use match-case:
# - 200, 201, 204: "Success"
# - 300, 301, 302: "Redirect"
# - 400, 401, 403, 404: "Client Error"
# - 500, 502, 503: "Server Error"
# - _: "Unknown status"
# Expected output: HTTP status categorization

# Your solution here:


# =============================================================================
# SECTION 7: ADVANCED PRACTICE PROBLEMS
# =============================================================================

# Problem 25: Grade Calculator
# Create a function that calculates letter grades with plus/minus:
# - A+: 97-100, A: 93-96, A-: 90-92
# - B+: 87-89, B: 83-86, B-: 80-82
# - C+: 77-79, C: 73-76, C-: 70-72
# - D+: 67-69, D: 63-66, D-: 60-62
# - F: Below 60
# Expected output: Detailed grade calculation

# Your solution here:


# Problem 26: Password Strength Checker
# Create a function that checks password strength:
# - Must be at least 8 characters
# - Must contain at least one uppercase letter
# - Must contain at least one lowercase letter
# - Must contain at least one digit
# - Must contain at least one special character
# Return strength level: "weak", "medium", "strong"
# Expected output: Password strength assessment

# Your solution here:


# Problem 27: Date Validator
# Create a function that validates a date (month, day, year):
# - Check if month is valid (1-12)
# - Check if day is valid for the given month
# - Handle leap years for February
# - Check if year is reasonable (1900-2100)
# Expected output: Date validation results

# Your solution here:


# Problem 28: Discount Calculator
# Create a function that calculates discounts based on:
# - Purchase amount
# - Customer type (regular, premium, vip)
# - Season (regular, holiday, clearance)
# Apply appropriate discount percentages
# Expected output: Discount calculation logic

# Your solution here:


# Problem 29: Game State Machine
# Create variables for a simple game state:
# - player_health (integer)
# - player_level (integer)
# - has_key (boolean)
# - door_locked (boolean)
# Write conditions for different game states and actions
# Expected output: Game state logic

# Your solution here:


# Problem 30: Error Code Handler
# Create a function that handles different error codes:
# - Network errors (100-199)
# - Authentication errors (200-299)
# - Permission errors (300-399)
# - Data errors (400-499)
# - System errors (500-599)
# Return appropriate error messages and suggested actions
# Expected output: Error handling logic

# Your solution here:


# =============================================================================
# BONUS CHALLENGES
# =============================================================================

# Bonus Problem 1: Advanced Pattern Matching
# Create a function that uses match-case with complex patterns:
# - Tuples with specific structures
# - Lists with specific lengths
# - Custom classes with attributes
# - Nested data structures
# Expected output: Complex pattern matching

# Your solution here:


# Bonus Problem 2: Conditional Expression Builder
# Create a function that builds complex conditional expressions dynamically:
# - Accept a list of conditions and operators
# - Build and evaluate the expression safely
# - Handle parentheses and operator precedence
# Expected output: Dynamic condition evaluation

# Your solution here:


# Bonus Problem 3: State Machine Implementation
# Create a simple state machine using conditionals:
# - Define states and transitions
# - Handle state changes based on conditions
# - Implement state validation
# Expected output: Basic state machine

# Your solution here: 