#!/usr/bin/env python3
"""
Phase 1: In-Depth OOP Foundations
Module 04: Magic (Dunder) Methods & Protocols

Dunder (Double Underscore) methods allow Python objects to hook into native
operators and built-in Python behaviors (e.g., len(), print(), index iteration, 
with statement).
In this module, we explore:
1. Object Lifecycle: `__new__` (allocator) vs `__init__` (initializer).
2. String formatting and representation: `__str__` vs `__repr__`.
3. Making objects callable like functions: `__call__`.
4. Emulating sequence/container types: `__len__`, `__getitem__`, `__setitem__`.
5. Context Manager Protocol: resource management with `__enter__` and `__exit__`.
"""

import time

# =====================================================================
# 1. THE LIFECYCLE: __new__ VS __init__
# =====================================================================
# `__new__` is the actual constructor. It is a static method that allocates
# the memory and returns the instance.
# `__init__` is the initializer that configures the instance attributes.
# Understanding __new__ is crucial for Singletons or customizing immutable classes.

class UpperCaseString(str):
    """A custom string type that is always uppercase, using __new__."""
    def __new__(cls, value: str):
        # Strings are immutable in Python, so we must intercept creation in __new__.
        # Standard __init__ cannot mutate the string after it is created!
        uppercase_val = value.upper()
        return super().__new__(cls, uppercase_val)


# =====================================================================
# 2. STRINGS, CALLABLES, AND CONTAINER EMULATION
# =====================================================================
class EnterpriseResourceRegistry:
    """
    An enterprise container representing active servers in a cluster.
    Illustrates __repr__, __str__, __call__, and Sequence Dunder Protocols.
    """
    def __init__(self, cluster_name: str):
        self.cluster_name = cluster_name
        self._servers = []  # List of server addresses

    # String representation for developers (debugging)
    def __repr__(self) -> str:
        return f"EnterpriseResourceRegistry(cluster_name='{self.cluster_name}', servers={self._servers})"

    # String representation for users/logging
    def __str__(self) -> str:
        return f"Cluster '{self.cluster_name}' manages {len(self._servers)} active server(s)."

    # Makes the class instance callable like a function: registry()
    def __call__(self, new_server: str):
        """Register a new server address directly by calling the object."""
        if new_server not in self._servers:
            self._servers.append(new_server)
            print(f"[Registry] Registered {new_server}")

    # Container protocols:
    def __len__(self) -> int:
        return len(self._servers)

    def __getitem__(self, index: int) -> str:
        return self._servers[index]

    def __setitem__(self, index: int, value: str):
        self._servers[index] = value


# =====================================================================
# 3. CONTEXT MANAGER PROTOCOL
# =====================================================================
# Using `with` ensures resources are correctly released even if exceptions occur.
# The protocol requires:
# - `__enter__`: Runs on entering block. Returns resource.
# - `__exit__`: Runs on exiting block. Receives exception details if one occurred.

class TimerTracker:
    """A context manager to measure the execution time of code blocks."""
    def __init__(self, operation_name: str):
        self.operation_name = operation_name
        self.start_time = 0.0

    def __enter__(self):
        print(f"[Timer] Starting timer for: {self.operation_name}")
        self.start_time = time.perf_counter()
        return self  # Can return self or another object to be captured by `as`

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.perf_counter()
        duration = end_time - self.start_time
        print(f"[Timer] Finished: '{self.operation_name}' took {duration:.6f} seconds.")
        
        # Exception handling check:
        if exc_type is not None:
            print(f"[Timer] Warning: Exception occurred in block: {exc_val}")
            # If we return True, the exception is suppressed.
            # If we return False (or None), the exception is propagated.
            return False 
        return True


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("MAGIC METHODS & PROTOCOLS: LIFE CYCLE, CONTEXT MANAGERS")
    print("==========================================================\n")

    # --- 1. Custom string creation via __new__ ---
    print("--- 1. Immutable Object Customization (__new__) ---")
    custom_str = UpperCaseString("hello world")
    print(f"custom_str (always uppercase): {custom_str}")
    print(f"Is custom_str an instance of str? {isinstance(custom_str, str)}\n")

    # --- 2. Registry Class (Container & Callable Dunders) ---
    print("--- 2. Container & Callable Dunder Protocols ---")
    registry = EnterpriseResourceRegistry("US-East-Production")
    
    # Trigger __call__
    registry("10.0.0.1")
    registry("10.0.0.2")
    registry("10.0.0.3")
    
    # Trigger __repr__ and __str__
    print(f"\nDeveloper Repr: {repr(registry)}")
    print(f"User Str:       {registry}")
    
    # Trigger __len__
    print(f"Number of servers: {len(registry)}")
    
    # Trigger __getitem__ (indexing and slicing support)
    print(f"First server in registry:  {registry[0]}")
    
    # Trigger __setitem__
    registry[1] = "10.0.0.99"
    print(f"Updated server index 1:    {registry[1]}")
    
    # Loop over registry (relies on __getitem__ or __iter__)
    print("Listing all servers:")
    for server in registry:
        print(f" - {server}")
    print()

    # --- 3. Context Managers ---
    print("--- 3. Context Manager Protocol ---")
    # Using the TimerTracker
    with TimerTracker("Database Sync Simulation") as timer:
        print("Executing heavy work...")
        time.sleep(0.5)
        print("Sync complete.")
    print()

    # Demonstrating Exception Propagation inside Context Manager
    print("Context Manager with Exception:")
    try:
        with TimerTracker("Unstable Server Run"):
            print("Processing data...")
            raise RuntimeError("Database connection timed out!")
    except RuntimeError as e:
        print(f"Main loop caught propagated exception: {e}")

    print("\n==========================================================")
    print("Module 04 completed successfully!")
    print("==========================================================")
