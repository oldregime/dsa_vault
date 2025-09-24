# ArrayList in Java

ArrayList is a resizable array implementation of the List interface that provides dynamic sizing and convenient methods for manipulation.
check

## 1. Basic Declaration and Creation

```java
// Import statement needed
import java.util.ArrayList;

// Declaration and initialization
ArrayList<Integer> numbers = new ArrayList<>();        // Empty ArrayList of Integers
ArrayList<String> names = new ArrayList<>();           // Empty ArrayList of Strings
ArrayList<Double> values = new ArrayList<>(20);        // Initial capacity of 20
```

## 2. Adding Elements

```java
ArrayList<String> fruits = new ArrayList<>();
fruits.add("Apple");                    // Adds to the end
fruits.add("Banana");                   // Adds to the end
fruits.add(1, "Orange");                // Adds at specific index
fruits.addAll(otherFruitsList);         // Adds all elements from another collection
```
`addAll to add multiple element` 
## 3. Accessing Elements

```java
String firstFruit = fruits.get(0);      // Access by index
int size = fruits.size();               // Get number of elements
boolean isEmpty = fruits.isEmpty();     // Check if empty
boolean containsApple = fruits.contains("Apple");  // Check if element exists
int position = fruits.indexOf("Banana"); // Find index of element
```

## 4. Modifying Elements

```java
fruits.set(0, "Mango");                 // Replace element at index 0
fruits.remove(0);                       // Remove by index
fruits.remove("Banana");                // Remove by object
fruits.clear();                         // Remove all elements
```

## 5. Iterating Through ArrayList

```java
// Using for loop easiest and comman
for (int i = 0; i < fruits.size(); i++) {
    System.out.println(fruits.get(i));
}

// Using enhanced for loop
for (String fruit : fruits) {
    System.out.println(fruit);
}

// Using iterator
Iterator<String> it = fruits.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}

// Using forEach (Java 8+)
fruits.forEach(fruit -> System.out.println(fruit));
```

## 6. Converting Between Array and ArrayList

```java
//for printing array really important
System.out.println(Arrays.toString(num));

// ArrayList to Array
String[] fruitArray = fruits.toArray(new String[0]);


// Array to ArrayList
String[] array = {"Apple", "Banana", "Orange"};
ArrayList<String> fruitList = new ArrayList<>(Arrays.asList(array));
```

## 7. Important ArrayList Methods

| Method                      | Description                                            |
| --------------------------- | ------------------------------------------------------ |
| `add(E element)`            | Adds element to the end                                |
| `add(int index, E element)` | Adds element at specified position                     |
| `get(int index)`            | Returns element at specified position                  |
| `set(int index, E element)` | Replaces element at specified position                 |
| `remove(int index)`         | Removes element at specified position                  |
| `remove(Object o)`          | Removes first occurrence of specified element          |
| `size()`                    | Returns number of elements                             |
| `isEmpty()`                 | Returns true if list contains no elements              |
| `clear()`                   | Removes all elements                                   |
| `contains(Object o)`        | Returns true if list contains specified element        |
| `indexOf(Object o)`         | Returns index of first occurrence of specified element |

## 8. ArrayList vs Array

| ArrayList                     | Array                           |
| ----------------------------- | ------------------------------- |
| Dynamic size                  | Fixed size                      |
| Can only store objects        | Can store primitives or objects |
| More memory overhead          | Less memory overhead            |
| Many built-in utility methods | Limited functionality           |
| Generics for type safety      | No built-in type checking       |
| `list.add(element)`           | `array[index] = element`        |

## 9. When to Use ArrayList

- When you need a resizable collection
- When you need frequent insertions and deletions
- When you need a collection of objects (not primitives)
- When you need built-in methods for searching, sorting, etc.