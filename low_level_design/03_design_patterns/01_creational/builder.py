#!/usr/bin/env python3
"""
Phase 3: Classic Design Patterns (Creational)
Module: Builder Pattern

The Builder pattern separates the construction of a complex object from its
representation, allowing the same construction process to create different
representations.
It is highly useful when an object requires many optional parameters to build,
preventing "telescoping constructor" anti-patterns.
"""

from typing import Optional

class Computer:
    """The complex object being built."""
    def __init__(self):
        self.cpu: Optional[str] = None
        self.ram_gb: Optional[int] = None
        self.storage_gb: Optional[int] = None
        self.gpu: Optional[str] = None
        self.os: Optional[str] = None

    def __str__(self) -> str:
        specs = []
        if self.cpu: specs.append(f"CPU: {self.cpu}")
        if self.ram_gb: specs.append(f"RAM: {self.ram_gb}GB")
        if self.storage_gb: specs.append(f"Storage: {self.storage_gb}GB")
        if self.gpu: specs.append(f"GPU: {self.gpu}")
        if self.os: specs.append(f"OS: {self.os}")
        return f"Computer [{', '.join(specs)}]"


class ComputerBuilder:
    """The builder that constructs the Computer step-by-step using a Fluent Interface."""
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._computer = Computer()

    def set_cpu(self, cpu: str) -> "ComputerBuilder":
        self._computer.cpu = cpu
        return self  # Return self to enable method chaining (fluent interface)

    def set_ram(self, ram_gb: int) -> "ComputerBuilder":
        self._computer.ram_gb = ram_gb
        return self

    def set_storage(self, storage_gb: int) -> "ComputerBuilder":
        self._computer.storage_gb = storage_gb
        return self

    def set_gpu(self, gpu: str) -> "ComputerBuilder":
        self._computer.gpu = gpu
        return self

    def set_os(self, os: str) -> "ComputerBuilder":
        self._computer.os = os
        return self

    def build(self) -> Computer:
        product = self._computer
        self.reset()  # Reset the builder state for the next build
        return product


class ComputerDirector:
    """
    The Director class is responsible for executing the building steps in a 
    predefined sequence. It knows the 'recipes' to build specific configurations.
    """
    def __init__(self, builder: ComputerBuilder):
        self._builder = builder

    def build_gaming_pc(self) -> Computer:
        return (self._builder
                .set_cpu("Intel Core i9 14900K")
                .set_ram(64)
                .set_storage(2000)
                .set_gpu("NVIDIA RTX 4090")
                .set_os("Windows 11")
                .build())

    def build_office_pc(self) -> Computer:
        return (self._builder
                .set_cpu("Intel Core i5")
                .set_ram(16)
                .set_storage(512)
                .set_os("Windows 11 Home")
                .build())


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("BUILDER DESIGN PATTERN (FLUENT INTERFACE)")
    print("==========================================================\n")

    builder = ComputerBuilder()
    director = ComputerDirector(builder)

    # --- 1. Building using the Director (Standard Recipes) ---
    print("--- 1. Building standard PCs via Director ---")
    gaming_rig = director.build_gaming_pc()
    office_machine = director.build_office_pc()
    print(f"Gaming PC: {gaming_rig}")
    print(f"Office PC: {office_machine}\n")

    # --- 2. Custom Building using the Builder Directly (Fluent Interface) ---
    print("--- 2. Custom Building with Method Chaining ---")
    custom_pc = (ComputerBuilder()
                 .set_cpu("AMD Ryzen 7 7800X3D")
                 .set_ram(32)
                 .set_os("Linux Ubuntu")
                 .build())
    print(f"Custom Linux PC: {custom_pc}")

    print("\n==========================================================")
    print("Builder Pattern module completed successfully!")
    print("==========================================================")
