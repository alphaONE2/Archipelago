from BaseClasses import Location
from .LocationsOoT import oot_locations
from .LocationsMM import mm_locations

class OoTMMLocation(Location):
    game = "Ocarina of Time & Majora's Mask"

locations = oot_locations | mm_locations