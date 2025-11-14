# HashMap

## 📋 Overview

A **HashMap** is a data structure that stores **key-value pairs** and allows fast access, insertion, and deletion of values using keys. 

### Key Characteristics:
- **Keys** are required to be **unique** and **immutable** (strings, numbers, tuples)
- **Values** can be any Python object
- In Python, **dictionaries (dict)** are built-in hash maps
- Provides **O(1) average time complexity** for insert, lookup, and delete operations

### Real-World Analogy:
Think of a HashMap like a dictionary or phone book:
- **Key** = Word/Name you're looking up
- **Value** = Definition/Phone number
- **Hash Function** = System that tells you which page the word is on

---

## 🎯 Applications

- **Caching**: Quickly map memory locations to stored values
- **Database Indexing**: Efficiently index tuples for fast retrieval
- **Counting Frequencies**: Efficient data aggregation (word counts, character frequencies)
- **Pattern Matching Algorithms**: Example: Rabin-Karp
- **Lookup Tables**: Fast O(1) access to data
- **Deduplication**: Check if element exists in set

---

## 🔄 How It Works
![[hashmap.webp]]
### 1. Hash Function
- **Purpose**: Converts a key into an index in the underlying **bucket array**
- **Formula**: `index = hash(key) % size`
- **Ideal Case**: Each key maps to a unique index
- **Reality**: Multiple keys may hash to the same index → **Collision**

### 2. Hash Table Structure
```
┌─────────────────────────────────────┐
│  Bucket Array (underlying storage)  │
├─────────────────────────────────────┤
│ [0] → []                             │
│ [1] → [('apple', 10)]              │
│ [2] → [('banana', 20), ('cherry', 30)]
│ [3] → []                             │
└─────────────────────────────────────┘
```

### 3. Collision Handling Methods

#### **Method 1: Chaining (Separate Chaining)**
- Store multiple key-value pairs in the same bucket as a **list or linked list**
- **Pros**: Simple, good for handling many collisions
- **Cons**: Extra memory for storing lists

#### **Method 2: Open Addressing / Rehashing**
- If a collision occurs, find another **empty bucket** using probing:
  - **Linear Probing**: Check next bucket (hash(key) + 1, hash(key) + 2, ...)
  - **Quadratic Probing**: Check at quadratic intervals
  - **Double Hashing**: Use a second hash function
- **Pros**: Better memory usage
- **Cons**: Clustering issues

---

## 💡 Key Operations

### 1. **Insert / Update - set_val(key, value)**
```
1. Calculate bucket index: hashed_key = hash(key) % size
2. Access the bucket at that index
3. Check if key already exists:
   - If YES: Update the value
   - If NO: Append new key-value pair
```

### 2. **Retrieve - get_val(key)**
```
1. Calculate bucket index: hashed_key = hash(key) % size
2. Search through the bucket for the key
3. Return value if found, else return "No record found"
```

### 3. **Delete - delete_val(key)**
```
1. Calculate bucket index: hashed_key = hash(key) % size
2. Search through the bucket for the key
3. Remove the key-value pair if found
```

### 4. **Display - __str__()**
```
1. Iterate through all buckets
2. Convert each bucket to string
3. Display all key-value pairs
```

---

## � Implementation

### Python - Custom HashMap from Scratch

#### **Step 1: Class Creation & Initialization**
```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]
```

**Explanation:**
- `size`: Number of buckets in the hash table
- `self.hash_table`: List of empty lists (each list = one bucket)
- Supports **chaining** for collision handling

---

#### **Step 2: Insert/Update Operation**
```python
def set_val(self, key, val):
    # Calculate which bucket this key belongs to
    hashed_key = hash(key) % self.size
    bucket = self.hash_table[hashed_key]
    
    # Check if key already exists and update it
    for index, (record_key, _) in enumerate(bucket):
        if record_key == key:
            bucket[index] = (key, val)  # Update existing value
            return
    
    # If key doesn't exist, append new pair
    bucket.append((key, val))
```

**Step-by-Step:**
1. `hash(key) % self.size` → Finds bucket index
2. Loop through bucket to find key
3. If found → Update value at that index
4. If not found → Append new key-value pair

---

#### **Step 3: Retrieve Operation**
```python
def get_val(self, key):
    # Find the bucket
    hashed_key = hash(key) % self.size
    bucket = self.hash_table[hashed_key]
    
    # Search for key in bucket
    for record_key, record_val in bucket:
        if record_key == key:
            return record_val
    
    return "No record found"
```

**Step-by-Step:**
1. Calculate bucket index
2. Loop through bucket
3. Return value if key found
4. Return "No record found" if not found

---

#### **Step 4: Delete Operation**
```python
def delete_val(self, key):
    # Find the bucket
    hashed_key = hash(key) % self.size
    bucket = self.hash_table[hashed_key]
    
    # Search and remove key-value pair
    for index, (record_key, _) in enumerate(bucket):
        if record_key == key:
            bucket.pop(index)
            return
```

**Step-by-Step:**
1. Calculate bucket index
2. Loop through bucket
3. Remove pair if key found using `pop(index)`

---

#### **Step 5: Display Operation**
```python
def __str__(self):
    return "".join(str(bucket) for bucket in self.hash_table)
```

**Explanation:**
- Iterates through all buckets
- Converts each bucket to string
- Shows all key-value pairs and distribution

---

### Complete Code Example

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]
    
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        
        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket[index] = (key, val)
                return
        
        bucket.append((key, val))
    
    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        
        for record_key, record_val in bucket:
            if record_key == key:
                return record_val
        
        return "No record found"
    
    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        
        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket.pop(index)
                return
    
    def __str__(self):
        return "".join(str(bucket) for bucket in self.hash_table)


# Usage
ht = HashTable(3)
print("Empty HashMap:", ht)
```

**Output:**
```
Empty HashMap: [][][]
```

---

### Practical Example: Working with HashMap

```python
# Create hash table with 3 buckets
ht = HashTable(3)

# Insert key-value pairs
ht.set_val('apple', 10)
ht.set_val('banana', 20)
ht.set_val('cherry', 30)

print("Hash Table:", ht)
# Output: [('cherry', 30)][('apple', 10)][('banana', 20)]

# Retrieve values
print("Value for 'banana':", ht.get_val('banana'))      # Output: 20
print("Value for 'apple':", ht.get_val('apple'))        # Output: 10

# Update a value
ht.set_val('apple', 50)
print("Updated Hash Table:", ht)
# Output: [('cherry', 30)][('apple', 50)][('banana', 20)]

# Delete a key-value pair
ht.delete_val('banana')
print("After Deletion:", ht)
# Output: [('cherry', 30)][('apple', 50)][]

# Try to retrieve deleted key
print("Value for 'banana':", ht.get_val('banana'))      # Output: No record found
```

**Execution Walkthrough:**
1. `HashTable(3)` → Creates 3 empty buckets: `[][][]`
2. `set_val()` → Adds keys; hash function distributes them across buckets
3. `get_val()` → Retrieves values using key lookup
4. `set_val()` with existing key → Updates the value instead of adding duplicate
5. `delete_val()` → Removes key-value pair from bucket
6. `get_val()` on deleted key → Returns "No record found"

---

## ⏰ Time Complexity

### Average Case (Good Hash Function):
| Operation | Time Complexity |
|-----------|-----------------|
| Insert | **O(1)** |
| Lookup/Retrieve | **O(1)** |
| Delete | **O(1)** |

**Why?** With a good hash function and low collision rate, operations are direct.

### Worst Case (Poor Hash Function / Many Collisions):
| Operation | Time Complexity |
|-----------|-----------------|
| Insert | **O(n)** |
| Lookup/Retrieve | **O(n)** |
| Delete | **O(n)** |

**Why?** If all keys hash to the same bucket (linear search required), it becomes like a linked list.

### Summary:
- **Best Case**: O(1) - Direct access to bucket
- **Average Case**: O(1) - Good distribution across buckets
- **Worst Case**: O(n) - All keys collide in one bucket

---

## � Space Complexity

| Aspect | Complexity |
|--------|-----------|
| Storage for n key-value pairs | **O(n)** |
| Bucket array | **O(m)** where m = number of buckets |
| Chaining overhead | **O(n)** for storing list pointers |

**Total Space**: **O(n + m)** ≈ **O(n)** (typically m is proportional to n)

---

## ✅ Advantages & Disadvantages

### ✅ Advantages:
| Advantage | Explanation |
|-----------|-------------|
| **Fast Access** | O(1) average time for insert, lookup, delete |
| **Flexible Keys** | Supports any hashable type (strings, numbers, tuples) |
| **Flexible Values** | Values can be any Python object |
| **Maintains Insertion Order** | Python 3.7+ dictionaries preserve insertion order |
| **No Array Index Needed** | Don't need to know position; use meaningful keys |
| **Space Efficient** | For large datasets compared to arrays |

### ❌ Disadvantages:
| Disadvantage | Explanation |
|-------------|-------------|
| **Collision Handling** | Collisions slow down operations (worst case O(n)) |
| **Poor Hash Function** | Bad hash functions cause clustering and performance loss |
| **Memory Overhead** | Extra space needed for bucket array, especially with chaining |
| **Unordered (with poor implementation)** | Without optimization, iteration order may be unpredictable |
| **Not Cache-Friendly** | Random memory access patterns may cause cache misses |
| **Load Factor Issues** | Performance degrades when table is too full |

---

## 🔍 Factors Affecting Performance

### 1. **Load Factor**
$$\text{Load Factor} = \frac{\text{Number of Elements (n)}}{\text{Number of Buckets (m)}}$$

- **Low Load Factor** (< 0.75): Few collisions, better performance
- **High Load Factor** (> 0.75): Many collisions, performance degrades
- **Solution**: Rehash (increase bucket count) when load factor exceeds threshold

### 2. **Hash Function Quality**
- **Good hash function**: Distributes keys evenly across buckets
- **Bad hash function**: Creates clustering, many collisions
- **Example**:
  - ❌ Bad: `hash(x) = x % 10` (biased for certain numbers)
  - ✅ Good: Python's built-in `hash()` uses cryptographic principles

### 3. **Collision Resolution**
- **Chaining**: Works well but uses extra memory
- **Open Addressing**: Memory efficient but suffers from clustering

---

## 🔗 Related Concepts

- [[Arrays]] - Underlying data structure for bucket array
- [[Linked Lists]] - Used in chaining for collision handling
- [[Hash Functions]] - Core to converting keys to indices
- [[Hash Sets]] - Similar structure but stores only keys, no values
- [[Tries]] - Alternative for string key storage
- [[B-Trees]] - Alternative for ordered key storage

---

## 🎴 Anki Cards

### Card 1: Basic Definition
**Q:** What is a HashMap and what are its main characteristics?
**A:** A HashMap is a data structure that stores key-value pairs with O(1) average access time. Keys must be unique and immutable, values can be any object. Python's dict is a built-in HashMap.

### Card 2: Core Operations
**Q:** What are the four main operations of a HashMap?
**A:** 
1. **Insert/Update** (set_val) - Add or update a key-value pair
2. **Retrieve** (get_val) - Get value by key
3. **Delete** (delete_val) - Remove a key-value pair
4. **Display** (__str__) - Show all stored pairs

### Card 3: Hash Function
**Q:** What does a hash function do in a HashMap?
**A:** A hash function converts a key into a bucket index using the formula: `index = hash(key) % size`. This determines where the key-value pair is stored.

### Card 4: Collision Handling
**Q:** What are the two main ways to handle hash collisions?
**A:** 
1. **Chaining**: Store multiple pairs in same bucket using lists/linked lists
2. **Open Addressing**: Find another empty bucket using probing (linear, quadratic, or double hashing)

### Card 5: Time Complexity
**Q:** What is the time complexity of HashMap operations?
**A:** 
- Average Case: O(1) for insert, lookup, delete
- Worst Case: O(n) when many collisions occur (all keys hash to same bucket)

### Card 6: Load Factor
**Q:** What is load factor and why does it matter in HashMap?
**A:** Load Factor = n / m (elements / buckets). Lower load factor (< 0.75) means fewer collisions and better performance. When too high, rehashing is needed.

### Card 7: Python Implementation
**Q:** In the custom HashTable implementation, how does set_val handle existing keys?
**A:** It calculates the bucket index, searches the bucket for the key. If found, it updates the value at that index. If not found, it appends a new pair.

### Card 8: Real-World Uses
**Q:** Give 3 real-world applications of HashMaps.
**A:** 
1. **Caching** - Fast lookup of cached values by key
2. **Database Indexing** - Quick retrieval of records by index
3. **Frequency Counting** - Storing counts of elements in data

---

## 📚 Resources

- [GeeksforGeeks - Hashing](https://www.geeksforgeeks.org/hashing-data-structure/)
- [Python Dictionary Documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Visualgo - Hash Table Visualizer](https://visualgo.net/en/hashtable)
- [InterviewBit - Hash Map](https://www.interviewbit.com/courses/programming/topics/hash-map/)

---

**Tags:** #data-structure #hashmap #hashtable #O(1) #python #dictionary #key-value #hashing
**Last Updated:** November 13, 2025
