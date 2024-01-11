# map_logger.py
"""
Map logger class.
It's used to create a single csv of a single map using the logger.
"""
from src.logger.event_logger import Logger


class MapLogger:
    """
    This class is used to create a single csv of a single map using the logger.
    """

    def __init__(self, map_coordinates):
        """
        Initialize the map logger.
        :param map_coordinates: tuple of (x, y) coordinates of the map
        """
        self._logger = Logger()
        self._map_coordinates = map_coordinates

    def start_logging(self):
        """
        Start logging the map.
        """
        self._logger.start_logging()

    def stop_logging(self):
        """
        Stop logging the map.
        """
        self._logger.stop_logging()

    def dump_to_csv(self, file_path):
        """
        Dump the recorded events to a csv file.

        :param file_path: path to the directory you want to save the csv file in
        """
        file_name = f"{self._map_coordinates[0]}_{self._map_coordinates[1]}.csv"
        self._logger.dump_to_csv(f"{file_path}/{file_name}")
