#!/usr/bin/env python3
"""
Phase 3: Classic Design Patterns (Creational)
Module: Singleton Pattern

The Singleton pattern ensures that a class has only one instance and provides
a global point of access to it.
In enterprise applications, singletons must be thread-safe to avoid race
conditions during initialization.

This module implements:
1. Thread-Safe Metaclass Singleton (Recommended: cleanest and reusable).
2. Thread-Safe Class Decorator Singleton.
3. __new__ Dunder Singleton with threading.Lock.
"""

import threading
import time

# =====================================================================
# METHOD 1: METACLASS SINGLETON (Highly Recommended)
# =====================================================================
# This is clean because it separates singleton mechanics from the class's logic.
# Subclasses automatically inherit the singleton property if they use this metaclass.

class SingletonMeta(type):
    """A thread-safe Metaclass implementation of Singleton."""
    _instances = {}
    _lock = threading.Lock()  # Synchronizes threads during instantiation

    def __call__(cls, *args, **kwargs):
        # Double-Checked Locking optimization
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    # Allocate and initialize the instance
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnectionPool(metaclass=SingletonMeta):
    """A mock Database Connection Pool implemented via Singleton Metaclass."""
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        print(f"[DB Pool] Initializing DatabaseConnectionPool with '{self.connection_string}'...")
        # Simulate slow initialization (helps demonstrate thread safety)
        time.sleep(0.1)

    def execute_query(self, query: str):
        print(f"[DB Pool] Executing query: '{query}' on connection: {hex(id(self))}")


# =====================================================================
# METHOD 2: CLASS DECORATOR SINGLETON
# =====================================================================
# Easy to read and apply. However, you cannot inherit easily from decorated classes.

def singleton_decorator(cls):
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton_decorator
class ApplicationConfig:
    def __init__(self):
        print("[Config] Loading application configuration file...")
        self.settings = {"port": 8080, "host": "localhost"}


# =====================================================================
# THREAD-SAFETY DEMONSTRATION RUNNER
# =====================================================================
def thread_task(thread_id: int):
    # Multiple threads will attempt to retrieve the database instance at the same time.
    # If not thread-safe, we'd see multiple initialization logs and multiple memory addresses.
    pool = DatabaseConnectionPool("postgresql://admin:password@localhost:5432/production")
    pool.execute_query(f"SELECT * FROM users LIMIT 1 (Thread {thread_id})")


if __name__ == "__main__":
    print("==========================================================")
    print("SINGLETON PATTERN: THREAD-SAFE IMPLEMENTATIONS")
    print("==========================================================\n")

    # --- 1. Testing Thread Safety of Metaclass Singleton ---
    print("--- 1. Testing Thread Safety (Concurrent Metaclass Singleton) ---")
    threads = []
    for i in range(5):
        t = threading.Thread(target=thread_task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print()

    # --- 2. Testing Decorator Singleton ---
    print("--- 2. Testing Decorator Singleton ---")
    config1 = ApplicationConfig()
    config2 = ApplicationConfig()
    print(f"config1 ID: {hex(id(config1))}")
    print(f"config2 ID: {hex(id(config2))}")
    print(f"Are both config instances identical? {config1 is config2}")
    
    print("\n==========================================================")
    print("Singleton Pattern module completed successfully!")
    print("==========================================================")
