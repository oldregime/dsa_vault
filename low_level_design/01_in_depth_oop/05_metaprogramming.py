#!/usr/bin/env python3
"""
Phase 1: In-Depth OOP Foundations
Module 05: Metaprogramming, Class Decorators & Metaclasses

Metaprogramming refers to the ability of code to inspect, modify, or create other
code at runtime. In Python, this is accomplished through class decorators, dynamic
class instantiation (`type()`), and metaclasses (the "classes of classes").

This module covers:
1. Class Decorators: Adding capabilities to classes non-invasively.
2. Dynamic Class Creation: Creating a class from a function using the type constructor.
3. Metaclasses: Enforcing rules, architectural guards, and automatic service registries.
"""

# =====================================================================
# 1. CLASS DECORATORS
# =====================================================================
# A class decorator is a function that takes a class object, modifies or wraps it,
# and returns the modified class. Excellent for cross-cutting concerns (logging, API injection).

def add_audit_logger(cls):
    """Class decorator that intercepts calls and prints logs for class initialization."""
    orig_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print(f"[Audit Log] Instantiating object of type '{cls.__name__}' with args={args} kwargs={kwargs}")
        orig_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls


@add_audit_logger
class UserSession:
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role


# =====================================================================
# 2. DYNAMIC CLASS CREATION
# =====================================================================
# In Python, everything is an object, including classes. The type of a class is `type`.
# We can dynamically create a class using: type(name, bases, dict)
# - name: String name of the class.
# - bases: Tuple of parent classes (inheritance).
# - dict: Dictionary containing class namespace (methods, variables).

def create_model_class(class_name: str, fields: list):
    """Factory function that dynamically builds a data-holding class."""
    
    def __init__(self, *args):
        if len(args) != len(fields):
            raise ValueError(f"Expected {len(fields)} arguments, got {len(args)}")
        for field, value in zip(fields, args):
            setattr(self, field, value)

    def __repr__(self) -> str:
        attrs = ", ".join(f"{f}={getattr(self, f)!r}" for f in fields)
        return f"{class_name}({attrs})"

    # Create the class namespace dict
    namespace = {
        "__init__": __init__,
        "__repr__": __repr__
    }

    # Dynamically build and return the class object
    return type(class_name, (object,), namespace)


# =====================================================================
# 3. METACLASSES
# =====================================================================
# Metaclasses are the blueprint for classes. Just as a class defines how an instance
# behaves, a metaclass defines how a class behaves.
# All standard classes inherit from `type`, which is Python's default metaclass.

class ArchitecturalGuardMeta(type):
    """
    A metaclass to enforce enterprise architectural rules on subclasses:
    1. Every subclass MUST have an attribute named 'API_VERSION'.
    2. Every subclass method name must use snake_case (no camelCase).
    """
    def __new__(cls, name, bases, dct):
        # We don't want to enforce rules on the base interface class itself
        if name != "BaseService":
            # 1. Enforce API_VERSION attribute existence
            if "API_VERSION" not in dct:
                raise TypeError(f"Class '{name}' must define a class variable 'API_VERSION'.")
            
            # 2. Enforce snake_case naming for methods
            for attr_name in dct:
                # If it is a function/method and not a magic method (e.g., __init__)
                if callable(dct[attr_name]) and not (attr_name.startswith("__") and attr_name.endswith("__")):
                    if any(char.isupper() for char in attr_name):
                        raise TypeError(f"Method '{attr_name}' in class '{name}' must be snake_case (no capital letters).")

        # Create and return the class object using parent type's __new__
        return super().__new__(cls, name, bases, dct)


class BaseService(metaclass=ArchitecturalGuardMeta):
    """Base API service that uses our architectural guard metaclass."""
    pass


# Success Case: BaseService subclassing
class PaymentsService(BaseService):
    API_VERSION = "v1.2"

    def process_payment(self, amount: float):
        print(f"Processing ${amount} via PaymentsService.")


# Failure Case 1: Missing API_VERSION class variable
try:
    class FailingService1(BaseService):
        def process_payment(self, amount):
            pass
except TypeError as e:
    print(f"\n[Meta Error Catch] Correctly caught missing class variable error:\n  => {e}")


# Failure Case 2: camelCase method naming rule violation
try:
    class FailingService2(BaseService):
        API_VERSION = "v2.0"
        
        def processPayment(self, amount):  # camelCase will violate the naming guard
            pass
except TypeError as e:
    print(f"[Meta Error Catch] Correctly caught camelCase method naming violation:\n  => {e}\n")


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("METAPROGRAMMING: CLASS DECORATORS, DYNAMIC CLASSES, METACLASSES")
    print("==========================================================\n")

    # --- 1. Class Decorator Demo ---
    print("--- 1. Class Decorators in Action ---")
    session = UserSession("alice_dev", "Administrator")
    print(f"Session object: username={session.username}, role={session.role}\n")

    # --- 2. Dynamic Class Creation Demo ---
    print("--- 2. Dynamic Class Creation via type() ---")
    # Dynamically build a "Client" class
    Client = create_model_class("Client", ["client_id", "email", "subscription_tier"])
    
    # Instantiate the dynamically created class
    client1 = Client("C_9872", "user@enterprise.com", "Enterprise Premium")
    print(f"Dynamically generated class type: {type(client1)}")
    print(f"Instance details: {client1}\n")

    # --- 3. Metaclasses Demo ---
    print("--- 3. Metaclass Architectural Enforcement ---")
    # Standard payments service works because it adheres to metaclass rules
    payment_service = PaymentsService()
    payment_service.process_payment(500.0)
    
    print("\n==========================================================")
    print("Module 05 completed successfully!")
    print("==========================================================")
