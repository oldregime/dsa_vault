#!/usr/bin/env python3
"""
Phase 1: In-Depth OOP Foundations
Module 03: Advanced OOP Mechanics

This module covers advanced OOP features that distinguish intermediate and senior
Python engineers:
1. Multiple Inheritance, the Diamond Problem, and Method Resolution Order (MRO).
2. Cooperative inheritance calls with `super()`.
3. Memory optimization via `__slots__`.
4. Python Descriptors: building reusable, clean database-style property validators.
5. Composition vs. Inheritance: clean architecture design choices.
"""

import sys

# =====================================================================
# 1. MULTIPLE INHERITANCE, DIAMOND PROBLEM & MRO
# =====================================================================
# In Python, multiple inheritance is resolved using the C3 Linearization algorithm.
# Every class has a Method Resolution Order (accessible via Class.mro() or Class.__mro__).

class A:
    def greet(self):
        print("Greeting from A")
        # In cooperative inheritance, super() delegates to the NEXT class in the MRO list,
        # which is NOT necessarily the parent class in the inheritance hierarchy!
        super().greet() if hasattr(super(), "greet") else None

class B(A):
    def greet(self):
        print("Greeting from B")
        super().greet()

class C(A):
    def greet(self):
        print("Greeting from C")
        super().greet()

class D(B, C):
    """
    Diamond Inheritance Structure:
         A
        / \
       B   C
        \ /
         D
    """
    def greet(self):
        print("Greeting from D")
        super().greet()


# =====================================================================
# 2. MEMORY OPTIMIZATION: __slots__
# =====================================================================
# By default, Python objects store instance variables in a dynamic __dict__ dictionary.
# This adds significant memory overhead. __slots__ optimizes this by allocating a fixed
# array of references instead. It prevents dynamic attribute addition.

class RegularObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedObject:
    # Tell Python to allocate memory for only these attributes. No __dict__ is created!
    __slots__ = ("x", "y")
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


# =====================================================================
# 3. PYTHON DESCRIPTORS
# =====================================================================
# Descriptors are classes that implement __get__, __set__, or __delete__ magic methods.
# They are used to reuse setter/getter logic across multiple attributes and classes.

class NonNegativeDescriptor:
    """A descriptor that ensures attributes are always non-negative numbers."""
    def __init__(self, name: str):
        # We store the private name to look up in the owner object's dictionary.
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, 0)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name[1:]} must be a number.")
        if value < 0:
            raise ValueError(f"{self.name[1:]} cannot be negative.")
        setattr(instance, self.name, value)


class Product:
    """Product model utilizing Descriptors for property validation."""
    # We define attributes as descriptors
    price = NonNegativeDescriptor("price")
    quantity = NonNegativeDescriptor("quantity")

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price       # Triggers descriptor's __set__
        self.quantity = quantity # Triggers descriptor's __set__

    def total_value(self) -> float:
        return self.price * self.quantity


# =====================================================================
# 4. COMPOSITION VS INHERITANCE
# =====================================================================
# "Favor composition over inheritance" is a key software design paradigm.
# Inheritance represents an "IS-A" relation, while Composition represents "HAS-A".
# Composition makes code much more modular and resilient to requirements changes.

# Inflexible Inheritance approach:
# class FlyingCar(Car, Airplane) -> leads to MRO nightmare and rigid hierarchy.

# Flexible Composition approach:
class CombustionEngine:
    def start(self):
        return "Vroom"

class ElectricEngine:
    def start(self):
        return "Silent hum"

class Car:
    """The Car HAS-A engine (Composition). We can plug in any engine dynamically!"""
    def __init__(self, engine):
        self.engine = engine  # Composite object

    def start_car(self):
        return f"Car started: {self.engine.start()}"


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("ADVANCED OOP: MRO, COOPERATIVE SUPER, SLOTS, DESCRIPTORS")
    print("==========================================================\n")

    # --- 1. MRO and the Diamond Problem ---
    print("--- 1. Diamond Inheritance & Method Resolution Order (MRO) ---")
    print(f"MRO list of class D: {[cls.__name__ for cls in D.__mro__]}")
    # Sequence of greetings should follow D -> B -> C -> A
    d_instance = D()
    d_instance.greet()
    print()

    # --- 2. Slots memory optimization ---
    print("--- 2. Slots Memory Optimization ---")
    reg = RegularObject(10, 20)
    slot = SlottedObject(10, 20)
    
    print(f"RegularObject has __dict__: {hasattr(reg, '__dict__')}")
    print(f"SlottedObject has __dict__: {hasattr(slot, '__dict__')}")
    
    # Try adding a dynamic attribute
    reg.z = 100  # Works fine
    try:
        slot.z = 100  # Fails because 'z' is not defined in slots
    except AttributeError as e:
        print(f"Adding attribute dynamically to SlottedObject failed (expected): {e}")
        
    # Measure sizes
    # Note: sys.getsizeof shows direct object size, but let's look at dictionaries.
    print(f"RegularObject size: {sys.getsizeof(reg)} bytes (+ dict size: {sys.getsizeof(reg.__dict__)} bytes)")
    print(f"SlottedObject size: {sys.getsizeof(slot)} bytes (No dict! Saved significant memory!)\n")

    # --- 3. Descriptors ---
    print("--- 3. Descriptors for Clean Validation ---")
    laptop = Product("MacBook", 1200.0, 10)
    print(f"Product: {laptop.name}, Total Value: ${laptop.total_value():,.2f}")
    
    try:
        laptop.price = -50  # Throws ValueError
    except ValueError as e:
        print(f"Descriptor validation block triggered: {e}")
        
    try:
        laptop.quantity = "ten"  # Throws TypeError
    except TypeError as e:
        print(f"Descriptor type validation block triggered: {e}")
    print()

    # --- 4. Composition vs Inheritance ---
    print("--- 4. Composition over Inheritance in Action ---")
    v8_car = Car(CombustionEngine())
    ev_car = Car(ElectricEngine())
    print(v8_car.start_car())
    print(ev_car.start_car())
    
    print("\n==========================================================")
    print("Module 03 completed successfully!")
    print("==========================================================")
