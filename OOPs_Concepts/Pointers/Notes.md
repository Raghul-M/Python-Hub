# Python Memory Management and References

## Understanding Python References
Python doesn't have traditional pointers like C/C++, but uses **references** to objects in memory. Variables are names that point to objects.

## Mutable vs Immutable Objects

### Immutable Objects
- **Cannot be changed** after creation
- Examples: integers, strings, tuples, floats
- When you "modify" them, Python creates a new object
- Multiple variables can reference the same immutable object

```python
num1 = 11
num2 = num1  # Both point to the same integer object
num2 = 22    # num2 now points to a new integer object
# num1 still points to 11
```

### Mutable Objects
- **Can be changed** after creation
- Examples: lists, dictionaries, sets
- When modified, the same object is updated
- Multiple variables referencing the same mutable object see the changes

```python
dict1 = {'val1': 10}
dict2 = dict1  # Both point to the same dictionary object
dict2['val1'] = 20  # Modifies the shared dictionary
# Both dict1 and dict2 now show {'val1': 20}
```

## Memory Addresses (`id()`)
- `id()` function returns the memory address of an object
- Same objects have the same `id()`
- Different objects have different `id()` values

## Garbage Collection
- Python automatically manages memory
- Objects with no references are automatically deleted
- Prevents memory leaks
- Uses reference counting and cycle detection

## Key Takeaways
1. **Immutable objects**: Changes create new objects
2. **Mutable objects**: Changes modify existing objects
3. **References**: Variables point to objects, not contain them
4. **Memory management**: Python handles cleanup automatically
5. **`id()` function**: Shows memory addresses for debugging
