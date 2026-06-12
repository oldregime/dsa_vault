#!/usr/bin/env python3
"""
Phase 1: In-Depth OOP Foundations
Module 02: Pillars of OOP

This module deep-dives into the four core pillars of Object-Oriented Programming,
using standard Python syntax and patterns:
1. Encapsulation: Data hiding, Protected/Private members, Name Mangling, and @property.
2. Inheritance: Code reuse, base/derived classes, and overriding.
3. Polymorphism: Method overriding, Operator overloading, and Duck Typing.
4. Abstraction: Abstract Base Classes (ABCs) and abstract methods.
"""

from abc import ABC, abstractmethod
import math

# =====================================================================
# 1. ABSTRACTION (Abstract Base Class)
# =====================================================================
class Shape(ABC):
    """
    Abstract Class representing a generic shape.
    It cannot be instantiated directly and forces subclasses to implement
    the abstract methods.
    """
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass

    def description(self) -> str:
        """Concrete method inside abstract class (reusable behavior)."""
        return f"I am a shape with an Area of {self.area():.2f} and Perimeter of {self.perimeter():.2f}"


# =====================================================================
# 2. INHERITANCE & ENCAPSULATION
# =====================================================================
class Circle(Shape):
    """A concrete Circle shape illustrating Inheritance and Encapsulation."""
    
    def __init__(self, radius: float):
        # Encapsulation: We hide the raw radius attribute using a private naming convention
        # In Python:
        # _name (Protected): Convention only, accessible but warned against.
        # __name (Private): Invokes Name Mangling. Python renames it internally to _ClassName__name.
        self.__radius = 0.0
        self.radius = radius  # Uses the setter below for validation!

    # GETTER (using @property decorator)
    @property
    def radius(self) -> float:
        """Getter for the private __radius attribute."""
        return self.__radius

    # SETTER
    @radius.setter
    def radius(self, value: float):
        """Setter for the private __radius attribute with validation (Enterprise Guard)."""
        if value <= 0:
            raise ValueError("Radius must be a positive number.")
        self.__radius = value

    # Implementing abstract methods from Shape
    def area(self) -> float:
        return math.pi * (self.__radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """A concrete Rectangle shape illustrating Encapsulation & Inheritance."""
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self._width = width    # Protected (single underscore)
        self._height = height  # Protected (single underscore)

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)


# =====================================================================
# 3. POLYMORPHISM
# =====================================================================
# Polymorphism allows different classes to respond to the same method call.
# Python implements two forms of Polymorphism:
# A) Subtype Polymorphism (Inheriting from Shape)
# B) Duck Typing ("If it walks like a duck and quacks like a duck, it's a duck")

class CustomGridObject:
    """
    This class does NOT inherit from Shape.
    However, it implements the area() method. Duck typing allows us to
    treat it interchangeably in polymorphic functions!
    """
    def area(self) -> float:
        return 50.0


def print_area_calculator(shape_object):
    """
    Polymorphic Function.
    It doesn't care about the type of shape_object; it only cares that
    the object has an area() method (Duck Typing).
    """
    print(f"Calculating area for {type(shape_object).__name__}: {shape_object.area():.2f}")


# C) Operator Overloading (Polymorphism via Magic/Dunder Methods)
class Point2D:
    """A 2D point demonstrating Operator Overloading."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self, other: "Point2D") -> "Point2D":
        if not isinstance(other, Point2D):
            return NotImplemented
        return Point2D(self.x + other.x, self.y + other.y)

    # Overloading the '==' operator
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("PILLARS OF OOP: ENCAPSULATION, INHERITANCE, POLYMORPHISM, ABSTRACTION")
    print("==========================================================\n")

    # --- 1. Abstraction & Inheritance Demo ---
    print("--- 1. Abstraction & Inheritance ---")
    try:
        # Attempting to instantiate an abstract class will fail
        s = Shape()
    except TypeError as e:
        print(f"Instantiating Shape directly failed (as expected): {e}")

    circle = Circle(5.0)
    rect = Rectangle(4.0, 6.0)
    print(circle.description())
    print(rect.description())
    print()

    # --- 2. Encapsulation & Name Mangling Demo ---
    print("--- 2. Encapsulation & Getter/Setter Safety ---")
    print(f"Circle Radius: {circle.radius}")
    try:
        circle.radius = -10  # Validation guard will raise ValueError
    except ValueError as e:
        print(f"Validation Guard caught bad assignment: {e}")

    # Accessing private variable directly:
    try:
        print(circle.__radius)
    except AttributeError as e:
        print(f"Direct access to circle.__radius failed (as expected): {e}")
        
    # Revealing Name Mangling:
    print(f"Accessing via name mangled attribute: circle._Circle__radius = {circle._Circle__radius}\n")

    # --- 3. Polymorphism & Duck Typing Demo ---
    print("--- 3. Polymorphism & Duck Typing ---")
    grid_item = CustomGridObject()
    
    print_area_calculator(circle)     # Subtype polymorphism
    print_area_calculator(rect)       # Subtype polymorphism
    print_area_calculator(grid_item)  # Duck Typing polymorphism! Works without inheriting Shape.
    print()

    # --- 4. Operator Overloading Demo ---
    print("--- 4. Operator Overloading ---")
    p1 = Point2D(2, 4)
    p2 = Point2D(5, 3)
    p3 = p1 + p2  # Uses the custom __add__ method
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p1 + p2 = {p3}")
    print(f"Is p1 == Point2D(2, 4)? {p1 == Point2D(2, 4)}")
    
    print("\n==========================================================")
    print("Module 02 completed successfully!")
    print("==========================================================")
