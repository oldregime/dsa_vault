#!/usr/bin/env python3
"""
Phase 2: LLD Design Principles
Module 01: SOLID Principles

This module provides clear, enterprise-grade demonstrations of the SOLID principles.
For each principle, we show:
1. The VIOLATION (bad design that is hard to extend and test).
2. The SOLUTION (good clean architecture design).
"""

from abc import ABC, abstractmethod

# =====================================================================
# 1. SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# =====================================================================
# "A class should have only one reason to change."

# --- VIOLATION ---
class BadInvoice:
    def __init__(self, amount: float):
        self.amount = amount

    def calculate_tax(self) -> float:
        return self.amount * 0.18

    def generate_html_invoice(self) -> str:
        return f"<html><body><h1>Invoice: ${self.amount}</h1></body></html>"

    def save_to_database(self):
        print(f"Saving invoice of ${self.amount} to PostgreSQL database...")


# --- SOLUTION ---
# We split the responsibilities into distinct classes:
class Invoice:
    """Class representing only Invoice Data."""
    def __init__(self, amount: float):
        self.amount = amount

    def calculate_tax(self) -> float:
        return self.amount * 0.18


class InvoiceFormatter:
    """Class responsible only for formatting representation."""
    def format_to_html(self, invoice: Invoice) -> str:
        return f"<html><body><h1>Invoice: ${invoice.amount}</h1></body></html>"


class InvoiceRepository:
    """Class responsible only for database operations."""
    def save(self, invoice: Invoice):
        print(f"[SRP Solution] Saving invoice of ${invoice.amount} to database.")


# =====================================================================
# 2. OPEN/CLOSED PRINCIPLE (OCP)
# =====================================================================
# "Software entities should be open for extension, but closed for modification."

# --- VIOLATION ---
class BadDiscountCalculator:
    def calculate_discount(self, amount: float, customer_type: str) -> float:
        # If we want to add a new customer type (e.g., Elite), we MUST modify this class!
        if customer_type == "Regular":
            return amount * 0.05
        elif customer_type == "VIP":
            return amount * 0.20
        return 0.0


# --- SOLUTION ---
# We use Abstraction and Polymorphism. To add new discounts, we write new classes
# without modifying the calculator. (Strategy Pattern)
class DiscountStrategy(ABC):
    @abstractmethod
    def get_discount(self, amount: float) -> float:
        pass

class RegularDiscount(DiscountStrategy):
    def get_discount(self, amount: float) -> float:
        return amount * 0.05

class VIPDiscount(DiscountStrategy):
    def get_discount(self, amount: float) -> float:
        return amount * 0.20

class EliteDiscount(DiscountStrategy):
    """Added EliteDiscount later without touching existing classes!"""
    def get_discount(self, amount: float) -> float:
        return amount * 0.35

class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate(self, amount: float) -> float:
        return self.strategy.get_discount(amount)


# =====================================================================
# 3. LISKOV SUBSTITUTION PRINCIPLE (LSP)
# =====================================================================
# "Subclasses should be substitutable for their base classes without altering program correctness."

# --- VIOLATION ---
class BadBird:
    def fly(self):
        return "Flying high"

class BadOstrich(BadBird):
    def fly(self):
        # Violation: An ostrich is a bird, but it CANNOT fly!
        # Throwing an exception breaks client code expecting all birds to fly.
        raise NotImplementedError("Ostriches cannot fly!")


# --- SOLUTION ---
# Re-architect the hierarchy. Not all birds fly, so flying is a separate capability.
class Bird(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass

class FlyingBird(Bird, ABC):
    @abstractmethod
    def fly(self) -> str:
        pass

class Eagle(FlyingBird):
    def eat(self) -> str:
        return "Eagle eating prey"
    def fly(self) -> str:
        return "Eagle flying high"

class Ostrich(Bird):
    def eat(self) -> str:
        return "Ostrich eating seeds"


# =====================================================================
# 4. INTERFACE SEGREGATION PRINCIPLE (ISP)
# =====================================================================
# "Clients should not be forced to depend on interfaces they do not use."

# --- VIOLATION ---
class BadMultiFunctionDevice(ABC):
    @abstractmethod
    def print_doc(self): pass
    @abstractmethod
    def scan_doc(self): pass
    @abstractmethod
    def fax_doc(self): pass

class BadSimplePrinter(BadMultiFunctionDevice):
    def print_doc(self):
        print("Printing...")
    def scan_doc(self):
        raise NotImplementedError("Simple printer cannot scan.")
    def fax_doc(self):
        raise NotImplementedError("Simple printer cannot fax.")


# --- SOLUTION ---
# Split the bloated interface into focused, segregated interfaces.
class Printer(ABC):
    @abstractmethod
    def print_doc(self): pass

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self): pass

class FaxMachine(ABC):
    @abstractmethod
    def fax_doc(self): pass

class SimplePrinter(Printer):
    def print_doc(self):
        print("[ISP Solution] SimplePrinter is printing doc.")

class OfficeWorkspaceCopier(Printer, Scanner):
    """Can implement multiple interfaces cleanly!"""
    def print_doc(self):
        print("[ISP Solution] OfficeCopier is printing.")
    def scan_doc(self):
        print("[ISP Solution] OfficeCopier is scanning.")


# =====================================================================
# 5. DEPENDENCY INVERSION PRINCIPLE (DIP)
# =====================================================================
# "High-level modules should not depend on low-level modules. Both should depend on abstractions."

# --- VIOLATION ---
class EmailClient:
    def send_email(self, msg: str):
        print(f"Sending email: {msg}")

class BadNotificationService:
    def __init__(self):
        # Violation: NotificationService is tightly coupled to EmailClient.
        # If we want to support SMS or WhatsApp, we must rewrite this class.
        self.email_client = EmailClient()

    def send(self, message: str):
        self.email_client.send_email(message)


# --- SOLUTION ---
# High-level module depends on an abstraction (MessageSender).
class MessageSender(ABC):
    @abstractmethod
    def send_message(self, message: str):
        pass

class EmailSender(MessageSender):
    def send_message(self, message: str):
        print(f"[DIP Solution] Email: {message}")

class SMSSender(MessageSender):
    def send_message(self, message: str):
        print(f"[DIP Solution] SMS: {message}")

class NotificationService:
    """High-level class depending on MessageSender abstraction (Dependency Injection)."""
    def __init__(self, sender: MessageSender):
        self.sender = sender  # Inject the dependency

    def send(self, message: str):
        self.sender.send_message(message)


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("SOLID DESIGN PRINCIPLES DEMONSTRATION")
    print("==========================================================\n")

    # --- 1. SRP Demo ---
    print("--- 1. Single Responsibility Principle ---")
    inv = Invoice(100.0)
    repo = InvoiceRepository()
    repo.save(inv)
    print()

    # --- 2. OCP Demo ---
    print("--- 2. Open/Closed Principle ---")
    vip_calc = DiscountCalculator(VIPDiscount())
    elite_calc = DiscountCalculator(EliteDiscount())
    print(f"VIP Discount on $1000:   ${vip_calc.calculate(1000.0):.2f}")
    print(f"Elite Discount on $1000: ${elite_calc.calculate(1000.0):.2f}")
    print()

    # --- 3. LSP Demo ---
    print("--- 3. Liskov Substitution Principle ---")
    # Polymorphic bird walker function
    def make_bird_eat(bird: Bird):
        print(f"{type(bird).__name__} says: {bird.eat()}")
        
    make_bird_eat(Eagle())
    make_bird_eat(Ostrich())
    # Ostrich can be substituted for Bird safely without unexpected exceptions!
    print()

    # --- 4. ISP Demo ---
    print("--- 4. Interface Segregation Principle ---")
    printer = SimplePrinter()
    printer.print_doc()
    office_device = OfficeWorkspaceCopier()
    office_device.print_doc()
    office_device.scan_doc()
    print()

    # --- 5. DIP Demo ---
    print("--- 5. Dependency Inversion Principle ---")
    # We can inject any message sender abstraction easily
    email_notifier = NotificationService(EmailSender())
    sms_notifier = NotificationService(SMSSender())
    
    email_notifier.send("Server online.")
    sms_notifier.send("CPU usage exceeds 90%!")
    
    print("\n==========================================================")
    print("SOLID Principles module completed successfully!")
    print("==========================================================")
