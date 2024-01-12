# player.py
"""
This module represents the player that will recreate the events.
"""
import time
from pynput import keyboard, mouse
from src.common.event import Event


class Player:
    """
    Class used to store the logic of the player.
    """

    def __init__(self, events):
        """
        Initialize the player.

        :param events: list of events
        """
        self.events = events

    def play(self):
        """
        Play the events.
        """
        current_time = time.time()
        for event in self.events:
            if event.get_event_type() == "keyboard":
                # We ignore the keyboard events for now
                time.sleep(event.get_event_time())
            else:
                self._play_mouse_event(event)
                # the sleep is inside the _move_mouse function
            elapsed_time = time.time() - current_time
            if elapsed_time < event.get_event_time():
                time.sleep(event.get_event_time() - elapsed_time)
            current_time = time.time()

    def get_events(self):
        """
        Return the events.
        """
        return self.events

    def _play_keyboard_event(self, event):
        """
        Play a keyboard event.
        """
        if event.get_event_subtype() == "press":
            keyboard.Controller().press(event.get_event_data())
        else:
            keyboard.Controller().release(event.get_event_data())

    def _play_mouse_event(self, event: Event):
        """
        Play a mouse event.
        """
        event_data = event.get_event_data()
        if event.get_event_subtype() == "scroll":
            pass

        # click:
        # NEEDS TO BE DEBUGGED:
        self.__move_mouse(event_data[0], event_data[1], event.get_event_time())
        mouse.Controller().click(mouse.Button.left, 1)

    def __move_mouse(self, x_position, y_position, duration):
        """
        Move the mouse to the given position in the given duration.

        :param x_position: x position
        :param y_position: y position
        :param duration: duration of the movement in seconds
        """
        # Calculate the number of steps for the given duration
        # steps = 50
        # sleep_time = duration / steps
        # Calculate the distance to move in each step
        # delta_x = (x_position - mouse.Controller().position[0]) / steps
        # delta_y = (y_position - mouse.Controller().position[1]) / steps

        # for i in range(steps):
        #     new_x = mouse.Controller().position[0] + delta_x * (i + 1)
        #     new_y = mouse.Controller().position[1] + delta_y * (i + 1)
        #     mouse.Controller().position = (new_x, new_y)
        #     time.sleep(sleep_time)

        mouse.Controller().position = (x_position, y_position)
        time.sleep(duration)
