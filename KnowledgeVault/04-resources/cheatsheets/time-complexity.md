# ⏰ Time & Space Complexity Cheat Sheet

## 📊 Big O Notation

### Time Complexity Order (Best to Worst)
1. **O(1)** - Constant
2. **O(log n)** - Logarithmic  
3. **O(n)** - Linear
4. **O(n log n)** - Linearithmic
5. **O(n²)** - Quadratic
6. **O(n³)** - Cubic
7. **O(2ⁿ)** - Exponential
8. **O(n!)** - Factorial

### Common Operations

#### Array Operations
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access by index | O(1) | O(1) |
| Search (unsorted) | O(n) | O(1) |
| Search (sorted) | O(log n) | O(1) |
| Insert at end | O(1) amortized | O(1) |
| Insert at beginning | O(n) | O(1) |
| Delete by index | O(n) | O(1) |

#### Linked List Operations
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access by index | O(n) | O(1) |
| Search | O(n) | O(1) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(1) with tail pointer | O(1) |
| Delete by value | O(n) | O(1) |

#### Stack Operations
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Push | O(1) | O(1) |
| Pop | O(1) | O(1) |
| Peek/Top | O(1) | O(1) |

#### Queue Operations
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Enqueue | O(1) | O(1) |
| Dequeue | O(1) | O(1) |
| Front | O(1) | O(1) |

## 🔍 Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable |
|-----------|-----------|--------------|------------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ |

## 🔎 Search Algorithms

| Algorithm | Time Complexity | Space Complexity | Prerequisites |
|-----------|----------------|------------------|---------------|
| Linear Search | O(n) | O(1) | None |
| Binary Search | O(log n) | O(1) | Sorted array |
| Hash Table Search | O(1) average, O(n) worst | O(n) | Hash function |

## 🌳 Tree Operations

### Binary Search Tree (Balanced)
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Search | O(log n) | O(1) |
| Insert | O(log n) | O(1) |
| Delete | O(log n) | O(1) |
| Traversal | O(n) | O(h) where h = height |

### Binary Search Tree (Unbalanced - Worst Case)
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Search | O(n) | O(1) |
| Insert | O(n) | O(1) |
| Delete | O(n) | O(1) |

## 🗺️ Graph Algorithms

### Traversal
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| DFS | O(V + E) | O(V) |
| BFS | O(V + E) | O(V) |

### Shortest Path
| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| Dijkstra | O(V²) or O(E + V log V) | O(V) | Single source, non-negative weights |
| Bellman-Ford | O(VE) | O(V) | Single source, negative weights allowed |
| Floyd-Warshall | O(V³) | O(V²) | All pairs shortest path |

## 💡 Quick Tips

### Time Complexity Rules
1. **Drop constants**: O(2n) = O(n)
2. **Drop non-dominant terms**: O(n² + n) = O(n²)
3. **Different inputs = different variables**: O(a + b), not O(n)

### Space Complexity Tips
1. **Input space doesn't count** (usually)
2. **Auxiliary space** is what we typically measure
3. **Recursive calls** use O(depth) space on call stack

### Common Patterns
- **Two nested loops over same input**: O(n²)
- **Binary search / divide and conquer**: O(log n)
- **Visiting all elements once**: O(n)
- **Recursive with branching factor b, depth d**: O(b^d)

---
*Quick reference for algorithm analysis*
