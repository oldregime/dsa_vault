#!/usr/bin/env python3
"""
Phase 3: Classic Design Patterns (Creational)
Module: Factory Patterns (Factory Method & Abstract Factory)

1. Factory Method: Defines an interface for creating a single product, but delegates
   instantiation to concrete creator subclasses.
2. Abstract Factory: Provides an interface for creating families of related or
   dependent products (e.g., Mac Button + Mac Textbox vs Windows Button + Windows Textbox)
   without specifying their concrete classes.
"""

from abc import ABC, abstractmethod

# =====================================================================
# PART 1: FACTORY METHOD PATTERN
# =====================================================================
# Goal: Create different kinds of document readers.

# Product Interface
class Document(ABC):
    @abstractmethod
    def read(self) -> str:
        pass

# Concrete Products
class PDFDocument(Document):
    def read(self) -> str:
        return "Reading content from PDF document."

class WordDocument(Document):
    def read(self) -> str:
        return "Reading content from Word document."


# Creator Class (Factory Method Interface)
class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        """The Factory Method."""
        pass

    def open_and_inspect(self) -> str:
        """Core business logic that uses the product returned by the factory method."""
        doc = self.create_document()
        return f"[Creator Logger] Opening document: {doc.read()}"


# Concrete Creators
class PDFCreator(DocumentCreator):
    def create_document(self) -> Document:
        return PDFDocument()

class WordCreator(DocumentCreator):
    def create_document(self) -> Document:
        return WordDocument()


# =====================================================================
# PART 2: ABSTRACT FACTORY PATTERN
# =====================================================================
# Goal: Create UI elements (Button and Checkbox) for Windows and MacOS.

# Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self) -> str: pass

class Checkbox(ABC):
    @abstractmethod
    def toggle(self) -> str: pass


# Windows Concrete Products
class WindowsButton(Button):
    def render(self) -> str:
        return "Rendering Windows style button [__]"

class WindowsCheckbox(Checkbox):
    def toggle(self) -> str:
        return "Toggled Windows checkbox [X]"


# MacOS Concrete Products
class MacOSButton(Button):
    def render(self) -> str:
        return "Rendering macOS style glass button (O)"

class MacOSCheckbox(Checkbox):
    def toggle(self) -> str:
        return "Toggled macOS style checkmark (/)"


# Abstract Factory Interface
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox: pass


# Concrete Factories
class WindowsUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacOSUIFactory(UIFactory):
    def create_button(self) -> Button:
        return MacOSButton()
    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("FACTORY METHOD & ABSTRACT FACTORY PATTERNS")
    print("==========================================================\n")

    # --- 1. Factory Method Demo ---
    print("--- 1. Factory Method Demonstration ---")
    creators = [PDFCreator(), WordCreator()]
    for creator in creators:
        print(creator.open_and_inspect())
    print()

    # --- 2. Abstract Factory Demo ---
    print("--- 2. Abstract Factory Demonstration ---")
    # Client code is completely decoupled from concrete operating system UI elements.
    def build_application_ui(factory: UIFactory):
        btn = factory.create_button()
        chk = factory.create_checkbox()
        print(f"UI Built:")
        print(f"  Button:   {btn.render()}")
        print(f"  Checkbox: {chk.toggle()}")

    print("Configuring app for Windows OS:")
    build_application_ui(WindowsUIFactory())
    
    print("\nConfiguring app for macOS:")
    build_application_ui(MacOSUIFactory())

    print("\n==========================================================")
    print("Factory Pattern module completed successfully!")
    print("==========================================================")
