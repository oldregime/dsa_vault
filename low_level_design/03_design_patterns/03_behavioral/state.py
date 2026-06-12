#!/usr/bin/env python3
"""
Phase 3: Classic Design Patterns (Behavioral)
Module: State Pattern

The State pattern allows an object to alter its behavior when its internal
state changes. The object will appear to change its class.

Example:
A Document Approval Workflow in a CMS (Content Management System).
States: Draft, Moderated, Published.
Transitions: publish(), rollback().
"""

from abc import ABC, abstractmethod

# =====================================================================
# THE STATE INTERFACE
# =====================================================================
class State(ABC):
    def __init__(self, document: "DocumentContext"):
        # The state retains a reference back to the context
        self.doc = document

    @abstractmethod
    def publish(self) -> None: pass

    @abstractmethod
    def rollback(self) -> None: pass

    @abstractmethod
    def get_status(self) -> str: pass


# =====================================================================
# THE CONTEXT CLASS
# =====================================================================
class DocumentContext:
    """The context class that is exposed to client code."""
    def __init__(self):
        # Initial state is Draft
        self._state = DraftState(self)

    def transition_to(self, state: State):
        print(f"[Context] Transitioning from {self._state.get_status()} to {state.get_status()}...")
        self._state = state

    # Delegates methods to current State object
    def publish(self):
        self._state.publish()

    def rollback(self):
        self._state.rollback()

    def get_status(self) -> str:
        return self._state.get_status()


# =====================================================================
# CONCRETE STATES
# =====================================================================
class DraftState(State):
    def publish(self) -> None:
        print("[Draft State] Submitting document for moderator review.")
        self.doc.transition_to(ModeratedState(self.doc))

    def rollback(self) -> None:
        print("[Draft State] Already in draft. Cannot rollback further.")

    def get_status(self) -> str:
        return "DRAFT"


class ModeratedState(State):
    def publish(self) -> None:
        print("[Moderated State] Moderator approved the document. Publishing...")
        self.doc.transition_to(PublishedState(self.doc))

    def rollback(self) -> None:
        print("[Moderated State] Moderator rejected the document. Returning to draft.")
        self.doc.transition_to(DraftState(self.doc))

    def get_status(self) -> str:
        return "MODERATED"


class PublishedState(State):
    def publish(self) -> None:
        print("[Published State] Document is already published. No action taken.")

    def rollback(self) -> None:
        print("[Published State] Pulling document from production. Moving to Moderation.")
        self.doc.transition_to(ModeratedState(self.doc))

    def get_status(self) -> str:
        return "PUBLISHED"


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("STATE DESIGN PATTERN")
    print("==========================================================\n")

    # Initialize Context (starts in DRAFT)
    my_doc = DocumentContext()
    print(f"Current Status: {my_doc.get_status()}\n")

    # 1. Rollback in Draft (No-op)
    my_doc.rollback()
    print()

    # 2. Publish Draft -> moves to MODERATED
    my_doc.publish()
    print(f"Current Status: {my_doc.get_status()}\n")

    # 3. Publish Moderated -> moves to PUBLISHED
    my_doc.publish()
    print(f"Current Status: {my_doc.get_status()}\n")

    # 4. Try to Publish again (No-op)
    my_doc.publish()
    print()

    # 5. Rollback Published -> moves back to MODERATED
    my_doc.rollback()
    print(f"Current Status: {my_doc.get_status()}\n")

    # 6. Rollback Moderated -> moves back to DRAFT
    my_doc.rollback()
    print(f"Current Status: {my_doc.get_status()}")

    print("\n==========================================================")
    print("State Pattern completed successfully!")
    print("==========================================================")
