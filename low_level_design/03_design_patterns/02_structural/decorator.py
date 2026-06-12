#!/usr/bin/env python3
"""
Phase 3: Classic Design Patterns (Structural)
Module: Decorator Pattern

The Decorator pattern dynamically attaches additional responsibilities to an
object. Decorators provide a flexible alternative to subclassing for extending functionality.

Important Note: This is the Classic OOP Decorator design pattern (wrapper objects),
not Python's native `@decorator` syntax (metaprogramming).

Example:
A Base Coffee Beverage that can be decorated with ingredients (Milk, Sugar, Caramel)
at runtime. Cost and description accumulate dynamically.
"""

from abc import ABC, abstractmethod

# =====================================================================
# BASE COMPONENT
# =====================================================================
class Beverage(ABC):
    """The interface that defines what behaviors can be decorated."""
    @abstractmethod
    def get_description(self) -> str: pass

    @abstractmethod
    def get_cost(self) -> float: pass


# =====================================================================
# CONCRETE COMPONENT
# =====================================================================
class Espresso(Beverage):
    """The base item that we will decorate."""
    def get_description(self) -> str:
        return "Espresso"

    def get_cost(self) -> float:
        return 2.50


# =====================================================================
# BASE DECORATOR
# =====================================================================
class BeverageDecorator(Beverage, ABC):
    """
    The decorator maintains a reference to a Component object and defines
    an interface that conforms to Component's interface.
    """
    def __init__(self, beverage: Beverage):
        self._wrapped_beverage = beverage

    def get_description(self) -> str:
        return self._wrapped_beverage.get_description()

    def get_cost(self) -> float:
        return self._wrapped_beverage.get_cost()


# =====================================================================
# CONCRETE DECORATORS
# =====================================================================
class Milk(BeverageDecorator):
    def get_description(self) -> str:
        return f"{super().get_description()}, Milk"

    def get_cost(self) -> float:
        return super().get_cost() + 0.50


class Sugar(BeverageDecorator):
    def get_description(self) -> str:
        return f"{super().get_description()}, Sugar"

    def get_cost(self) -> float:
        return super().get_cost() + 0.20


class Caramel(BeverageDecorator):
    def get_description(self) -> str:
        return f"{super().get_description()}, Caramel Drizzle"

    def get_cost(self) -> float:
        return super().get_cost() + 0.80


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("DECORATOR DESIGN PATTERN")
    print("==========================================================\n")

    # Start with a plain Espresso
    my_coffee = Espresso()
    print(f"Base Order:      {my_coffee.get_description()} -> ${my_coffee.get_cost():.2f}")

    # Decorate it with Milk
    my_coffee = Milk(my_coffee)
    print(f"Add Milk:        {my_coffee.get_description()} -> ${my_coffee.get_cost():.2f}")

    # Decorate it with Sugar
    my_coffee = Sugar(my_coffee)
    print(f"Add Sugar:       {my_coffee.get_description()} -> ${my_coffee.get_cost():.2f}")

    # Decorate it with Caramel
    my_coffee = Caramel(my_coffee)
    print(f"Add Caramel:     {my_coffee.get_description()} -> ${my_coffee.get_cost():.2f}")

    print("\n==========================================================")
    print("Decorator Pattern completed successfully!")
    print("==========================================================")
