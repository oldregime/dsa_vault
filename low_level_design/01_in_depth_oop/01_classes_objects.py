#!/usr/bin/env python3
"""
Phase 1: In-Depth OOP Foundations
Module 01: Classes and Objects

This module covers the core mechanics of how classes and objects are represented 
in Python. We deep-dive into:
1. Object Instantiation and the role of `__init__` and `self`.
2. Class Variables vs. Instance Variables (and how they affect memory/state).
3. The lookup mechanism using `__dict__` namespaces.
4. The three types of methods: Instance, Class, and Static methods.
5. Code example displaying Python's memory layout and references.
"""

import sys
import ctypes

class Engine:
    """A helper class to demonstrate association."""
    def __init__(self, horsepower: int, engine_type: str):
        self.horsepower = horsepower
        self.engine_type = engine_type

    def __repr__(self):
        return f"Engine({self.horsepower} HP, {self.engine_type})"


class Vehicle:
    """
    Enterprise-grade demonstration of Python class mechanics.
    """
    # 1. CLASS VARIABLES (shared across all instances of the class)
    total_vehicles_created = 0
    DEFAULT_WHEELS = 4

    def __init__(self, brand: str, model: str, horsepower: int):
        """
        The constructor/initializer.
        - `self` refers to the specific instance of the object being created in memory.
        - Instance variables (brand, model, engine) are unique to this object.
        """
        # 2. INSTANCE VARIABLES (bound to `self`)
        self.brand = brand
        self.model = model
        
        # Composition: Instantiating another class as part of this class
        self.engine = Engine(horsepower, "V8 Turbo")
        
        # Modify a class variable using the class name
        Vehicle.total_vehicles_created += 1

    # 3. INSTANCE METHOD
    # Requires an instance of the class to be called (represented by `self`).
    def get_description(self) -> str:
        """Returns a string representation of the vehicle."""
        return f"{self.brand} {self.model} with {self.engine}"

    # 4. CLASS METHOD
    # Bound to the class and not the instance. Receives the class (`cls`) as the first argument.
    # Often used as alternative constructors (Factory pattern).
    @classmethod
    def create_electric(cls, brand: str, model: str) -> "Vehicle":
        """
        A class method acting as a Factory Constructor.
        Notice that it uses `cls` to instantiate the class, meaning if we subclass Vehicle,
        this method will correctly return an instance of that subclass!
        """
        electric_vehicle = cls(brand, model, 300)
        electric_vehicle.engine.engine_type = "Dual Electric Motor"
        return electric_vehicle

    # 5. STATIC METHOD
    # Bound to the class but behaves like a regular utility function. Does not receive `self` or `cls`.
    # Used for logical grouping of utilities that don't need to read/write state of class/instance.
    @staticmethod
    def calculate_tax(price: float, tax_rate: float) -> float:
        """Pure utility method that calculates sales tax."""
        return price * tax_rate


# Let's write an interactive execution driver to show how namespaces, lookups, and memory work.
if __name__ == "__main__":
    print("==========================================================")
    print("PYTHON OOP FOUNDATIONS: CLASSES, OBJECTS & NAMESPACES")
    print("==========================================================\n")

    # --- 1. Creating Instances ---
    print("--- 1. Instantiating Objects ---")
    car1 = Vehicle("BMW", "M5", 600)
    car2 = Vehicle("Porsche", "911", 450)
    print(f"car1: {car1.get_description()}")
    print(f"car2: {car2.get_description()}")
    print(f"Total vehicles created: {Vehicle.total_vehicles_created}\n")

    # --- 2. Understanding Instance vs. Class Variables ---
    print("--- 2. Instance vs Class Variables ---")
    # Read class variable from Class AND from Instance
    print(f"Vehicle.DEFAULT_WHEELS: {Vehicle.DEFAULT_WHEELS}")
    print(f"car1.DEFAULT_WHEELS:    {car1.DEFAULT_WHEELS}")
    
    # What happens when we modify it on the class?
    print("\nModifying Vehicle.DEFAULT_WHEELS = 6...")
    Vehicle.DEFAULT_WHEELS = 6
    print(f"car1.DEFAULT_WHEELS (reflected): {car1.DEFAULT_WHEELS}")
    print(f"car2.DEFAULT_WHEELS (reflected): {car2.DEFAULT_WHEELS}")
    
    # What happens when we shadow it on car1 (the instance)?
    print("\nShadowing DEFAULT_WHEELS on car1 = 3...")
    car1.DEFAULT_WHEELS = 3
    print(f"car1.DEFAULT_WHEELS (shadowed):  {car1.DEFAULT_WHEELS}")
    print(f"car2.DEFAULT_WHEELS (unchanged): {car2.DEFAULT_WHEELS}")
    print(f"Vehicle.DEFAULT_WHEELS (original): {Vehicle.DEFAULT_WHEELS}\n")

    # --- 3. Namespace Deep-Dive via __dict__ ---
    print("--- 3. Namespace Lookups via __dict__ ---")
    # Python uses __dict__ dictionary to store attributes.
    print(f"car1 Namespace: {car1.__dict__}")
    print(f"car2 Namespace: {car2.__dict__}")
    # Note that DEFAULT_WHEELS is NOT in car2's __dict__, but it IS in car1's __dict__ now!
    # That's why car2 falls back to looking up the attribute on Vehicle.__dict__.
    print(f"Vehicle Class Namespace keys: {list(Vehicle.__dict__.keys())}\n")

    # --- 4. Method Types Demo ---
    print("--- 4. Method Types Demo ---")
    # Class Method (Alternative Constructor)
    tesla = Vehicle.create_electric("Tesla", "Model S")
    print(f"Tesla created via @classmethod: {tesla.get_description()}")
    
    # Static Method
    tax = Vehicle.calculate_tax(100000, 0.08)
    print(f"Static Method Tax Calculation: ${tax:,.2f}\n")

    # --- 5. Memory Layout and Reference Counting ---
    print("--- 5. Under the Hood: Reference Count and Memory ---")
    # sys.getrefcount returns the reference count.
    # Note: it's temporarily increased by 1 because getrefcount takes it as an argument.
    ref_count = sys.getrefcount(car1) - 1
    print(f"Reference count of car1: {ref_count}")
    
    # Let's create a new reference
    another_ref = car1
    print(f"Reference count of car1 (after creating another_ref): {sys.getrefcount(car1) - 1}")
    
    # Check memory address (using id())
    print(f"Memory Address of car1:        {hex(id(car1))}")
    print(f"Memory Address of another_ref: {hex(id(another_ref))} (Identical!)")
    print(f"Memory Address of car2:        {hex(id(car2))} (Different!)")
    
    print("\n==========================================================")
    print("Module 01 completed successfully!")
    print("==========================================================")
