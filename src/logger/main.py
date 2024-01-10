# main.py
"""
This is the main file, it receives the map coordinates by command line arguments
and runs the map_logger
"""
import sys
from map_logger import MapLogger

DIRECTORY_PATH = "./maps"


def main():
    """
    Main function of the program.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <x> <y>")
        return
    map_coordinates = (int(sys.argv[1]), int(sys.argv[2]))
    map_logger = MapLogger(map_coordinates)
    print("Press Escape to stop logging...")
    map_logger.start_logging()
    map_logger.stop_logging()
    map_logger.dump_to_csv(DIRECTORY_PATH)
    print("Done!")


if __name__ == "__main__":
    main()
