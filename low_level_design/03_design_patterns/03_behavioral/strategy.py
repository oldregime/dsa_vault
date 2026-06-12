#!/usr/bin/env python3
"""
Phase 3: Classic Design Patterns (Behavioral)
Module: Strategy Pattern

The Strategy pattern defines a family of algorithms, encapsulates each one,
and makes them interchangeable at runtime. It allows the algorithm to vary 
independently of the client that uses it.

Example:
An e-commerce Checkout System that supports multiple payment processing
strategies (Credit Card, PayPal, Crypto) without hardcoding conditional branching.
"""

from abc import ABC, abstractmethod

# =====================================================================
# STRATEGY INTERFACE
# =====================================================================
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


# =====================================================================
# CONCRETE STRATEGIES
# =====================================================================
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount: float) -> str:
        # Mask card number for security logs
        masked_card = f"XXXX-XXXX-XXXX-{self.card_number[-4:]}"
        return f"Processing ${amount:.2f} payment via Credit Card: {masked_card}"


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> str:
        return f"Processing ${amount:.2f} payment via PayPal Account: {self.email}"


class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> str:
        return f"Processing ${amount:.2f} payment via Bitcoin Wallet: {self.wallet_address[:8]}..."


# =====================================================================
# THE CLIENT CONTEXT
# =====================================================================
class ShoppingCart:
    """The context class that interacts with the interchangeable strategy."""
    def __init__(self):
        self._items = []

    def add_item(self, item_name: str, price: float):
        self._items.append((item_name, price))

    def get_total(self) -> float:
        return sum(price for item, price in self._items)

    def checkout(self, payment_method: PaymentStrategy) -> str:
        """Executes checkout using the injected strategy."""
        total = self.get_total()
        if total == 0:
            return "Cart is empty. Nothing to pay."
        
        # Delegate payment execution to the strategy
        result = payment_method.pay(total)
        self._items.clear()  # Clear cart after payment
        return result


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("STRATEGY DESIGN PATTERN")
    print("==========================================================\n")

    # Set up cart
    cart = ShoppingCart()
    cart.add_item("MacBook Pro M3", 1999.99)
    cart.add_item("USB-C Hub", 49.99)
    print(f"Items added to cart. Total: ${cart.get_total():.2f}\n")

    # Checkout using Credit Card Strategy
    print("Paying with Credit Card:")
    cc_strategy = CreditCardPayment("4111222233334444", "123")
    receipt1 = cart.checkout(cc_strategy)
    print(f"Receipt: {receipt1}\n")

    # Fill cart again
    cart.add_item("Mechanical Keyboard", 120.00)
    print(f"Items added to cart. Total: ${cart.get_total():.2f}\n")

    # Checkout using PayPal Strategy
    print("Paying with PayPal:")
    paypal_strategy = PayPalPayment("customer@enterprise.com")
    receipt2 = cart.checkout(paypal_strategy)
    print(f"Receipt: {receipt2}\n")

    # Fill cart again
    cart.add_item("Ergonomic Chair", 350.00)
    
    # Checkout using Crypto Strategy
    print("Paying with Crypto:")
    crypto_strategy = CryptoPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    receipt3 = cart.checkout(crypto_strategy)
    print(f"Receipt: {receipt3}")

    print("\n==========================================================")
    print("Strategy Pattern completed successfully!")
    print("==========================================================")
