# reader.py
"""
Simple csv reader that loads the events from the csv file.
"""
import csv
from src.common.event import Event

DIR_PATH = "./src/logger/maps"


class Reader:
    """
    Reader class that loads events from the csv file.
    """

    def __init__(self, map_coordinates):
        """
        Initialize the reader.

        :param map_coordinates: tuple of (x, y) map coordinates
        """
        self._map_coordinates = map_coordinates

    def read_events(self):
        """
        Read the events from the csv file.

        :return: list of events
        """
        events = []
        path = f"{DIR_PATH}/{self._map_coordinates[0]}_{self._map_coordinates[1]}.csv"
        with open(path, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            next(csv_reader)  # skip header
            for row in csv_reader:
                event_type = row[0]
                event_subtype = row[1]
                if event_subtype == "keyboard":
                    event_data = row[2]
                else:
                    event_data = row[2].split(";")
                    event_data = event_data[:-2]
                    event_data = [int(data) for data in event_data]
                event_time = float(row[3])
                events.append(Event(event_type, event_subtype, event_data, event_time))
        return events

    def get_map_coordinates(self):
        """
        Return the map coordinates.
        """
        return self._map_coordinates
