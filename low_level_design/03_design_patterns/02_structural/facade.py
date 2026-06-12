#!/usr/bin/env python3
"""
Phase 3: Classic Design Patterns (Structural)
Module: Facade Pattern

The Facade pattern provides a simplified interface to a complex subsystem
of classes, library, or framework. It shields client code from direct
interaction with multiple moving parts, reducing dependency coupling.

Example:
A Home Theater System. Watching a movie requires coordinate execution of multiple
components: turning on lights, dimming them, lowering the screen, turning on 
projector, configuring sound system, and starting the player.
A HomeTheaterFacade exposes simple 'watch_movie' and 'end_movie' interfaces.
"""

# =====================================================================
# THE SUBSYSTEM CLASSES
# =====================================================================
class Amplifier:
    def turn_on(self): print("Amplifier: ON")
    def set_volume(self, level: int): print(f"Amplifier: Volume set to {level}")
    def turn_off(self): print("Amplifier: OFF")

class Projector:
    def turn_on(self): print("Projector: ON")
    def set_input(self, input_source: str): print(f"Projector: Input set to {input_source}")
    def turn_off(self): print("Projector: OFF")

class TheaterLights:
    def dim(self, level: int): print(f"Lights: Dimmed to {level}%")
    def turn_on(self): print("Lights: ON (Full Brightness)")

class Screen:
    def lower(self): print("Screen: Lowered down")
    def raise_up(self): print("Screen: Raised up")

class StreamingService:
    def play_movie(self, title: str): print(f"Streaming Service: Playing '{title}'")
    def stop(self): print("Streaming Service: Stopped playback")


# =====================================================================
# THE FACADE
# =====================================================================
class HomeTheaterFacade:
    """The Facade wraps the complex subsystem and exposes simple APIs."""
    def __init__(self, amp: Amplifier, proj: Projector, lights: TheaterLights, screen: Screen, stream: StreamingService):
        self._amp = amp
        self._proj = proj
        self._lights = lights
        self._screen = screen
        self._stream = stream

    def watch_movie(self, title: str):
        print(f"\n[Facade] Preparing to watch '{title}'...")
        self._lights.dim(10)
        self._screen.lower()
        self._proj.turn_on()
        self._proj.set_input("Streaming Box")
        self._amp.turn_on()
        self._amp.set_volume(7)
        self._stream.play_movie(title)
        print("[Facade] Movie setup complete. Enjoy!")

    def end_movie(self):
        print("\n[Facade] Shutting down home theater...")
        self._stream.stop()
        self._amp.turn_off()
        self._proj.turn_off()
        self._screen.raise_up()
        self._lights.turn_on()
        print("[Facade] Theater successfully shut down.")


# =====================================================================
# EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("==========================================================")
    print("FACADE DESIGN PATTERN")
    print("==========================================================\n")

    # Client instantiates subsystem components
    amp = Amplifier()
    proj = Projector()
    lights = TheaterLights()
    screen = Screen()
    stream = StreamingService()

    # Create the Facade
    facade = HomeTheaterFacade(amp, proj, lights, screen, stream)

    # Client uses the Facade instead of calls to 5 different classes!
    facade.watch_movie("Interstellar")
    facade.end_movie()

    print("\n==========================================================")
    print("Facade Pattern completed successfully!")
    print("==========================================================")
