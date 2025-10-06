# Python Classes 

## What are Classes?
Classes are user-defined data types that serve as blueprints for creating objects. They encapsulate data (attributes) and behavior (methods) into a single unit.

## Key Concepts

### 1. Class Definition
```python
class ClassName:
    # class body
```

### 2. Constructor (`__init__`) 
- Special method called when an object is created
- Used to initialize object attributes
- Always takes `self` as the first parameter

```python
def __init__(self, parameter1, parameter2):
    self.attribute1 = parameter1
    self.attribute2 = parameter2
```

### 3. `self` Parameter
- Refers to the instance of the class
- Must be the first parameter in instance methods
- Allows access to instance attributes and methods

### 4. Object Creation
```python
object_name = ClassName(arg1, arg2)
```

### 5. Accessing Attributes and Methods
```python
# Access attributes
object_name.attribute

# Call methods
object_name.method_name()
```

## Simple Example

```python
class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

# Creating objects
cookie_one = Cookie("red")
print(cookie_one.get_color())

cookie_one.set_color("blue")
print(cookie_one.get_color())
```

### What This Example Shows:
- **Constructor**: `__init__` method initializes the cookie with a color
- **Getter Method**: `get_color()` returns the current color
- **Setter Method**: `set_color()` changes the color
- **Object Creation**: `Cookie("red")` creates a new cookie object
- **Method Calls**: Using dot notation to call methods on objects

## Key Benefits
- **Encapsulation**: Data and methods are bundled together
- **Reusability**: Create multiple objects from the same class
- **Organization**: Code is more structured and maintainable
- **Abstraction**: Hide complex implementation details
