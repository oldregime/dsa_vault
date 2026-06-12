#!/usr/bin/env python3
"""
Phase 4: Enterprise Case Studies
Module 01: Parking Lot System Design

This module implements a complete, enterprise-grade, thread-safe Low-Level Design (LLD)
for a Parking Lot System.

Requirements implemented:
1. Support for multiple vehicle types (Motorcycle, Car, Truck).
2. Support for multiple spot types (Motorcycle, Compact, Large) and matching vehicle types.
3. Multi-floor parking lot.
4. Concurrency control: Thread-safe ticket generation and spot assignment.
5. Dynamic Spot Allocation Strategy (Nearest spot first).
6. Extensible Payment Calculation Strategy (Hourly billing).
"""

from abc import ABC, abstractmethod
from enum import Enum
import datetime
import threading
import time
from typing import List, Optional, Dict

# =====================================================================
# ENUMS
# =====================================================================
class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    TRUCK = 3


class SpotType(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3


# =====================================================================
# VEHICLE CLASS HIERARCHY
# =====================================================================
class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)

class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.CAR)

class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.TRUCK)


# =====================================================================
# PARKING SPOT HIERARCHY
# =====================================================================
class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle: Optional[Vehicle] = None
        self._lock = threading.Lock()  # Lock for thread-safety at spot level

    def is_free(self) -> bool:
        return self.vehicle is None

    def assign_vehicle(self, vehicle: Vehicle) -> bool:
        with self._lock:
            if not self.is_free():
                return False
            self.vehicle = vehicle
            return True

    def remove_vehicle(self) -> Optional[Vehicle]:
        with self._lock:
            temp = self.vehicle
            self.vehicle = None
            return temp


# =====================================================================
# PARKING FLOOR
# =====================================================================
class ParkingFloor:
    def __init__(self, floor_number: int):
        self.floor_number = floor_number
        self.spots: Dict[SpotType, List[ParkingSpot]] = {
            SpotType.MOTORCYCLE: [],
            SpotType.COMPACT: [],
            SpotType.LARGE: []
        }

    def add_spot(self, spot: ParkingSpot):
        self.spots[spot.spot_type].append(spot)

    def get_free_spots_by_type(self, spot_type: SpotType) -> List[ParkingSpot]:
        return [spot for spot in self.spots[spot_type] if spot.is_free()]


# =====================================================================
# STRATEGIES: SPOT ALLOCATION & PAYMENT
# =====================================================================
class SpotAllocationStrategy(ABC):
    @abstractmethod
    def allocate_spot(self, floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        pass


class NearestFirstStrategy(SpotAllocationStrategy):
    """Assigns the nearest free spot on the lowest floor that fits the vehicle."""
    def __init__(self):
        # Define what spot type fits each vehicle type
        self.fit_rules = {
            VehicleType.MOTORCYCLE: [SpotType.MOTORCYCLE, SpotType.COMPACT, SpotType.LARGE],
            VehicleType.CAR: [SpotType.COMPACT, SpotType.LARGE],
            VehicleType.TRUCK: [SpotType.LARGE]
        }

    def allocate_spot(self, floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        allowed_spots = self.fit_rules[vehicle.vehicle_type]
        
        # Traverse floors from lowest to highest (nearest first)
        for floor in floors:
            for spot_type in allowed_spots:
                free_spots = floor.get_free_spots_by_type(spot_type)
                if free_spots:
                    # Return the first available spot
                    return free_spots[0]
        return None


class PaymentStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, entry_time: datetime.datetime, exit_time: datetime.datetime, vehicle_type: VehicleType) -> float:
        pass


class HourlyPaymentStrategy(PaymentStrategy):
    """Calculates billing based on hourly rates specified per vehicle type."""
    def __init__(self, rates: Dict[VehicleType, float]):
        self.rates = rates

    def calculate_cost(self, entry_time: datetime.datetime, exit_time: datetime.datetime, vehicle_type: VehicleType) -> float:
        duration = exit_time - entry_time
        hours = max(1.0, duration.total_seconds() / 3600.0)
        rate = self.rates.get(vehicle_type, 5.0)
        return round(hours * rate, 2)


# =====================================================================
# TICKET
# =====================================================================
class ParkingTicket:
    def __init__(self, ticket_id: str, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.datetime.now()
        self.exit_time: Optional[datetime.datetime] = None
        self.amount_paid = 0.0
        self.is_active = True

    def close_ticket(self, amount: float):
        self.exit_time = datetime.datetime.now()
        self.amount_paid = amount
        self.is_active = False


# =====================================================================
# THE PARKING LOT SYSTEM (SINGLETON)
# =====================================================================
class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ParkingLot(metaclass=SingletonMeta):
    """Central parking lot management system."""
    def __init__(self):
        self.name = ""
        self.floors: List[ParkingFloor] = []
        self.allocation_strategy: Optional[SpotAllocationStrategy] = None
        self.payment_strategy: Optional[PaymentStrategy] = None
        self._active_tickets: Dict[str, ParkingTicket] = {}
        self._lock = threading.Lock()  # System level lock
        self._ticket_counter = 0

    def configure(self, name: str, allocation: SpotAllocationStrategy, payment: PaymentStrategy):
        self.name = name
        self.allocation_strategy = allocation
        self.payment_strategy = payment

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        """Thread-safe vehicle parking request."""
        with self._lock:
            # 1. Allocate a spot based on strategy
            spot = self.allocation_strategy.allocate_spot(self.floors, vehicle)
            if spot is None:
                print(f"[Parking Lot] Failed to park '{vehicle.license_plate}': No spots available.")
                return None

            # 2. Occupy the spot
            if spot.assign_vehicle(vehicle):
                self._ticket_counter += 1
                ticket_id = f"TKT-{self._ticket_counter:04d}"
                ticket = ParkingTicket(ticket_id, vehicle, spot)
                self._active_tickets[ticket_id] = ticket
                print(f"[Parking Lot] Parked vehicle '{vehicle.license_plate}' in Spot '{spot.spot_id}' (Floor {spot.spot_id[2]}). Ticket: {ticket_id}")
                return ticket
            
            return None

    def unpark_vehicle(self, ticket_id: str) -> Optional[float]:
        """Thread-safe vehicle exit and payment calculation."""
        with self._lock:
            if ticket_id not in self._active_tickets:
                print(f"[Parking Lot] Error: Ticket '{ticket_id}' not found.")
                return None

            ticket = self._active_tickets[ticket_id]
            spot = ticket.spot
            
            # 1. Remove vehicle from spot
            spot.remove_vehicle()
            
            # 2. Calculate payment (Simulate exit time 2 hours in the future for test purposes)
            fake_exit_time = ticket.entry_time + datetime.timedelta(hours=2.5)
            cost = self.payment_strategy.calculate_cost(ticket.entry_time, fake_exit_time, ticket.vehicle.vehicle_type)
            
            # 3. Close the ticket
            ticket.close_ticket(cost)
            del self._active_tickets[ticket_id]
            
            print(f"[Parking Lot] Exited vehicle '{ticket.vehicle.license_plate}' from Spot '{spot.spot_id}'. Bill for 2.5 hours: ${cost:.2f}")
            return cost


# =====================================================================
# CONCURRENCY TEST & EXECUTION
# =====================================================================
def simulate_gate_entry(vehicle: Vehicle):
    """Simulates a gate entry processing a vehicle parking request."""
    lot = ParkingLot()
    lot.park_vehicle(vehicle)


if __name__ == "__main__":
    print("==========================================================")
    print("ENTERPRISE LOW LEVEL DESIGN: SYSTEM PARKING LOT")
    print("==========================================================\n")

    # 1. Initialize the Parking Lot
    lot = ParkingLot()
    
    # Configure Strategies
    rates = {
        VehicleType.MOTORCYCLE: 2.0,  # $2/hr
        VehicleType.CAR: 5.0,         # $5/hr
        VehicleType.TRUCK: 10.0       # $10/hr
    }
    lot.configure(
        name="Chicago Downtown Plaza",
        allocation=NearestFirstStrategy(),
        payment=HourlyPaymentStrategy(rates)
    )

    # Add 2 Floors with spots
    for f_idx in range(1, 3):
        floor = ParkingFloor(f_idx)
        # Add motorcycle spots
        for s_idx in range(1, 3):
            floor.add_spot(ParkingSpot(f"F{f_idx}M{s_idx}", SpotType.MOTORCYCLE))
        # Add compact spots
        for s_idx in range(1, 3):
            floor.add_spot(ParkingSpot(f"F{f_idx}C{s_idx}", SpotType.COMPACT))
        # Add large spots
        for s_idx in range(1, 2):
            floor.add_spot(ParkingSpot(f"F{f_idx}L{s_idx}", SpotType.LARGE))
        lot.add_floor(floor)

    print(f"Configured Parking Lot: '{lot.name}' with 2 floors.")
    print("Each floor has: 2 Motorcycle spots, 2 Compact spots, 1 Large spot.\n")

    # --- 2. Sequential Parking Demonstration ---
    car1 = Car("CAR-9999")
    motorcycle1 = Motorcycle("MOTO-8888")
    truck1 = Truck("TRK-7777")

    ticket1 = lot.park_vehicle(car1)          # Should go to Floor 1 Compact
    ticket2 = lot.park_vehicle(motorcycle1)   # Should go to Floor 1 Motorcycle
    ticket3 = lot.park_vehicle(truck1)        # Should go to Floor 1 Large
    print()

    # --- 3. Exit and Payment Demo ---
    lot.unpark_vehicle(ticket1.ticket_id)
    lot.unpark_vehicle(ticket3.ticket_id)
    print()

    # --- 4. Concurrency Test: Multi-gate parking simulation ---
    print("--- 4. Concurrency Test: 4 Vehicles entering simultaneously ---")
    gate_vehicles = [
        Car("CAR-CONC-1"),
        Car("CAR-CONC-2"),
        Car("CAR-CONC-3"),
        Car("CAR-CONC-4")
    ]
    
    threads = []
    for vehicle in gate_vehicles:
        t = threading.Thread(target=simulate_gate_entry, args=(vehicle,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n==========================================================")
    print("Parking Lot Case Study completed successfully!")
    print("==========================================================")
