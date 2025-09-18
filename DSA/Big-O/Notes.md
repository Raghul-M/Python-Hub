
## Big O Notation – Time & Space Complexity

<img width="1180" height="720" alt="image" src="https://github.com/user-attachments/assets/bceacfc1-4f46-4cb4-944f-f3c29d3edeb5" />
<br><br><br>

Big O notation is a way of measuring how **efficient** an algorithm is.  
It is very useful for writing **optimized and scalable code**.



##### 1. Time Complexity
- Measured in the **number of operations** an algorithm performs.
- Focuses on *how fast* an algorithm runs as the input grows.

##### 2. Space Complexity
- Measured in the **amount of memory** used to complete a task.
- Focuses on *how much memory* an algorithm consumes.

---

####  Three Greek Letters

```
1. Ω (Omega) : Best Case
   - Fastest possible scenario.  
   - Example: finding the element immediately at the start of a list.

2. Θ (Theta) : Average Case 
   - The "expected" running time for most inputs.  

3. O (Big O) : Worst Case 
   - The slowest possible scenario.  
   - Note: When people talk about Big O, they usually mean the worst case.There is no average and best case in Big (o)
```

#### Example
Finding a specific element in a list of size `n`:  
- Ω = Best case (element found at index 1).  
- Θ = Average case (element found somewhere in the middle).  
- O = Worst case (element found at the last index or not found at all).  

---

###  Big O Examples

#### **1. O(n): Linear Time**
Proportional to the size of `n`.  

```python
eg: 

def print_items(n):
    for i in range(n):
        print(i)

print_items(10)  # Runs 10 operations
```




#### **2. Dropping Constants**

If we perform `2n` operations, we don’t write `O(2n)`. Instead, we simplify it to `O(n)`

```python
eg: 

def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items(10)  # Runs 20 operations, still O(n)
```

#### **3. O(n²) : Quadratic Time**

Nested loops – operations grow as `n * n`.

```python
eg:

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)  # Runs 100 operations
```

⚠️ **Note** : Much less efficient from a time complexity standpoint.


#### **4. Dropping Non-Dominant Terms**

`O(n² + n)` → **O(n²)** because `n²` dominates for large `n`.

```python
eg:

def print_items(n):
    for i in range(n):
       for j in range(n):
          print(i,j)
    
    for k in range(n):
       print(k)

print_items(10)
```


#### **5. O(1) : Constant Time**

Runs in the same time regardless of input size.

```python
eg:

def add_num(n):
    return n + n + n

print(add_num(10))  # Always 1 operation
```

✅ **Note :** The most efficient time complexity.


#### **6. O(log n) : Logarithmic Time**

* Problem size is reduced by half each step.
* Common in **binary search**.
* More efficient than O(n) and O(n²).



#### 7. O(n log n) : Linearithmic Time

* Appears in efficient **sorting algorithms** (Merge Sort, Quick Sort).
* Faster than O(n²), slower than O(n).


#### 8. Input Variations

* **O(a + b):** When there are two independent inputs.
* **O(a × b):** When nested loops run over two inputs.

---

#### Big O with Lists

* **Access by index:** O(1)
* **Search by value:** O(n)
* **Insert at end:** O(1)
* **Insert at beginning:** O(n)


#### Cheatsheet Tips
```
1. O(1): Constant → Example: Accessing an array element.
2. O(log n): Divide & Conquer → Example: Binary Search.
3. O(n): Linear → Example: Looping through a list.
4. O(n log n): Efficient sorting → Example: Merge Sort.
5. O(n²): Loop within a loop → Example: Bubble Sort.
```


#### Summary

* **Big O (O):** Worst case → Slowest possible runtime.
* **Theta (Θ):** Average case → Typical runtime.
* **Omega (Ω):** Best case → Fastest runtime.

#### Rules:

* Drop constants → `O(2n)` → **O(n)**
* Drop non-dominant terms → `O(n² + n)` → **O(n²)**


