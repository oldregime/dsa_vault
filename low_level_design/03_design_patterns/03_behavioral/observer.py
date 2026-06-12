#!/usr/bin/env python3
"""
Phase 3: Classic Design Patterns (Behavioral)
Module: Observer Pattern

The Observer pattern defines a one-to-many dependency between objects so that
when one object (the Subject/Publisher) changes state, all its dependents
(Observers/Subscribers) are notified and updated automatically.

Example:
A Stock Market Ticker (Subject) notifies multiple client dashboards and automated
trading bots (Observers) whenever a stock price fluctuates.
"""

from abc import ABC, abstractmethod
from typing import List

# =====================================================================
# OBSERVER INTERFACE
# =====================================================================
class Observer(ABC):
    @abstractmethod
    def update(self, symbol: str, price: float):
        pass


# =====================================================================
# SUBJECT INTERFACE
# =====================================================================
class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, symbol: str, price: float):
        for observer in self._observers:
            observer.update(symbol, price)


# =====================================================================
# CONCRETE SUBJECT
# =====================================================================
class StockMarketTicker(Subject):
    """The concrete subject maintaining prices and notifying on change."""
    def __init__(self):
        super().__init__()
        self._prices = {}

    def set_price(self, symbol: str, price: float):
        self._prices[symbol] = price
        # Notify subscribers
        self.notify_observers(symbol, price)


# =====================================================================
# CONCRETE OBSERVERS
# =====================================================================
class MobileAppDashboard(Observer):
    def __init__(self, username: str):
        self.username = username

    def update(self, symbol: str, price: float):
        print(f"[Mobile App - {self.username}] Notification: {symbol} is now ${price:.2f}")


class TradingBot(Observer):
    def __init__(self, target_price: float):
        self.target_price = target_price

    def update(self, symbol: str, price: float):
        if price < self.target_price:
            print(f"[Trading Bot] BUY ORDER PLACED: {symbol} is ${price:.2f} (Target was < ${self.target_price:.2f})")


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("OBSERVER DESIGN PATTERN (PUBLISH-SUBSCRIBE)")
    print("==========================================================\n")

    # Setup the stock market publisher
    nasdaq = StockMarketTicker()

    # Setup observers
    user1_app = MobileAppDashboard("Alice")
    user2_app = MobileAppDashboard("Bob")
    bot = TradingBot(target_price=150.00)

    # Register/Attach observers
    print("Attaching subscribers...")
    nasdaq.attach(user1_app)
    nasdaq.attach(user2_app)
    nasdaq.attach(bot)
    print()

    # Change prices (triggers notifications)
    print("Updating AAPL price to $155.00...")
    nasdaq.set_price("AAPL", 155.00)
    print()

    # Change price to trigger Trading Bot action
    print("Updating AAPL price to $145.00...")
    nasdaq.set_price("AAPL", 145.00)
    print()

    # Detach one observer (Bob uninstalled the mobile app)
    print("Detaching Bob's Mobile app...")
    nasdaq.detach(user2_app)
    print()

    # Change prices again
    print("Updating AAPL price to $142.00...")
    nasdaq.set_price("AAPL", 142.00)

    print("\n==========================================================")
    print("Observer Pattern completed successfully!")
    print("==========================================================")
