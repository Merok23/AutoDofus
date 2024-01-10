# event_logger.py
"""
Class used to store the logic of the logger.
"""
import time
from pynput import keyboard, mouse
from event import Event


class Logger:
    """
    This class is used to manage the keyboard an mouse events and
    store them in RAM.

    :param _events: list of events
    :param _last_time: time of the last event
    """

    def __init__(self):
        """
        Initialize the logger.
        """
        self._events = []
        self._last_time = time.time()
        self.finished = False
        self.keyboard_listener = None
        self.mouse_listener = None

    def _on_keyboard_press(self, key):
        """
        Handle keyboard press events.
        """
        if key == keyboard.Key.esc:
            self.stop_logging()
            return False
        self._events.append(
            Event("keyboard", "press", key, time.time() - self._last_time)
        )
        self._last_time = time.time()
        return True

    def _on_keyboard_release(self, key):
        """
        Handle keyboard release events.
        """
        self._events.append(
            Event("keyboard", "release", key, time.time() - self._last_time)
        )
        self._last_time = time.time()

    def _translate_button(self, button):
        """
        Translate the button to a string.
        """
        if button == mouse.Button.left:
            return "left"
        if button == mouse.Button.right:
            return "right"
        return "middle"

    def _on_mouse_click(self, x_pos, y_pos, button, pressed):
        """
        Handle mouse click events.
        """
        button = self._translate_button(button)
        self._events.append(
            Event(
                "mouse",
                "click",
                (x_pos, y_pos, button, pressed),
                time.time() - self._last_time,
            )
        )
        self._last_time = time.time()

    def dump_to_csv(self, file_path):
        """
        Dump the recorded events to a csv file.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("event_type,event_subtype,event_data,event_time\n")
            for event in self._events:
                file.write(f"{event.event_type},{event.event_subtype}")
                file.write(f",{event.event_data},{event.event_time}\n")

    def start_logging(self):
        """
        Start logging keyboard and mouse events.
        """
        self.keyboard_listener = keyboard.Listener(
            on_press=self._on_keyboard_press, on_release=self._on_keyboard_release
        )
        self.mouse_listener = mouse.Listener(on_click=self._on_mouse_click)

        with self.keyboard_listener as keyboard_listener:
            with self.mouse_listener as mouse_listener:
                keyboard_listener.join()
                mouse_listener.join()

    def stop_logging(self):
        """
        Stop logging keyboard and mouse events.
        """
        self.finished = True
        self.keyboard_listener.stop()
        self.mouse_listener.stop()

    def get_events(self):
        """
        Returns a list of events.
        """
        return self._events
