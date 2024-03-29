# main.py
"""
This is the main file for the player, it receives the map coordinates
by command line arguments, these are where the player is currently standing.
"""
import sys
import time
from src.player.map_cycler import MapCycler


def main():
    """
    Main function of the program.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <x> <y>")
        return
    map_coordinates = (int(sys.argv[1]), int(sys.argv[2]))
    print("Press Cntrl+C to stop playing...")
    print("Starting in 3...")
    time.sleep(1)
    print("Starting in 2...")
    time.sleep(1)
    print("Starting in 1...")
    time.sleep(1)
    print("Starting!")
    cycler = MapCycler(map_coordinates)
    cycler.start()  # we need to interrupt this
    cycler.stop()
    print("Done!")


if __name__ == "__main__":
    main()
