#!/usr/bin/env python3
"""
Phase 3: Classic Design Patterns (Behavioral)
Module: Command Pattern

The Command pattern encapsulates a request as an object, thereby letting you
parameterize clients with different requests, queue or log requests, and 
support undoable operations.

Example:
A Document Text Editor. Actions like writing text or deleting text are wrapped
as command objects. The editor maintains a history stack, allowing full Undo/Redo.
"""

from abc import ABC, abstractmethod
from typing import List

# =====================================================================
# THE RECEIVER
# =====================================================================
class TextDocument:
    """The Receiver class. Contains actual business logic to manipulate text."""
    def __init__(self):
        self.text = ""

    def insert_text(self, position: int, content: str):
        self.text = self.text[:position] + content + self.text[position:]

    def delete_text(self, position: int, length: int) -> str:
        deleted = self.text[position : position + length]
        self.text = self.text[:position] + self.text[position + length :]
        return deleted

    def __str__(self) -> str:
        return f"Document Content: '{self.text}'"


# =====================================================================
# THE COMMAND INTERFACE
# =====================================================================
class Command(ABC):
    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


# =====================================================================
# CONCRETE COMMANDS
# =====================================================================
class InsertTextCommand(Command):
    """Command to insert text at a specific index."""
    def __init__(self, doc: TextDocument, position: int, text_to_insert: str):
        self.doc = doc
        self.position = position
        self.text_to_insert = text_to_insert

    def execute(self) -> None:
        self.doc.insert_text(self.position, self.text_to_insert)

    def undo(self) -> None:
        # To undo insertion, delete the exact text we inserted
        self.doc.delete_text(self.position, len(self.text_to_insert))


class DeleteTextCommand(Command):
    """Command to delete text at a specific index. Keeps track of deleted text for undo."""
    def __init__(self, doc: TextDocument, position: int, length: int):
        self.doc = doc
        self.position = position
        self.length = length
        self.deleted_text = ""

    def execute(self) -> None:
        # Save deleted text so we can restore it on undo
        self.deleted_text = self.doc.delete_text(self.position, self.length)

    def undo(self) -> None:
        # Restore the saved text
        self.doc.insert_text(self.position, self.deleted_text)


# =====================================================================
# THE INVOKER / HISTORY TRACKER
# =====================================================================
class EditorInvoker:
    """The Invoker. Triggers commands and manages the undo history stack."""
    def __init__(self):
        self._history: List[Command] = []

    def execute_command(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo(self):
        if not self._history:
            print("[Invoker] Nothing to undo.")
            return
        
        command = self._history.pop()
        command.undo()
        print(f"[Invoker] Undo executed.")


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("COMMAND DESIGN PATTERN (WITH UNDO HISTORY)")
    print("==========================================================\n")

    # Document (Receiver) and Editor (Invoker)
    doc = TextDocument()
    editor = EditorInvoker()
    print(f"Initial State: {doc}")

    # 1. Insert some text
    print("\nExecuting: Insert 'Hello ' at index 0")
    cmd1 = InsertTextCommand(doc, 0, "Hello ")
    editor.execute_command(cmd1)
    print(doc)

    # 2. Insert more text
    print("\nExecuting: Insert 'World!' at index 6")
    cmd2 = InsertTextCommand(doc, 6, "World!")
    editor.execute_command(cmd2)
    print(doc)

    # 3. Delete some text
    print("\nExecuting: Delete 6 characters starting at index 0 ('Hello ')")
    cmd3 = DeleteTextCommand(doc, 0, 6)
    editor.execute_command(cmd3)
    print(doc)

    # 4. Perform Undo
    print("\n--- Triggering Undo ---")
    editor.undo()
    print(doc)

    # 5. Perform another Undo
    print("\n--- Triggering Undo ---")
    editor.undo()
    print(doc)

    # 6. Perform another Undo
    print("\n--- Triggering Undo ---")
    editor.undo()
    print(doc)

    print("\n==========================================================")
    print("Command Pattern completed successfully!")
    print("==========================================================")
