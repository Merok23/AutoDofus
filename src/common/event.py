# event.py
"""
This class is only for storing events.
"""


class Event:
    """
    The idea of the event is:
    - event_type: keyboard or mouse
    - event_subtype: press, release, click, scroll
    - event_data: key or mouse data
        For key press/release: key
        For mouse click: (x, y, button, pressed)
    - event_time: time since the last event
    """

    def __init__(self, event_type, event_subtype, event_data, event_time):
        self.event_type = event_type
        self.event_subtype = event_subtype
        for data in event_data:
            if data not in ["left", "right", "middle"]:
                data = int(data)
        self.event_data = event_data
        self.event_time = event_time

    def get_event_type(self):
        """
        Returns the event type.

        :return: event type (str, "keyboard" or "mouse")
        """
        return self.event_type

    def get_event_subtype(self):
        """
        Returns the event subtype.

        :return: event subtype (str, "press", "release", "click", "scroll")
        """
        return self.event_subtype

    def get_event_data(self):
        """
        Returns the event data.

        :return: event data (varies based on event type and subtype)
        """
        return self.event_data

    def get_event_time(self):
        """
        Returns the event time.

        :return: event time (float)
        """
        return self.event_time

    # to print the events:
    def __str__(self):
        literal = ""
        literal += f"Event: {self.event_type}, {self.event_subtype}, "
        literal += f"{self.event_data}, {self.event_time}"
        return literal
