from typing import List

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import OoTMMItem, items
from .Options import ootmm_options
from .Locations import OoTMMLocation, locations
import json


class OoTMMWebWorld(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Archipelago Ocarina of Time & Majora's Mask software on your computer.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["Fletch & Iryoku"],
    )

    tutorials = [setup_en]


class OoTMMWorld(World):
    """Ocarina of Time & Majora's Mask"""

    game = "Ocarina of Time & Majora's Mask"
    data_version = 3
    web = OoTMMWebWorld()
    option_definitions = ootmm_options
    location_name_to_id = {name: location.id for name, location in locations.items()}
    item_name_to_id = {item.display_name: code for code, item in items.items()}
    item_symbolic_id_to_id = {item.symbolic_id: code for code, item in items.items()}

    def create_item(self, item: str) -> OoTMMItem:
        id = self.item_name_to_id[item]
        return self.create_item_from_id(id)

    def create_item_from_symbolic_id(self, symbolic_id: str) -> OoTMMItem:
        id = self.item_symbolic_id_to_id[symbolic_id]
        return self.create_item_from_id(id)

    def create_item_from_id(self, id: int) -> OoTMMItem:
        data = items[id]
        return OoTMMItem(data.display_name, data.classification, data.code, self.player)

    def create_items(self) -> None:
        item_pool: list[OoTMMItem] = []
        filler: list[OoTMMItem] = []

        for location in locations.values():
            symbolic_id = location.vanilla_item

            # Handle RANDOM and FLEXIBLE items
            if symbolic_id == "OOT_RANDOM" or symbolic_id == "OOT_FLEXIBLE":
                symbolic_id = "OOT_RUPEE_GREEN"
            elif symbolic_id == "MM_RANDOM":
                symbolic_id = "MM_RUPEE_GREEN"

            item = self.create_item_from_symbolic_id(symbolic_id)
            if item.advancement or item.useful:
                item_pool.append(item)
            else:
                filler.append(item)

        # The Deku Mask is required, but does not exist at any vanilla
        # location in the randomizer, so we need to explicitly add it
        # to the item pool.
        item_pool.append(self.create_item_from_symbolic_id("MM_MASK_DEKU"))

        # and then remove one filler item to make room for the Deku Mask
        filler.remove(self.random.choice(filler))

        self.multiworld.itempool += item_pool
        self.multiworld.itempool += filler

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        ootmm = Region("OoTMM", self.player, self.multiworld)
        self.multiworld.regions.append(ootmm)
        menu.connect(ootmm)

        ootmm.add_locations(self.location_name_to_id, OoTMMLocation)

        self.multiworld.completion_condition[self.player] = lambda state: (
            state.has("GANON", self.player) and state.has("MAJORA", self.player)
        )

    def generate_output(self, output_directory):
        pass
        # zetable = []
        # for location in self.multiworld.get_locations(self.player):
        #     assert isinstance(location, OoTMMLocation)
        #     key = location.name
        #     data = location_data_table[key]
        #     if location.item.player == self.player:
        #         zetable.append(
        #             {
        #                 "Location Name": data.name,
        #                 "Location Id": data.id,
        #                 "Game": data.game,
        #                 "Item": {"Type": "OoTM", "Id": location.item.name},
        #             }
        #         )
        #     else:
        #         zetable.append(
        #             {
        #                 "Location Name": data.name,
        #                 "Location Id": data.id,
        #                 "Game": data.game,
        #                 "Item": {"Type": "AP", "Id": location.item.code, "Slot": location.item.player},
        #             }
        #         )

        # with open(output_directory + "/output.json", "w", encoding="utf-8") as outfile:
        #     outfile.write(json.dumps(zetable))

        # path = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}.json")

    # def set_rules(self) -> None:
    #     button_rule = get_button_rule(self.multiworld, self.player)
    #     self.multiworld.get_location("The Big Red Button", self.player).access_rule = button_rule
    #     self.multiworld.get_location("In the Player's Mind", self.player).access_rule = button_rule

    #     # Do not allow button activations on buttons.
    #     self.multiworld.get_location("The Big Red Button", self.player).item_rule =\
    #         lambda item: item.name != "Button Activation"

    #     # Completion condition.
    #     self.multiworld.completion_condition[self.player] = lambda state: state.has("The Urge to Push", self.player)

    # def fill_slot_data(self):
    #     return {
    #         "color": getattr(self.multiworld, "color")[self.player].current_key
    #     }
