#!/usr/bin/env python3
"""
Phase 4: Enterprise Case Studies
Module 03: Multi-Elevator System Design

This module implements a complete, enterprise-grade Low-Level Design (LLD) for a
Multi-Elevator Controller System.

Features:
1. Support for multiple elevators.
2. Directional states (IDLE, UP, DOWN) and elevator status management.
3. Distinguishes between External Request (hall button pressed at a floor to go UP/DOWN)
   and Internal Request (button pressed inside a specific elevator cabin).
4. EFFICIENT DISPATCH ALGORITHM: Selects the optimal elevator based on proximity, 
   direction matches, and state.
5. Elevators move according to the LOOK/SCAN algorithm.
"""

from enum import Enum
from typing import List, Set, Dict, Optional
import time

# =====================================================================
# ENUMS & MODELS
# =====================================================================
class Direction(Enum):
    UP = 1
    DOWN = 2
    IDLE = 3


class RequestType(Enum):
    INTERNAL = 1  # Passenger pressed button inside elevator
    EXTERNAL = 2  # Passenger pressed hall call button on a floor


class ElevatorRequest:
    def __init__(self, target_floor: int, direction: Direction, req_type: RequestType):
        self.target_floor = target_floor
        self.direction = direction
        self.req_type = req_type


# =====================================================================
# THE ELEVATOR CAR
# =====================================================================
class ElevatorCar:
    """Represents an individual elevator cabin, its state and request queues."""
    def __init__(self, elevator_id: int, total_floors: int):
        self.elevator_id = elevator_id
        self.current_floor = 0
        self.direction = Direction.IDLE
        self.total_floors = total_floors
        
        # Request sets: separated to implement standard LOOK algorithm
        self.up_stops: Set[int] = set()
        self.down_stops: Set[int] = set()

    def add_request(self, request: ElevatorRequest):
        floor = request.target_floor
        if request.direction == Direction.UP or (request.direction == Direction.IDLE and floor > self.current_floor):
            self.up_stops.add(floor)
        else:
            self.down_stops.add(floor)
            
        # If currently idle, determine immediate direction
        if self.direction == Direction.IDLE:
            if floor > self.current_floor:
                self.direction = Direction.UP
            elif floor < self.current_floor:
                self.direction = Direction.DOWN
            else:
                self.direction = Direction.IDLE  # Already on that floor

    def step(self) -> Optional[int]:
        """
        Simulates one step of elevator motion (moving up/down 1 floor).
        Returns the floor number if a stop is made, else None.
        Uses LOOK algorithm.
        """
        # If idle, do nothing
        if self.direction == Direction.IDLE:
            return None

        # 1. Move one floor in current direction
        if self.direction == Direction.UP:
            self.current_floor += 1
        elif self.direction == Direction.DOWN:
            self.current_floor -= 1

        print(f"[Elevator {self.elevator_id}] Reached Floor {self.current_floor} (Moving {self.direction.name})")

        # 2. Check if we should stop at the current floor
        stopped = False
        if self.direction == Direction.UP and self.current_floor in self.up_stops:
            self.up_stops.remove(self.current_floor)
            stopped = True
        elif self.direction == Direction.DOWN and self.current_floor in self.down_stops:
            self.down_stops.remove(self.current_floor)
            stopped = True

        # 3. Check for direction switch or transition to IDLE (LOOK Logic)
        if self.direction == Direction.UP:
            # If no more stops above us, we either reverse or go IDLE
            if not any(f > self.current_floor for f in self.up_stops | self.down_stops):
                if self.down_stops:
                    self.direction = Direction.DOWN
                else:
                    self.direction = Direction.IDLE
        elif self.direction == Direction.DOWN:
            # If no more stops below us, we either reverse or go IDLE
            if not any(f < self.current_floor for f in self.up_stops | self.down_stops):
                if self.up_stops:
                    self.direction = Direction.UP
                else:
                    self.direction = Direction.IDLE

        if stopped:
            print(f"[Elevator {self.elevator_id}] *** STOPPING at Floor {self.current_floor} to open doors ***")
            return self.current_floor

        return None

    def has_pending_requests(self) -> bool:
        return len(self.up_stops) > 0 or len(self.down_stops) > 0


# =====================================================================
# THE ELEVATOR DISPATCH CONTROLLER
# =====================================================================
class ElevatorController:
    """Manages the bank of elevator cars and schedules requests optimally."""
    def __init__(self, num_elevators: int, total_floors: int):
        self.total_floors = total_floors
        self.elevators: List[ElevatorCar] = [
            ElevatorCar(idx + 1, total_floors) for idx in range(num_elevators)
        ]

    def handle_external_request(self, floor: int, direction: Direction):
        """Dispatches the best suited elevator to respond to a floor hall button call."""
        request = ElevatorRequest(floor, direction, RequestType.EXTERNAL)
        best_elevator = self._find_optimal_elevator(floor, direction)
        print(f"[Controller] Hall Call at Floor {floor} to go {direction.name} -> Dispatched Elevator {best_elevator.elevator_id}")
        best_elevator.add_request(request)

    def handle_internal_request(self, elevator_id: int, target_floor: int):
        """Registers a button click inside the elevator cabin."""
        # Validate ID
        elevator = next((e for e in self.elevators if e.elevator_id == elevator_id), None)
        if elevator is None:
            print(f"[Controller] Error: Invalid elevator ID {elevator_id}")
            return
            
        direction = Direction.UP if target_floor > elevator.current_floor else Direction.DOWN
        request = ElevatorRequest(target_floor, direction, RequestType.INTERNAL)
        print(f"[Controller] Cabin button pressed in Elevator {elevator_id} for Floor {target_floor}")
        elevator.add_request(request)

    def _find_optimal_elevator(self, floor: int, direction: Direction) -> ElevatorCar:
        """
        Optimal Dispatch Algorithm:
        Assigns scores based on proximity and motion match.
        Lowest cost wins.
        """
        best_score = float('inf')
        selected_elevator = self.elevators[0]

        for elevator in self.elevators:
            cost = 0
            distance = abs(elevator.current_floor - floor)

            # Scenario 1: Elevator is IDLE (medium cost based on distance)
            if elevator.direction == Direction.IDLE:
                cost = distance + 5  # Fixed startup penalty

            # Scenario 2: Elevator is moving in the SAME direction
            elif elevator.direction == direction:
                # Elevator is on the path (low cost)
                if (direction == Direction.UP and elevator.current_floor <= floor) or \
                   (direction == Direction.DOWN and elevator.current_floor >= floor):
                    cost = distance
                # Elevator already passed the floor (high cost: must finish current run first)
                else:
                    cost = (self.total_floors * 2) - distance

            # Scenario 3: Elevator is moving in the OPPOSITE direction (high cost)
            else:
                cost = (self.total_floors * 2) + distance

            if cost < best_score:
                best_score = cost
                selected_elevator = elevator

        return selected_elevator

    def run_simulation_step(self) -> bool:
        """Runs one simulation step across all elevators. Returns True if any elevator is moving."""
        any_moving = False
        for elevator in self.elevators:
            if elevator.has_pending_requests() or elevator.direction != Direction.IDLE:
                elevator.step()
                any_moving = True
        return any_moving


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("ENTERPRISE LOW LEVEL DESIGN: MULTI-ELEVATOR SYSTEM")
    print("==========================================================\n")

    # Bank of 2 elevators, serving a building of 10 floors (0 to 9)
    controller = ElevatorController(num_elevators=2, total_floors=10)

    # Place initial elevator positions for testing
    controller.elevators[0].current_floor = 0
    controller.elevators[1].current_floor = 8
    
    print(f"System Initialized:")
    print(f"  Elevator 1 starts at Floor {controller.elevators[0].current_floor}")
    print(f"  Elevator 2 starts at Floor {controller.elevators[1].current_floor}\n")

    # --- Simulate Calls ---
    # 1. Hall Call: Floor 3 wants to go UP
    controller.handle_external_request(floor=3, direction=Direction.UP)
    
    # 2. Hall Call: Floor 7 wants to go DOWN
    controller.handle_external_request(floor=7, direction=Direction.DOWN)
    print()

    # Run simulation loop
    print("--- Running Elevator Simulation ---")
    step_count = 0
    while controller.run_simulation_step():
        step_count += 1
        time.sleep(0.05)  # Speeds up run for output
        
        # Inject passenger actions dynamically:
        if step_count == 3:
            # Passenger in Elevator 1 presses button for Floor 6
            # (Assuming Elevator 1 picked up the Floor 3 call)
            controller.handle_internal_request(elevator_id=1, target_floor=6)
        
        if step_count == 6:
            # New hall call: Floor 1 wants to go UP
            controller.handle_external_request(floor=1, direction=Direction.UP)

    print(f"\nAll elevator queues cleared in {step_count} simulation steps.")
    print("==========================================================")
    print("Elevator System Case Study completed successfully!")
    print("==========================================================")
