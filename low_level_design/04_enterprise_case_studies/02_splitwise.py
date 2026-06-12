#!/usr/bin/env python3
"""
Phase 4: Enterprise Case Studies
Module 02: Splitwise (Expense Sharing & Debt Settlement)

This module implements a complete, enterprise-grade Low-Level Design (LLD) for a 
Splitwise-like expense sharing system.

Key features:
1. User and Group entities.
2. Multiple splitting options: Equal splits, Exact splits, and Percentage splits.
3. Split validation guards (e.g., percentages sum to 100%, exact shares sum to total).
4. GREEDY DEBT SIMPLIFICATION ALGORITHM (Minimizing final transaction count).
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Tuple
import heapq

# =====================================================================
# USER & SPLIT STRUCTS
# =====================================================================
class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"User({self.name})"


class Split(ABC):
    """Abstract base class representing a share of an expense."""
    def __init__(self, user: User, amount: float = 0.0):
        self.user = user
        self.amount = amount  # Calculated share of the expense


class EqualSplit(Split):
    pass


class ExactSplit(Split):
    def __init__(self, user: User, amount: float):
        super().__init__(user, amount)


class PercentageSplit(Split):
    def __init__(self, user: User, percent: float):
        super().__init__(user)
        self.percent = percent


# =====================================================================
# EXPENSE VALIDATORS & BUILDERS (Strategy Pattern)
# =====================================================================
class ExpenseMetadata:
    def __init__(self, description: str):
        self.description = description


class Expense(ABC):
    """Base abstract class for an expense."""
    def __init__(self, paid_by: User, amount: float, splits: List[Split], metadata: ExpenseMetadata):
        self.paid_by = paid_by
        self.amount = amount
        self.splits = splits
        self.metadata = metadata

    @abstractmethod
    def validate(self) -> bool:
        pass


class EqualExpense(Expense):
    def validate(self) -> bool:
        # For equal expense, validation is simple
        return True


class ExactExpense(Expense):
    def validate(self) -> bool:
        # Sum of splits must match total amount
        total_split = sum(split.amount for split in self.splits)
        return abs(total_split - self.amount) < 0.01


class PercentageExpense(Expense):
    def validate(self) -> bool:
        # Sum of percentages must equal 100%
        total_percent = sum(split.percent for split in self.splits)
        return abs(total_percent - 100.0) < 0.01


# =====================================================================
# EXPENSE SERVICE (Calculates and executes transactions)
# =====================================================================
class ExpenseService:
    @staticmethod
    def create_expense(paid_by: User, amount: float, splits: List[Split], description: str) -> Expense:
        metadata = ExpenseMetadata(description)
        
        # Determine expense type based on splits provided
        first_split = splits[0]
        if isinstance(first_split, EqualSplit):
            # Calculate equal distribution
            split_amount = round(amount / len(splits), 2)
            for split in splits:
                split.amount = split_amount
            # Handle rounding adjustments (inject penny difference to first user)
            total_calc = split_amount * len(splits)
            diff = amount - total_calc
            if abs(diff) > 0.001:
                splits[0].amount += round(diff, 2)
                
            expense = EqualExpense(paid_by, amount, splits, metadata)
        
        elif isinstance(first_split, ExactSplit):
            expense = ExactExpense(paid_by, amount, splits, metadata)
            
        elif isinstance(first_split, PercentageSplit):
            # Calculate amount from percentage
            for split in splits:
                split.amount = round((split.percent * amount) / 100.0, 2)
            expense = PercentageExpense(paid_by, amount, splits, metadata)
            
        else:
            raise ValueError("Unsupported split type.")

        if not expense.validate():
            raise ValueError(f"Validation failed for expense: '{description}'")

        return expense


# =====================================================================
# DEBT SETTLEMENT SERVICE (Greedy Simplify Debts)
# =====================================================================
class DebtSettlementService:
    """
    Implements transaction minimization algorithm.
    Uses a greedy approach to match the person who owes the most (Debtor)
    with the person who is owed the most (Creditor).
    """
    @staticmethod
    def simplify_debts(balances: Dict[str, float], users: Dict[str, User]) -> List[Tuple[User, User, float]]:
        # balances map: user_id -> net_balance
        # A positive balance means they are owed money (Creditor).
        # A negative balance means they owe money (Debtor).
        
        debtors = []   # Min heap for debtors (we store positive value of debt)
        creditors = [] # Max heap for creditors (we store negative value for min-heap emulation)

        for u_id, balance in balances.items():
            if balance < -0.01:
                # We store (debt_amount, user_id)
                heapq.heappush(debtors, (-balance, u_id))
            elif balance > 0.01:
                # We store (-credit_amount, user_id) to simulate max heap
                heapq.heappush(creditors, (-balance, u_id))

        transactions = []

        while debtors and creditors:
            debt_amount, debtor_id = heapq.heappop(debtors)
            credit_amount, creditor_id = heapq.heappop(creditors)
            credit_amount = -credit_amount  # Convert back to positive

            # Settle minimum of debtor debt vs creditor credit
            settled_val = min(debt_amount, credit_amount)
            debtor_user = users[debtor_id]
            creditor_user = users[creditor_id]

            transactions.append((debtor_user, creditor_user, round(settled_val, 2)))

            # Update remaining balances
            remaining_debt = debt_amount - settled_val
            remaining_credit = credit_amount - settled_val

            if remaining_debt > 0.01:
                heapq.heappush(debtors, (remaining_debt, debtor_id))
            if remaining_credit > 0.01:
                heapq.heappush(creditors, (-remaining_credit, creditor_id))

        return transactions


# =====================================================================
# GROUP MANAGEMENT
# =====================================================================
class Group:
    """A collection of users sharing expenses."""
    def __init__(self, group_id: str, name: str):
        self.group_id = group_id
        self.name = name
        self.users: Dict[str, User] = {}
        self.expenses: List[Expense] = []
        self.balances: Dict[str, float] = {}  # net balance per user_id

    def add_user(self, user: User):
        self.users[user.user_id] = user
        self.balances[user.user_id] = 0.0

    def add_expense(self, paid_by: User, amount: float, splits: List[Split], description: str):
        # 1. Create and validate expense
        expense = ExpenseService.create_expense(paid_by, amount, splits, description)
        self.expenses.append(expense)

        # 2. Update running balances:
        # The person who paid gets a credit of the full amount
        self.balances[paid_by.user_id] += amount
        # Everyone in the split gets a debt of their individual share
        for split in splits:
            self.balances[split.user.user_id] -= split.amount

        print(f"[Group '{self.name}'] Added expense: '{description}' of ${amount:.2f} paid by {paid_by.name}")

    def show_balances(self):
        print(f"\n--- Running Net Balances for Group '{self.name}' ---")
        for u_id, bal in self.balances.items():
            user = self.users[u_id]
            status = "is owed" if bal > 0 else "owes"
            print(f"  {user.name:8} {status:8} ${abs(bal):.2f}")

    def get_simplified_transactions(self) -> List[Tuple[User, User, float]]:
        """Invokes the settlement algorithm to return minimal payment steps."""
        return DebtSettlementService.simplify_debts(self.balances, self.users)


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("ENTERPRISE LOW LEVEL DESIGN: SPLITWISE DEBT SIMPLIFICATION")
    print("==========================================================\n")

    # 1. Setup Users
    u1 = User("u1", "Alice", "alice@test.com")
    u2 = User("u2", "Bob", "bob@test.com")
    u3 = User("u3", "Charlie", "charlie@test.com")
    u4 = User("u4", "David", "david@test.com")

    # 2. Create Group
    trip = Group("g1", "EuroTrip 2026")
    trip.add_user(u1)
    trip.add_user(u2)
    trip.add_user(u3)
    trip.add_user(u4)

    # 3. Add Expenses
    # Expense 1: Alice paid $100. Split EQUALLY among all 4 members
    splits1 = [EqualSplit(u1), EqualSplit(u2), EqualSplit(u3), EqualSplit(u4)]
    trip.add_expense(paid_by=u1, amount=100.0, splits=splits1, description="Cabin Rent")

    # Expense 2: Bob paid $50. Split EXACTLY: Charlie shares $30, Bob shares $20
    splits2 = [ExactSplit(u3, 30.0), ExactSplit(u2, 20.0)]
    trip.add_expense(paid_by=u2, amount=50.0, splits=splits2, description="Groceries")

    # Expense 3: Charlie paid $120. Split PERCENTAGE: Alice 50%, David 50%
    splits3 = [PercentageSplit(u1, 50.0), PercentageSplit(u4, 50.0)]
    trip.add_expense(paid_by=u3, amount=120.0, splits=splits3, description="Dinner Outing")
    
    # Show running balances
    trip.show_balances()

    # 4. Settle Balances
    print(f"\n--- Settle Transactions (Simplified Steps) ---")
    transactions = trip.get_simplified_transactions()
    if not transactions:
        print("All balances are clear.")
    else:
        for debtor, creditor, amount in transactions:
            print(f"  [Transaction] {debtor.name:8} must pay {creditor.name:8} => ${amount:.2f}")

    print("\n==========================================================")
    print("Splitwise Case Study completed successfully!")
    print("==========================================================")
