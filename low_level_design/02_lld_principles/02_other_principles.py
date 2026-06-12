#!/usr/bin/env python3
"""
Phase 2: LLD Design Principles
Module 02: DRY, KISS, YAGNI & Law of Demeter

This module covers other key software engineering principles:
1. DRY (Don't Repeat Yourself): Consolidating duplicate logic.
2. KISS (Keep It Simple, Stupid): Avoiding over-engineering.
3. YAGNI (You Aren't Gonna Need It): Avoiding pre-emptive feature implementation.
4. Law of Demeter (Principle of Least Knowledge): Restricting object traversal.
"""

# =====================================================================
# 1. LAW OF DEMETER (LoD)
# =====================================================================
# "Only talk to your immediate friends; don't talk to strangers."
# A method of an object should only call methods on:
# - The object itself.
# - Objects passed as parameters.
# - Objects created/instantiated within the method.
# - Direct component objects (immediate attributes).
# Avoid "train wreck" calls: object.get_a().get_b().get_c().do_something()

# --- VIOLATION (Train Wreck) ---
class Wallet:
    def __init__(self, balance: float):
        self.balance = balance

class Customer:
    def __init__(self, wallet: Wallet):
        self.wallet = wallet

class PaperBoy:
    def collect_payment(self, customer: Customer, charge: float):
        # Violation: PaperBoy reaches deep into Customer to access Wallet, and then modifies balance!
        # PaperBoy depends on the internal structure of Customer and Wallet. If Wallet changes, PaperBoy breaks!
        if customer.wallet.balance >= charge:
            customer.wallet.balance -= charge
            print(f"[LoD Violation] Charged customer ${charge}. Wallet remaining: ${customer.wallet.balance}")


# --- SOLUTION ---
# We delegate the behavior. Customer manages their own wallet payment.
class GoodWallet:
    def __init__(self, balance: float):
        self._balance = balance

    def withdraw(self, amount: float) -> bool:
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    @property
    def balance(self) -> float:
        return self._balance


class GoodCustomer:
    def __init__(self, wallet: GoodWallet):
        self._wallet = wallet

    def pay(self, amount: float) -> bool:
        # Customer manages their wallet
        return self._wallet.withdraw(amount)

    def get_wallet_balance(self) -> float:
        # Exposes only what is necessary
        return self._wallet.balance


class GoodPaperBoy:
    def collect_payment(self, customer: GoodCustomer, charge: float):
        # Solution: PaperBoy talks only to immediate friend (Customer) and calls pay()
        if customer.pay(charge):
            print(f"[LoD Solution] Charged customer ${charge}. Wallet remaining: ${customer.get_wallet_balance()}")
        else:
            print("[LoD Solution] Customer does not have enough money.")


# =====================================================================
# 2. DRY, KISS & YAGNI CONCEPT SHOWCASE
# =====================================================================

# --- DRY (Don't Repeat Yourself) ---
# Bad: Writing identical validation checks in user registration, user update, and password reset.
# Good: Creating a single validation function or descriptor.

# --- YAGNI (You Aren't Gonna Need It) ---
# Bad: Building a complex, multi-region distributed caching cluster with Redis Sentinel for an app
# that currently has only 10 active local users.
# Good: Start with local memory storage (like a python dict). Wrap it behind an abstract interface,
# so you can plug in Redis later *when actually needed*. (KISS + YAGNI)

class SimpleCache:
    """KISS and YAGNI conforming cache. Simple dictionary-based storage."""
    def __init__(self):
        self._storage = {}

    def get(self, key: str):
        return self._storage.get(key)

    def set(self, key: str, value: str):
        self._storage[key] = value


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("KISS, YAGNI, DRY & LAW OF DEMETER DEMONSTRATION")
    print("==========================================================\n")

    # --- Law of Demeter Demo ---
    print("--- Law of Demeter: Violation vs Solution ---")
    
    # Violation Run
    bad_wallet = Wallet(50.0)
    bad_cust = Customer(bad_wallet)
    paperboy = PaperBoy()
    paperboy.collect_payment(bad_cust, 15.0)
    
    # Solution Run
    good_wallet = GoodWallet(50.0)
    good_cust = GoodCustomer(good_wallet)
    good_paperboy = GoodPaperBoy()
    good_paperboy.collect_payment(good_cust, 15.0)
    
    print("\n==========================================================")
    print("KISS, YAGNI, DRY & LoD module completed successfully!")
    print("==========================================================")
