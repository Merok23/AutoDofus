# map_cycler.py
"""
This class contains the logic of clycling through the maps.
"""
from src.common.event import Event
from src.player.reader import Reader
from src.player.player import Player

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 630


class MapCycler:
    """
    This class contains the logic of cycling through the maps.
    """

    def __init__(self, map_coordinates):
        """
        Initialize the map cycler.

        :param map_coordinates: tuple of (x, y) map coordinates
        """
        self.map_coordinates = map_coordinates
        self.csv_reader = Reader(map_coordinates)
        self.finished = False

    def start(self):
        """
        Run the map cycler in a loop.
        """
        while not self.finished:
            events = self.csv_reader.read_events()
            player = Player(events)
            player.play()
            last_event = events[-1]
            next_map = self._calculate_next_map(last_event, self.map_coordinates)
            self.csv_reader = Reader(next_map)

    def stop(self):
        """
        Stop the map cycler.
        """
        self.finished = True

    def _calculate_next_map(self, last_event: Event, map_coordinates):
        """
        Calculate the next map coordinates.

        :param last_event: last event of the map
        :param map_coordinates: current map coordinates
        """
        if last_event.get_event_type() == "keyboard":
            raise TypeError("Last event cannot be a keyboard event")

        event_data = last_event.get_event_data()
        x_pos = event_data[0]
        y_pos = event_data[1]

        x_distance_to_left = x_pos
        x_distance_to_right = SCREEN_WIDTH - x_pos
        y_distance_to_top = y_pos
        y_distance_to_bottom = SCREEN_HEIGHT - y_pos

        min_distance = min(
            x_distance_to_left,
            x_distance_to_right,
            y_distance_to_top,
            y_distance_to_bottom,
        )

        if min_distance == x_distance_to_left:
            return (map_coordinates[0] - 1, map_coordinates[1])  # left
        if min_distance == x_distance_to_right:
            return (map_coordinates[0] + 1, map_coordinates[1])  # right
        if min_distance == y_distance_to_top:
            return (map_coordinates[0], map_coordinates[1] + 1)  # top
        return (map_coordinates[0], map_coordinates[1] - 1)  # bottom
