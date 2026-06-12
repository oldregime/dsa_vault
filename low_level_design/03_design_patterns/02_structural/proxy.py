#!/usr/bin/env python3
"""
Phase 3: Classic Design Patterns (Structural)
Module: Proxy Pattern

The Proxy pattern provides a surrogate or placeholder for another object to
control access to it. Proxies can perform lazy loading (virtual proxy), 
enforce security policies (protection proxy), or cache query results (caching proxy).

Example:
A Database Query Executor class (expensive operation). We implement a Proxy 
that adds query caching and logs performance.
"""

from abc import ABC, abstractmethod
import time

# =====================================================================
# THE SUBJECT INTERFACE
# =====================================================================
class DatabaseExecutor(ABC):
    @abstractmethod
    def execute_query(self, sql: str) -> str:
        pass


# =====================================================================
# THE REAL SUBJECT
# =====================================================================
class RealDatabaseExecutor(DatabaseExecutor):
    """The expensive database executor. Connects to disk and runs query."""
    def __init__(self):
        print("[DB Connection] Opening connection pool to database (slow)...")
        time.sleep(0.5)  # Simulate slow network handshake

    def execute_query(self, sql: str) -> str:
        print(f"[DB Engine] Running SQL on disk: '{sql}'")
        time.sleep(0.2)  # Simulate expensive database lookup
        return f"Result rows for '{sql}'"


# =====================================================================
# THE PROXY
# =====================================================================
class CachedDatabaseProxy(DatabaseExecutor):
    """
    The Caching Proxy. Intercepts calls to RealDatabaseExecutor:
    1. Delays database connection until the first query is actually run (lazy init / virtual proxy).
    2. Caches query results in local memory to avoid hitting the database twice.
    """
    def __init__(self):
        # We hold a reference to the real database executor, but do NOT instantiate it yet.
        self._real_executor = None
        self._cache = {}

    def execute_query(self, sql: str) -> str:
        print(f"\n[Proxy] Query Intercepted: '{sql}'")
        
        # 1. Lazy Initialization (Virtual Proxy)
        if self._real_executor is None:
            print("[Proxy] First request. Initializing connection to database...")
            self._real_executor = RealDatabaseExecutor()

        # 2. Caching Lookup
        if sql in self._cache:
            print(f"[Proxy] Cache HIT! Returning cached results for: '{sql}'")
            return self._cache[sql]

        # 3. Delegation (calling real subject if cache miss)
        print("[Proxy] Cache MISS. Delegating to real database...")
        start_time = time.perf_counter()
        result = self._real_executor.execute_query(sql)
        end_time = time.perf_counter()
        
        # Store in cache
        self._cache[sql] = result
        print(f"[Proxy] Execution took: {end_time - start_time:.4f}s. Saved to cache.")
        
        return result


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("PROXY DESIGN PATTERN (LAZY INIT & CACHING)")
    print("==========================================================\n")

    # Client interacts with the Proxy as if it were the Database
    db = CachedDatabaseProxy()
    
    # Run first query (connection is initialized, cache miss)
    res1 = db.execute_query("SELECT name FROM employees WHERE id = 12")
    
    # Run identical query (cache hit, instant return, no database hit)
    res2 = db.execute_query("SELECT name FROM employees WHERE id = 12")
    
    # Run different query (initialized, cache miss, database hit)
    res3 = db.execute_query("SELECT * FROM projects")

    print("\n==========================================================")
    print("Proxy Pattern completed successfully!")
    print("==========================================================")
