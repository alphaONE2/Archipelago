# -----------------------------------------------------------------------------
# This file was auto-generated from the following files from the OoTMM project:
#
# https://raw.githubusercontent.com/OoTMM/OoTMM/master/
#    packages/core/lib/combo/settings/data.ts
# -----------------------------------------------------------------------------

from Options import Option, Choice, DefaultOnToggle, Toggle, Range, OptionSet, DeathLink


class OoTMMChoice(Choice):
    display_names: list[str] = []

    @classmethod
    def get_option_name(cls, value: int) -> str:
        if value in cls.display_names:
            return cls.display_names[value]
        return super().get_option_name(value)


# category: main


class Games(OoTMMChoice):
    """
    The games.

    OoT+MM: The combo randomizer experience.
    OoT Only: Ocarina of Time Only.
    MM Only: Majora's Mask Only.
    """

    display_name = "Games"

    option_ootmm = 0
    option_oot = 1
    option_mm = 2

    default = 0

    display_names = [
        "OoT+MM",
        "OoT Only",
        "MM Only",
    ]


class Goal(OoTMMChoice):
    """
    The objective of the seed. The game will end when the specified goal is reached.

    Any Final Boss: You can beat either Ganon or Majora.
    Ganon: You must beat Ganon.
    Majora: You must beat Majora.
    Ganon & Majora: You must beat Ganon AND Majora. You can do so in any order.
    Triforce Hunt: You must collect Triforce Pieces to win.
    Triforce Quest: You must collect the three parts of the Triforce (Power, Courage and Wisdom) to win. Specific hints will guide you.
    """

    display_name = "Goal"

    option_any = 0
    option_ganon = 1
    option_majora = 2
    option_both = 3
    option_triforce = 4
    option_triforce3 = 5

    default = 0

    display_names = [
        "Any Final Boss",
        "Ganon",
        "Majora",
        "Ganon & Majora",
        "Triforce Hunt",
        "Triforce Quest",
    ]


class TriforceGoal(Range):
    """
    The amount of Triforce Pieces that are required to win.
    """

    display_name = "Triforce Goal"

    range_start = 1
    range_end = 999

    default = 20

    # condition: function (s) { return s.goal === 'triforce'; }


class TriforcePieces(Range):
    """
    The total amount of Triforce Pieces in the item pool.
    """

    display_name = "Triforce Pieces"

    range_start = 1
    range_end = 999

    default = 30

    # condition: function (s) { return s.goal === 'triforce'; }


class ItemPool(OoTMMChoice):
    """
    Change the item pool.

    Plentiful: One extra copy of every major item. Heart containers only.
    Normal: The regular item count for each game.
    Scarce: One less of every major item. No Heart Pieces.
    Minimal: Only one of each major item. No Heart Pieces or Containers.
    Barren: Minimal item pool, plus every shuffled item that is not strictly required to reach the goal (beatable only) or any location (all locations) gets removed.
    """

    display_name = "Item Pool"

    option_plentiful = 0
    option_normal = 1
    option_scarce = 2
    option_minimal = 3
    option_barren = 4

    default = 0

    display_names = [
        "Plentiful",
        "Normal",
        "Scarce",
        "Minimal",
        "Barren",
    ]


# category: main.shuffle


class Songs(OoTMMChoice):
    """
    Controls where songs can be obtained, in both games.

    Song Locations: Only locations that contain songs in the vanilla games will have songs.
    Anywhere: Songs can be placed anywhere.
    """

    display_name = "Song Shuffle"

    option_song_locations = 0
    option_anywhere = 1

    default = 0

    display_names = [
        "Song Locations",
        "Anywhere",
    ]


class GoldSkulltulaTokens(OoTMMChoice):
    """
    Controls how Gold Skulltulas will be shuffled

    No Shuffle: All Gold Skulltula Tokens will be vanilla
    Dungeons Only: Only the Gold Skulltulas within dungeons will be shuffled
    Overworld Only: Only the Gold Skulltulas outside of dungeons will be shuffled
    All Tokens: Every single Gold Skulltula will be shuffled
    """

    display_name = "Gold Skulltula Tokens Shuffle"

    option_none = 0
    option_dungeons = 1
    option_overworld = 2
    option_all = 3

    default = 0

    display_names = [
        "No Shuffle",
        "Dungeons Only",
        "Overworld Only",
        "All Tokens",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class HousesSkulltulaTokens(OoTMMChoice):
    """
    Controls how Swamp and Ocean Skulltulas will be shuffled

    No Shuffle: Swamp and Ocean Tokens will be vanilla
    Gold Skulltulas Only: Any unshuffled Token can be found on any other unshuffled Skulltula
    All Tokens: Swamp and Ocean Tokens can be found anywhere
    """

    display_name = "House Skulltula Tokens Shuffle"

    option_none = 0
    option_cross = 1
    option_all = 2

    default = 0

    display_names = [
        "No Shuffle",
        "Gold Skulltulas Only",
        "All Tokens",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class TingleShuffle(OoTMMChoice):
    """
    Controls where Tingle Maps are

    Vanilla: Tingle Maps can be bought at Tingle, in their original locations
    Anywhere: Tingle Maps will be anywhere
    Starting Items: Tingle Maps are in Link's pocket
    Removed: Tingle Maps are fully removed and cannot be obtained
    """

    display_name = "Tingle Maps Shuffle"

    option_vanilla = 0
    option_anywhere = 1
    option_starting = 2
    option_removed = 3

    default = 0

    display_names = [
        "Vanilla",
        "Anywhere",
        "Starting Items",
        "Removed",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class MapCompassShuffle(OoTMMChoice):
    """
    Controls where Maps and Compasses can be

    Own Dungeon:  Maps and Compasses will be in their own dungeons
    Anywhere:  Maps and Compasses can be on any location
    Starting Items:  Maps and Compasses will be in Link's Pocket
    Removed: Fully removed and cannot be obtained
    """

    display_name = "Map / Compass Shuffle"

    option_own_dungeon = 0
    option_anywhere = 1
    option_starting = 2
    option_removed = 3

    default = 0

    display_names = [
        "Own Dungeon",
        "Anywhere",
        "Starting Items",
        "Removed",
    ]


class SmallKeyShuffleOot(OoTMMChoice):
    """
    Controls where Small Keys (for Dungeons) can be in OoT

    Own Dungeon: Dungeon Small Keys can only be found in their own dungeons
    Anywhere: Dungeon Small Keys can be found anywhere
    Removed: Small keys are removed and small key doors are unlocked
    """

    display_name = "Small Key Shuffle (OoT)"

    option_own_dungeon = 0
    option_anywhere = 1
    option_removed = 2

    default = 0

    display_names = [
        "Own Dungeon",
        "Anywhere",
        "Removed",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class SmallKeyShuffleMm(OoTMMChoice):
    """
    Controls where Small Keys (for Dungeons) can be in MM

    Own Dungeon: Dungeon Small Keys can only be found in their own dungeons
    Anywhere: Dungeon Small Keys can be found anywhere
    Removed: Small keys are removed and small key doors are unlocked
    """

    display_name = "Small Key Shuffle (MM)"

    option_own_dungeon = 0
    option_anywhere = 1
    option_removed = 2

    default = 0

    display_names = [
        "Own Dungeon",
        "Anywhere",
        "Removed",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class SmallKeyShuffleHideout(OoTMMChoice):
    """
    Controls where Hideout (Gerudo Fortress) Small Keys can be

    Vanilla: Hideout Small Keys are always on the guards
    Own Dungeon: Hideout Small Keys can only be found within Gerudo Fortress INTERIOR
    Anywhere: Hideout Small Keys can be found anywhere
    """

    display_name = "Hideout Small Key Shuffle"

    option_vanilla = 0
    option_own_dungeon = 1
    option_anywhere = 2

    default = 0

    display_names = [
        "Vanilla",
        "Own Dungeon",
        "Anywhere",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class SmallKeyShuffleChestGame(OoTMMChoice):
    """
    Controls where Chest Game Small Keys can be

    Vanilla: Chest Minigame will behave as in vanilla
    Own Minigame: Chest Minigame Keys can be found inside the minigame
    Anywhere: Chest Minigame Keys can be found anywhere
    """

    display_name = "Chest Game Small Key Shuffle"

    option_vanilla = 0
    option_own_dungeon = 1
    option_anywhere = 2

    default = 0

    display_names = [
        "Vanilla",
        "Own Minigame",
        "Anywhere",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class BossKeyShuffleOot(OoTMMChoice):
    """
    Controls where Boss Keys can be in OoT

    Own Dungeon: Boss Keys can only be in their own dungeons
    Anywhere: Boss Keys can be found anywhere
    Removed: Boss Keys are removed and boss doors are unlocked
    """

    display_name = "Boss Key Shuffle (OoT)"

    option_own_dungeon = 0
    option_anywhere = 1
    option_removed = 2

    default = 0

    display_names = [
        "Own Dungeon",
        "Anywhere",
        "Removed",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class BossKeyShuffleMm(OoTMMChoice):
    """
    Controls where Boss Keys can be in MM

    Own Dungeon: Boss Keys can only be in their own dungeons
    Anywhere: Boss Keys can be found anywhere
    Removed: Boss Keys are removed and boss doors are unlocked
    """

    display_name = "Boss Key Shuffle (MM)"

    option_own_dungeon = 0
    option_anywhere = 1
    option_removed = 2

    default = 0

    display_names = [
        "Own Dungeon",
        "Anywhere",
        "Removed",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class SmallKeyRingOot(OptionSet):
    """
    Controls the grouping of keys into key rings, for OoT

    forest: Forest Temple
    fire: Fire Temple
    water: Water Temple
    shadow: Shadow Temple
    spirit: Spirit Temple
    botw: Bottom of the Well
    gtg: Gerudo Training Grounds
    ganon: Ganon's Castle
    gf: Hideout
    tcg: Chest Game
    """

    display_name = "Small Key Ring (OoT)"

    valid_keys = {
        "forest",
        "fire",
        "water",
        "shadow",
        "spirit",
        "botw",
        "gtg",
        "ganon",
        "gf",
        "tcg",
    }

    # condition: function (x) { return hasGame(x, 'oot'); }


class SmallKeyRingMm(OptionSet):
    """
    Controls the grouping of keys into key rings, for MM

    wf: Woodfall Temple
    sh: Snowhead Temple
    gb: Great Bay Temple
    st: Stone Tower Temple
    """

    display_name = "Small Key Ring (MM)"

    valid_keys = {
        "wf",
        "sh",
        "gb",
        "st",
    }

    # condition: function (x) { return hasGame(x, 'mm'); }


class SilverRupeeShuffle(OoTMMChoice):
    """
    Make silver rupees items that can be shuffled.

    Vanilla: Silver Rupees are vanilla
    Own Dungeon: Silver Rupees are found within their own dungeon
    Anywhere: Silver Rupees are shuffled in the item pool
    """

    display_name = "Silver Rupee Shuffle"

    option_vanilla = 0
    option_own_dungeon = 1
    option_anywhere = 2

    default = 0

    display_names = [
        "Vanilla",
        "Own Dungeon",
        "Anywhere",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class SilverRupeePouches(OptionSet):
    """
    Controls grouping of silver rupees into a single item.

    dc: Dodongo's Cavern
    botw: Bottom of the Well
    spirit_child: Spirit Temple (Child)
    spirit_sun: Spirit Temple (Sun)
    spirit_boulders: Spirit Temple (Boulders)
    spirit_lobby: Spirit Temple (Lobby)
    spirit_adult: Spirit Temple (Adult)
    shadow_scythe: Shadow Temple (Scythe)
    shadow_pit: Shadow Temple (Pit)
    shadow_spikes: Shadow Temple (Spikes)
    shadow_blades: Shadow Temple (Blades)
    ic_scythe: Ice Cavern (Scythe)
    ic_block: Ice Cavern (Block)
    gtg_slopes: GTG (Slopes)
    gtg_lava: GTG (Lava)
    gtg_water: GTG (Water)
    ganon_light: Ganon (Light)
    ganon_forest: Ganon (Forest)
    ganon_fire: Ganon (Fire)
    ganon_water: Ganon (Water)
    ganon_shadow: Ganon (Shadow)
    ganon_spirit: Ganon (Spirit)
    """

    display_name = "Silver Rupee Pouches"

    valid_keys = {
        "dc",
        "botw",
        "spirit_child",
        "spirit_sun",
        "spirit_boulders",
        "spirit_lobby",
        "spirit_adult",
        "shadow_scythe",
        "shadow_pit",
        "shadow_spikes",
        "shadow_blades",
        "ic_scythe",
        "ic_block",
        "gtg_slopes",
        "gtg_lava",
        "gtg_water",
        "ganon_light",
        "ganon_forest",
        "ganon_fire",
        "ganon_water",
        "ganon_shadow",
        "ganon_spirit",
    }

    # condition: function (s) { return hasOoT(s) && s.silverRupeeShuffle !== 'vanilla'; }


class TownFairyShuffle(OoTMMChoice):
    """
    Controls where the Clock Town Stray Fairy can be

    Vanilla: The Clock Town Stray Fairy will be at its original location
    Anywhere: The Clock Town Stray Fairy can be found anywhere
    """

    display_name = "Town Stray Fairy Shuffle"

    option_vanilla = 0
    option_anywhere = 1

    default = 0

    display_names = [
        "Vanilla",
        "Anywhere",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class StrayFairyChestShuffle(OoTMMChoice):
    """
    Controls where the Dungeon Chest Stray Fairies can be

    Starting: Start with the fairies
    Vanilla: The Dungeon Chest Stray Fairies will be at their original locations
    Own Dungeon: All Dungeon Chest Stray Fairies are shuffled within their own dungeon
    Anywhere: All Dungeon Chest Stray Fairies are shuffled anywhere
    """

    display_name = "Dungeon Chest Fairy Shuffle"

    option_starting = 0
    option_vanilla = 1
    option_own_dungeon = 2
    option_anywhere = 3

    default = 0

    display_names = [
        "Starting",
        "Vanilla",
        "Own Dungeon",
        "Anywhere",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class StrayFairyOtherShuffle(OoTMMChoice):
    """
    Controls where the Dungeon Freestanding Stray Fairies can be

    Removed: Start with the fairies, and the bubbles are removed.
    Starting: Start with the fairies
    Vanilla: The Dungeon Freestanding Stray Fairies will be at their original locations
    Own Dungeon: All Dungeon Freestanding Stray Fairies are shuffled within their own dungeon
    Anywhere: All Dungeon Freestanding Stray Fairies are shuffled anywhere
    """

    display_name = "Dungeon Freestanding Fairy Shuffle"

    option_removed = 0
    option_starting = 1
    option_vanilla = 2
    option_own_dungeon = 3
    option_anywhere = 4

    default = 0

    display_names = [
        "Removed",
        "Starting",
        "Vanilla",
        "Own Dungeon",
        "Anywhere",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class GanonBossKey(OoTMMChoice):
    """
    Controls where Ganon Boss Key should be

    Removed: Ganon Boss Key is removed, and so is the lock on the door leading to Ganondorf
    Vanilla: Ganon Boss Key will be in its original chest, within Ganon's Castle
    Ganon's Castle: Ganon Boss Key will be anywhere within Ganon's Castle
    Anywhere: Ganon Boss Key can be found anywhere
    Custom:
    """

    display_name = "Ganon Boss Key Shuffle"

    option_removed = 0
    option_vanilla = 1
    option_ganon = 2
    option_anywhere = 3
    option_custom = 4

    default = 0

    display_names = [
        "Removed",
        "Vanilla",
        "Ganon's Castle",
        "Anywhere",
        "Custom",
    ]

    # condition: function (s) { return hasOoT(s) && s.goal !== 'triforce' && s.goal !== 'triforce3'; }


class DungeonRewardShuffle(OoTMMChoice):
    """
    Controls where the dungeons rewards should be

    Dungeon Blue Warps: Only the blue warps will grant the rewards
    Dungeons (Max one per dungeon): Anywhere in dungeons (one max)
    Dungeons (Unrestricted): Anywhere in dungeons
    Anywhere: Can be anywhere
    """

    display_name = "Dungeon Reward Shuffle"

    option_dungeon_blue_warps = 0
    option_dungeons_limited = 1
    option_dungeons = 2
    option_anywhere = 3

    default = 0

    display_names = [
        "Dungeon Blue Warps",
        "Dungeons (Max one per dungeon)",
        "Dungeons (Unrestricted)",
        "Anywhere",
    ]


class ScrubShuffleOot(Toggle):
    """
    Controls whether or not Business Scrubs are shuffled (OoT). If not, the one in Hyrule Field by Lake Hylia's fences, the one by the Bridge in Lost Woods, and the front one in the grotto near Sacred Forest Meadow will still be shuffled
    """

    display_name = "Scrub Shuffle (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ScrubShuffleMm(Toggle):
    """
    Controls whether or not Business Scrubs are shuffled (MM). If not, the one in Termina Field near the Observatory and the one in Goron Village will still be shuffled
    """

    display_name = "Scrub Shuffle (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class CowShuffleOot(Toggle):
    """
    Controls whether or not playing Epona's Song near cows will give an item (OOT)
    """

    display_name = "Cow Shuffle (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class CowShuffleMm(Toggle):
    """
    Controls whether or not playing Epona's Song near cows will give an item (MM)
    """

    display_name = "Cow Shuffle (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class ShopShuffleOot(OoTMMChoice):
    """
    Controls whether or not shops in OOT should have their items shuffled

    None: All the items are vanilla
    Full: All 8 items are shuffled
    """

    display_name = "Shop Shuffle (OoT)"

    option_none = 0
    option_full = 1

    default = 0

    display_names = [
        "None",
        "Full",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class ShopShuffleMm(OoTMMChoice):
    """
    Controls whether or not shops in MM should have their items shuffled. If not, the Bomb Bag purchases will still be shuffled

    None: All the items are vanilla
    Full: All 8 items are shuffled
    """

    display_name = "Shop Shuffle (MM)"

    option_none = 0
    option_full = 1

    default = 0

    display_names = [
        "None",
        "Full",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class OwlShuffle(OoTMMChoice):
    """
    Make owl statue items that can be shuffled.

    None: Owl statues are vanilla
    Anywhere: Owl statues are shuffled in the item pool
    """

    display_name = "Owl Statue Shuffle"

    option_none = 0
    option_anywhere = 1

    default = 0

    display_names = [
        "None",
        "Anywhere",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class ShufflePotsOot(Toggle):
    """
    Controls whether or not the pots are shuffled (OoT).
    """

    display_name = "Pots Shuffle (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ShufflePotsMm(Toggle):
    """
    Controls whether or not the pots are shuffled (MM).
    """

    display_name = "Pots Shuffle (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class ShuffleGrassOot(Toggle):
    """
    Controls whether or not the grass is shuffled (OoT)
    """

    display_name = "Grass Shuffle (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ShuffleGrassMm(Toggle):
    """
    Controls whether or not the grass is shuffled (MM)
    """

    display_name = "Grass Shuffle (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class ShuffleFreeRupeesOot(Toggle):
    """
    Controls whether or not the freestanding rupees are shuffled (OoT)
    """

    display_name = "Freestanding Rupees Shuffle (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ShuffleFreeRupeesMm(Toggle):
    """
    Controls whether or not the freestanding rupees are shuffled (MM)
    """

    display_name = "Freestanding Rupees Shuffle (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class ShuffleFreeHeartsOot(Toggle):
    """
    Controls whether or not the freestanding hearts are shuffled (OoT)
    """

    display_name = "Freestanding Hearts Shuffle (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ShuffleFreeHeartsMm(Toggle):
    """
    Controls whether or not the freestanding hearts are shuffled (MM)
    """

    display_name = "Freestanding Hearts Shuffle (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class ShuffleWonderItemsOot(Toggle):
    """
    Controls whether or not the wonder items are shuffled (OoT)
    """

    display_name = "Wonder Items Shuffle (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ShuffleWonderItemsMm(Toggle):
    """
    Controls whether or not the wonder items are shuffled (MM)
    """

    display_name = "Wonder Items Shuffle (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class ShuffleOcarinasOot(DefaultOnToggle):
    """
    Controls whether or not the two Ocarinas in OoT are shuffled
    """

    display_name = "Ocarina Shuffle (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ShuffleMasterSword(DefaultOnToggle):
    """
    Controls whether or not the Master Sword is shuffled
    """

    display_name = "Master Sword Shuffle"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ShuffleGerudoCard(DefaultOnToggle):
    """
    Controls whether or not the Gerudo Membership Card is shuffled
    """

    display_name = "Gerudo Card Shuffle"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ShuffleMerchantsMm(Toggle):
    """
    Controls whether or not the Milk Bar and Gorman milk purchases in MM are shuffled
    """

    display_name = "Merchants Shuffle (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class PondFishShuffle(Toggle):
    """
    Controls whether or not the Fish (and the Loaches) in the Fishing Pond are shuffled amongst all the items.
    """

    display_name = "Fishing Pond Fish Shuffle"

    # condition: function (x) { return hasGame(x, 'oot'); }


class DivingGameRupeeShuffle(Toggle):
    """
    Controls whether or not the Zora's Domain Diving Game has 5 random items instead of green, blue, red, purple and 500 rupees.
    """

    display_name = "Diving Game Rupee Shuffle"

    # condition: function (x) { return hasGame(x, 'oot'); }


class FairyFountainFairyShuffleOot(Toggle):
    """
    Controls whether or not fairies in fairy fountains are shuffled (OoT).
    """

    display_name = "Fairy Fountain Fairy Shuffle (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class FairyFountainFairyShuffleMm(Toggle):
    """
    Controls whether or not fairies in fairy fountains are shuffled (MM).
    """

    display_name = "Fairy Fountain Fairy Shuffle (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class FairySpotShuffleOot(Toggle):
    """
    Controls whether or not big fairies in fairy spots are shuffled (OoT). Play either Song of Storms or Sun's Song
    """

    display_name = "Fairy Spot Shuffle (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class EggShuffle(Toggle):
    """
    Fun setting: should using the Weird/Pocket Eggs give an item? If not, they're entirely removed from the game
    """

    display_name = "Weird / Pocket Egg Content Shuffle"

    # condition: function (x) { return hasGame(x, 'oot'); }


main_shuffle_options: dict[str, Option] = {
    "songs": Songs,
    "gold_skulltula_tokens": GoldSkulltulaTokens,
    "houses_skulltula_tokens": HousesSkulltulaTokens,
    "tingle_shuffle": TingleShuffle,
    "map_compass_shuffle": MapCompassShuffle,
    "small_key_shuffle_oot": SmallKeyShuffleOot,
    "small_key_shuffle_mm": SmallKeyShuffleMm,
    "small_key_shuffle_hideout": SmallKeyShuffleHideout,
    "small_key_shuffle_chest_game": SmallKeyShuffleChestGame,
    "boss_key_shuffle_oot": BossKeyShuffleOot,
    "boss_key_shuffle_mm": BossKeyShuffleMm,
    "small_key_ring_oot": SmallKeyRingOot,
    "small_key_ring_mm": SmallKeyRingMm,
    "silver_rupee_shuffle": SilverRupeeShuffle,
    "silver_rupee_pouches": SilverRupeePouches,
    "town_fairy_shuffle": TownFairyShuffle,
    "stray_fairy_chest_shuffle": StrayFairyChestShuffle,
    "stray_fairy_other_shuffle": StrayFairyOtherShuffle,
    "ganon_boss_key": GanonBossKey,
    "dungeon_reward_shuffle": DungeonRewardShuffle,
    "scrub_shuffle_oot": ScrubShuffleOot,
    "scrub_shuffle_mm": ScrubShuffleMm,
    "cow_shuffle_oot": CowShuffleOot,
    "cow_shuffle_mm": CowShuffleMm,
    "shop_shuffle_oot": ShopShuffleOot,
    "shop_shuffle_mm": ShopShuffleMm,
    "owl_shuffle": OwlShuffle,
    "shuffle_pots_oot": ShufflePotsOot,
    "shuffle_pots_mm": ShufflePotsMm,
    "shuffle_grass_oot": ShuffleGrassOot,
    "shuffle_grass_mm": ShuffleGrassMm,
    "shuffle_free_rupees_oot": ShuffleFreeRupeesOot,
    "shuffle_free_rupees_mm": ShuffleFreeRupeesMm,
    "shuffle_free_hearts_oot": ShuffleFreeHeartsOot,
    "shuffle_free_hearts_mm": ShuffleFreeHeartsMm,
    "shuffle_wonder_items_oot": ShuffleWonderItemsOot,
    "shuffle_wonder_items_mm": ShuffleWonderItemsMm,
    "shuffle_ocarinas_oot": ShuffleOcarinasOot,
    "shuffle_master_sword": ShuffleMasterSword,
    "shuffle_gerudo_card": ShuffleGerudoCard,
    "shuffle_merchants_mm": ShuffleMerchantsMm,
    "pond_fish_shuffle": PondFishShuffle,
    "diving_game_rupee_shuffle": DivingGameRupeeShuffle,
    "fairy_fountain_fairy_shuffle_oot": FairyFountainFairyShuffleOot,
    "fairy_fountain_fairy_shuffle_mm": FairyFountainFairyShuffleMm,
    "fairy_spot_shuffle_oot": FairySpotShuffleOot,
    "egg_shuffle": EggShuffle,
}

# category: main.prices


class PriceOotShops(OoTMMChoice):
    """
    Sets the price of items inside OoT shops

    Affordable: All prices are set to 10 rupees.
    Vanilla: All prices are set to their vanilla values.
    Weighted Random: All prices are randomized, but lower prices are favored.
    Random: All prices are randomized.
    """

    display_name = "OoT Shops Prices"

    option_affordable = 0
    option_vanilla = 1
    option_weighted = 2
    option_randomized = 3

    default = 0

    display_names = [
        "Affordable",
        "Vanilla",
        "Weighted Random",
        "Random",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class PriceOotScrubs(OoTMMChoice):
    """
    Sets the price of items sold by OoT scrubs

    Affordable: All prices are set to 10 rupees.
    Vanilla: All prices are set to their vanilla values.
    Weighted Random: All prices are randomized, but lower prices are favored.
    Random: All prices are randomized.
    """

    display_name = "OoT Scrubs Prices"

    option_affordable = 0
    option_vanilla = 1
    option_weighted = 2
    option_randomized = 3

    default = 0

    display_names = [
        "Affordable",
        "Vanilla",
        "Weighted Random",
        "Random",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class PriceMmShops(OoTMMChoice):
    """
    Sets the price of items sold inside MM shops

    Affordable: All prices are set to 10 rupees.
    Vanilla: All prices are set to their vanilla values.
    Weighted Random: All prices are randomized, but lower prices are favored.
    Random: All prices are randomized.
    """

    display_name = "MM Shops Prices"

    option_affordable = 0
    option_vanilla = 1
    option_weighted = 2
    option_randomized = 3

    default = 0

    display_names = [
        "Affordable",
        "Vanilla",
        "Weighted Random",
        "Random",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class PriceMmTingle(OoTMMChoice):
    """
    Sets the price of items sold by Tingle

    Affordable: All prices are set to 10 rupees.
    Vanilla: All prices are set to their vanilla values.
    Weighted Random: All prices are randomized, but lower prices are favored.
    Random: All prices are randomized.
    """

    display_name = "MM Tingle Prices"

    option_affordable = 0
    option_vanilla = 1
    option_weighted = 2
    option_randomized = 3

    default = 0

    display_names = [
        "Affordable",
        "Vanilla",
        "Weighted Random",
        "Random",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


main_prices_options: dict[str, Option] = {
    "price_oot_shops": PriceOotShops,
    "price_oot_scrubs": PriceOotScrubs,
    "price_mm_shops": PriceMmShops,
    "price_mm_tingle": PriceMmTingle,
}

# category: main.events


class GanonTrials(OptionSet):
    """
    Controls which trials in Ganon's Castle are enabled

    light: Light Trial
    forest: Forest Trial
    fire: Fire Trial
    water: Water Trial
    shadow: Shadow Trial
    spirit: Spirit Trial
    """

    display_name = "Ganon Trials"

    valid_keys = {
        "light",
        "forest",
        "fire",
        "water",
        "shadow",
        "spirit",
    }

    # condition: function (x) { return hasGame(x, 'oot'); }


class MoonCrash(OoTMMChoice):
    """
    Change the behavior of moon crashing

    Reset: Moon Crash will restore the last save. No progress will be kept.
    New Cycle: Moon Crash will initiate a new cycle, keeping progress. Saving is enabled on the Clock Tower Roof.
    """

    display_name = "Moon Crash Behavior"

    option_reset = 0
    option_cycle = 1

    default = 0

    display_names = [
        "Reset",
        "New Cycle",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class StartingAge(OoTMMChoice):
    """
    Choose the starting age

    Child: Link will start off as child
    Adult: Link will start off as adult
    Random: Link will start off as either adult or child, with a 50/50 probability
    """

    display_name = "Starting Age"

    option_child = 0
    option_adult = 1
    option_randomized = 2

    default = 0

    display_names = [
        "Child",
        "Adult",
        "Random",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class SwordlessAdult(Toggle):
    """
    Choose whether or not adult Link can be swordless
    """

    display_name = "Allow adult link to be swordless"

    # condition: function (x) { return hasGame(x, 'oot'); }


class TimeTravelSword(DefaultOnToggle):
    """
    Choose whether or not Link needs the Master Sword to travel through time
    """

    display_name = "Time Travel requires Master Sword"

    # condition: function (s) { return hasOoT(s) && s.swordlessAdult; }


class DoorOfTime(OoTMMChoice):
    """
    Alters the Door of Time state

    Closed: The Door will be closed, and you will need to play Song of Time in front of the Temple of Time altar to open it. (The Spiritual Stones and Ocarina of Time are NOT needed)
    Open: The Door is already open
    """

    display_name = "Door of Time"

    option_closed = 0
    option_open = 1

    default = 0

    display_names = [
        "Closed",
        "Open",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class AgeChange(OoTMMChoice):
    """
    Allows you to switch ages by playing Song of Time, if you've been to Temple of Time as both ages

    None: Cannot change age by playing Song of Time.
    Ocarina of Time: Can change age by playing Song of Time with the Ocarina of Time specifically.
    Always: Can always change age by playing Song of Time.
    """

    display_name = "Age Change upon Song of Time"

    option_none = 0
    option_oot = 1
    option_always = 2

    default = 0

    display_names = [
        "None",
        "Ocarina of Time",
        "Always",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class DekuTree(OoTMMChoice):
    """
    Controls the behavior of Mido blocking the Deku Tree as child

    Closed: Mido will block the way to the Deku Tree until you have a Deku Shield and the Kokiri Sword.
    Vanilla: Mido will block the way to the Deku Tree, but the tree itself will be open as child.
    Open: Mido will not block the way, the Deku Tree will be open from the start
    """

    display_name = "Deku Tree"

    option_closed = 0
    option_vanilla = 1
    option_open = 2

    default = 0

    display_names = [
        "Closed",
        "Vanilla",
        "Open",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class OpenDungeonsOot(OptionSet):
    """
    Opens the entrance to the chosen dungeons

    dekutreeadult: Deku Tree as Adult
    welladult: Bottom of the Well as Adult
    firechild: Fire Temple as Child
    dc: Dodongo's Cavern
    botw: Bottom of the Well
    jj: Jabu-Jabu
    shadow: Shadow Temple
    water: Water Temple
    """

    display_name = "Open Dungeons (OoT)"

    valid_keys = {
        "dekutreeadult",
        "welladult",
        "firechild",
        "dc",
        "botw",
        "jj",
        "shadow",
        "water",
    }

    # condition: function (x) { return hasGame(x, 'oot'); }


class OpenDungeonsMm(OptionSet):
    """
    Controls whether or not MM dungeons will need their respective song. Takes priority over Clear State

    wf: Woodfall Temple
    sh: Snowhead Temple
    gb: Great Bay Temple
    st: Stone Tower Temples
    """

    display_name = "Open Dungeons (MM)"

    valid_keys = {
        "wf",
        "sh",
        "gb",
        "st",
    }

    # condition: function (x) { return hasGame(x, 'mm'); }


class ClearStateDungeonsMm(OoTMMChoice):
    """
    Controls whether or not MM dungeons will need their respectives songs in the cleared state
    """

    display_name = "Clear State Dungeons (MM)"

    option_none = 0
    option_wf = 1
    option_gb = 2
    option_both = 3

    default = 0

    display_names = [
        "None",
        "Woodfall Temple",
        "Great Bay Temple",
        "Both",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class KakarikoGate(OoTMMChoice):
    """
    Controls the behavior of the gate in Kakariko blocking Death Mountain as child

    Closed: The gate will be closed until you show Zelda's Letter to the guard
    Open: The gate will be open from the start
    """

    display_name = "Kakariko Gate"

    option_closed = 0
    option_open = 1

    default = 0

    display_names = [
        "Closed",
        "Open",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class OpenZdShortcut(Toggle):
    """
    Removes the ice blocking Zora's Domain in Lake Hylia as adult
    """

    display_name = "Open Zora's Domain Shortcut"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ZoraKing(OoTMMChoice):
    """
    Controls the behavior of King Zora in Zora's Domain

    Vanilla: You will need to present him Ruto's Letter in order to enter Zora's Fountain as both Child and Adult
    Open (Adult Only): Already on the side as Adult, granting free Zora's Fountain access. Child still needs Ruto's Letter
    Open: He will already be on the side for both Child and Adult, and Ruto's Letter is replaced by an empty bottle
    """

    display_name = "King Zora"

    option_vanilla = 0
    option_adult = 1
    option_open = 2

    default = 0

    display_names = [
        "Vanilla",
        "Open (Adult Only)",
        "Open",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class GerudoFortress(OoTMMChoice):
    """
    Controls the behavior of the Carpenters in Gerudo Fortress

    Vanilla: You will need to rescue all carpenters.
    One Carpenter: You will need to rescue only one carpenter.
    Open: Carpenters are rescued from the start and the bridge in Gerudo Valley as adult is repaired.
    """

    display_name = "Gerudo Fortress"

    option_vanilla = 0
    option_single = 1
    option_open = 2

    default = 0

    display_names = [
        "Vanilla",
        "One Carpenter",
        "Open",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class SkipZelda(Toggle):
    """
    This changes the beginning of the child trade quest. True means you'll start having already met Zelda and got her item along with the one from Impa. The Chicken is also removed from the game, but Malon will still be at Hyrule Castle
    """

    display_name = "Skip Child Zelda"

    # condition: function (x) { return hasGame(x, 'oot'); }


class OpenMoon(Toggle):
    """
    Skip playing Oath to Order to reach the Moon.
    """

    display_name = "Skip Oath to Order"

    # condition: function (x) { return hasGame(x, 'mm'); }


class Lacs(OoTMMChoice):
    """
    Controls how the Light Arrow Cutscene should be triggered

    Vanilla: Triggers at Temple of Time with Shadow and Spirit Medallions
    Custom: Triggers at Temple of Time with a special condition
    """

    display_name = "Light Arrow Cutscene"

    option_vanilla = 0
    option_custom = 1

    default = 0

    display_names = [
        "Vanilla",
        "Custom",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class RainbowBridge(OoTMMChoice):
    """
    Controls how the Rainbow Bridge should be triggered

    Open: The Rainbow Bridge is always open
    Vanilla: Opens when you have the Light Arrows, Shadow Medallion, and Spirit Medallion
    Medallions: Opens when you have all Medallions
    Custom: You will need to meet a special condition to open the bridge
    """

    display_name = "Rainbow Bridge"

    option_open = 0
    option_vanilla = 1
    option_medallions = 2
    option_custom = 3

    default = 0

    display_names = [
        "Open",
        "Vanilla",
        "Medallions",
        "Custom",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class MajoraChild(OoTMMChoice):
    """
    Controls the requirements to enter Majora's arena

    None: As soon as you have access to the Moon you can enter Majora's arena
    Custom: You will need to meet a special condition to enter Majora's arena
    """

    display_name = "Majora Child Requirements"

    option_none = 0
    option_custom = 1

    default = 0

    display_names = [
        "None",
        "Custom",
    ]

    # condition: function (s) { return hasMM(s) && s.goal !== 'triforce' && s.goal !== 'triforce3'; }


class BossWarpPads(OoTMMChoice):
    """
    Controls the behavior of the MM Boss Warp Pads.

    Boss Beaten: Enabled when the boss is beaten
    Remains: Enabled when the matching remain is obtained
    """

    display_name = "Boss Warp Pads"

    option_boss_beaten = 0
    option_remains = 1

    default = 0

    display_names = [
        "Boss Beaten",
        "Remains",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class FreeScarecrowOot(Toggle):
    """
    Allows to spawn Pierre the Scarecrow just by pulling the Ocarina out
    """

    display_name = "Free Scarecrow (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class FreeScarecrowMm(Toggle):
    """
    Allows to spawn the Scarecrow just by pulling the Ocarina out
    """

    display_name = "Free Scarecrow (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class PreCompletedDungeons(Toggle):
    """
    Allow dungeons to be pre-completed depending on rules.
    """

    display_name = "Pre-Completed Dungeons"

    # condition: function (s) { return (s.mode !== 'multi' || s.distinctWorlds); }


class PreCompletedDungeonsMajor(Range):
    """
    How many major dungeons sould be pre-completed. Can be combined with other pre-completed dungeon rules.
    """

    display_name = "Pre-Completed Dungeons (Major)"

    range_start = 0
    range_end = 12

    default = 0

    # condition: function (s) { return s.preCompletedDungeons; }


class PreCompletedDungeonsStones(Range):
    """
    Pre-completes dungeons containing at least one stone, until it reaches that many stones. Can be combined with other pre-completed dungeon rules.
    """

    display_name = "Pre-Completed Dungeons (Stones)"

    range_start = 0
    range_end = 3

    default = 0

    # condition: function (s) { return hasOoT(s) && s.preCompletedDungeons; }


class PreCompletedDungeonsMedallions(Range):
    """
    Pre-completes dungeons containing at least one medallion, until it reaches that many medallions. Can be combined with other pre-completed dungeon rules.
    """

    display_name = "Pre-Completed Dungeons (Medallions)"

    range_start = 0
    range_end = 6

    default = 0

    # condition: function (s) { return hasOoT(s) && s.preCompletedDungeons; }


class PreCompletedDungeonsRemains(Range):
    """
    Pre-completes dungeons containing at least one remain, until in reaches that many remains. Can be combined with other pre-completed dungeon rules.
    """

    display_name = "Pre-Completed Dungeons (Remains)"

    range_start = 0
    range_end = 4

    default = 0

    # condition: function (s) { return hasMM(s) && s.preCompletedDungeons; }


class OpenMaskShop(Toggle):
    """
    Makes the Mask Shop in Market open during the night
    """

    display_name = "Open Mask Shop at night"

    # condition: function (x) { return x.games === 'ootmm'; }


class OotPreplantedBeans(Toggle):
    """
    Automatically plants beans for
    """

    display_name = "Pre-Planted beans (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


main_events_options: dict[str, Option] = {
    "ganon_trials": GanonTrials,
    "moon_crash": MoonCrash,
    "starting_age": StartingAge,
    "swordless_adult": SwordlessAdult,
    "time_travel_sword": TimeTravelSword,
    "door_of_time": DoorOfTime,
    "age_change": AgeChange,
    "deku_tree": DekuTree,
    "open_dungeons_oot": OpenDungeonsOot,
    "open_dungeons_mm": OpenDungeonsMm,
    "clear_state_dungeons_mm": ClearStateDungeonsMm,
    "kakariko_gate": KakarikoGate,
    "open_zd_shortcut": OpenZdShortcut,
    "zora_king": ZoraKing,
    "gerudo_fortress": GerudoFortress,
    "skip_zelda": SkipZelda,
    "open_moon": OpenMoon,
    "lacs": Lacs,
    "rainbow_bridge": RainbowBridge,
    "majora_child": MajoraChild,
    "boss_warp_pads": BossWarpPads,
    "free_scarecrow_oot": FreeScarecrowOot,
    "free_scarecrow_mm": FreeScarecrowMm,
    "pre_completed_dungeons": PreCompletedDungeons,
    "pre_completed_dungeons_major": PreCompletedDungeonsMajor,
    "pre_completed_dungeons_stones": PreCompletedDungeonsStones,
    "pre_completed_dungeons_medallions": PreCompletedDungeonsMedallions,
    "pre_completed_dungeons_remains": PreCompletedDungeonsRemains,
    "open_mask_shop": OpenMaskShop,
    "oot_preplanted_beans": OotPreplantedBeans,
}

# category: main.cross


class CrossAge(Toggle):
    """
    When you enter MM as Adult Link, you will be Adult Link in MM.
    """

    display_name = "Cross-Games Age"

    # condition: function (x) { return x.games === 'ootmm'; }


class CrossWarpOot(Toggle):
    """
    Allows you to play OOT Warp Songs from MM to warp to their respective locations. Logic could even expect you to do so
    """

    display_name = "Cross-Games OoT Warp Songs"

    # condition: function (x) { return x.games === 'ootmm'; }


class CrossWarpMm(OoTMMChoice):
    """
    Controls whether you can play Song of Soaring from OOT to warp to MM Owl Statues and how logic should be affected

    None: Song of Soaring is fully disabled in OOT
    Child Only: Song of Soaring in OOT is enabled and logical only for Child
    Child & Adult: Song of Soaring in OOT is enabled and logical for both Child and Adult
    """

    display_name = "Cross-Games MM Song of Soaring"

    option_none = 0
    option_child_only = 1
    option_full = 2

    default = 0

    display_names = [
        "None",
        "Child Only",
        "Child & Adult",
    ]

    # condition: function (x) { return x.games === 'ootmm'; }


class CrossGameFw(Toggle):
    """
    Controls whether you can use Farore's Wind to warp between OOT and MM.
    """

    display_name = "Cross-Games Farore's Wind"

    # condition: function (x) { return hasOoTMM(x) && x.spellWindMm; }


main_cross_options: dict[str, Option] = {
    "cross_age": CrossAge,
    "cross_warp_oot": CrossWarpOot,
    "cross_warp_mm": CrossWarpMm,
    "cross_game_fw": CrossGameFw,
}

# category: main.misc


class Csmc(OoTMMChoice):
    """
    Modifies the chest, grass, and pot appearance so that they match their content. Works for unique items, keys, fairies, and souls. Grass and pots will otherwise always be gold if the item has not been collected

    Never: Containers will be vanilla
    Stone of Agony: Containers will match content when you have the Stone of Agony in OoT
    Always: Containers will always match content
    """

    display_name = "Container Appearance Matches Content"

    option_never = 0
    option_agony = 1
    option_always = 2

    default = 0

    display_names = [
        "Never",
        "Stone of Agony",
        "Always",
    ]


class CsmcHearts(DefaultOnToggle):
    """
    Use a specific texture for heart pieces/containers
    """

    display_name = "CAMC for Heart Pieces/Containers"

    # condition: function (x) { return x.csmc !== 'never'; }


class CsmcExtra(Toggle):
    """
    Enables CAMC for shuffled Gold, Swamp, and Ocean Skulltulas
    """

    display_name = "Skulltula CAMC"

    # condition: function (x) { return x.csmc !== 'never'; }


class BlastMaskCooldown(OoTMMChoice):
    """
    Changes the cooldown between each explostion of the Blast Mask
    """

    display_name = "Blast Mask Cooldown"

    option_instant = 0
    option_veryshort = 1
    option_short = 2
    option_default = 3
    option_long = 4
    option_verylong = 5

    default = 0

    display_names = [
        "Instant (0s)",
        "Very Short (~2s)",
        "Short (~6s)",
        "Default (~15s)",
        "Long (~25s)",
        "Very Long (~51s)",
    ]

    # condition: function (s) { return hasMM(s) || s.blastMaskOot; }


class ClockSpeed(OoTMMChoice):
    """
    Alters the speed of the clock. Some options may render seeds unbeatable due to being unable to do time-related checks

    Very Slow: The time will flow 66% slower than usual
    Slow: The time will flow 33% slower than usual
    Default: The normal clock speed
    Fast: The clock speed will twice as fast than usual
    Very Fast: USE AT OWN RISK!! - The clock speed will be 3x faster than usual, even on inverted
    Super Fast: USE AT OWN RISK!! - The clock speed will be 6x faster than usual, even on inverted
    """

    display_name = "Clock Speed"

    option_veryslow = 0
    option_slow = 1
    option_default = 2
    option_fast = 3
    option_veryfast = 4
    option_superfast = 5

    default = 0

    display_names = [
        "Very Slow",
        "Slow",
        "Default",
        "Fast",
        "Very Fast",
        "Super Fast",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class AutoInvert(OoTMMChoice):
    """
    Auto-inverts time at the start of a cycle
    """

    display_name = "Auto-Invert Time (MM)"

    option_never = 0
    option_first_cycle = 1
    option_always = 2

    default = 0

    display_names = [
        "Never",
        "First Cycle",
        "Always",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class KeepItemsReset(Toggle):
    """
    Keep items through a cycle reset
    """

    display_name = "Keep Items on Cycle Reset"

    # condition: function (x) { return hasGame(x, 'mm'); }


class FastMasks(Toggle):
    """
    Makes the mask transitions very fast
    """

    display_name = "Fast Form Transitions"

    # condition: function (x) { return hasGame(x, 'mm'); }


class FierceDeityAnywhere(Toggle):
    """
    Controls the ability to use Fierce Deity outside of boss lairs. No logical applications
    """

    display_name = "Fierce Deity Anywhere in MM"

    # condition: function (x) { return hasGame(x, 'mm'); }


class HookshotAnywhereOot(OoTMMChoice):
    """
    Modifies all surfaces to be hooked onto and if it is expected in logic
    """

    display_name = "Hookshot Anywhere (OoT)"

    option_off = 0
    option_enabled = 1
    option_logical = 2

    default = 0

    display_names = [
        "Off",
        "On",
        "Logical",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class HookshotAnywhereMm(OoTMMChoice):
    """
    Modifies all surfaces to be hooked onto and if it is expected in logic
    """

    display_name = "Hookshot Anywhere (MM)"

    option_off = 0
    option_enabled = 1
    option_logical = 2

    default = 0

    display_names = [
        "Off",
        "On",
        "Logical",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class ClimbMostSurfacesOot(OoTMMChoice):
    """
    Modifies most surface to be climbable and if it is expected in logic
    """

    display_name = "Climb Most Surfaces (OoT)"

    option_off = 0
    option_enabled = 1
    option_logical = 2

    default = 0

    display_names = [
        "Off",
        "On",
        "Logical",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class ClimbMostSurfacesMm(Toggle):
    """
    Modifies most surface to be climbable
    """

    display_name = "Climb Most Surfaces (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class FastBunnyHood(DefaultOnToggle):
    """
    Modifies the Bunny Hood in OoT to give a speed increase
    """

    display_name = "Fast Bunny Hood"

    # condition: function (x) { return hasGame(x, 'oot'); }


class CritWiggleDisable(DefaultOnToggle):
    """
    Disables the camera zoom-in and weird movements when low on health
    """

    display_name = "Disable Crit Wiggle"


class RestoreBrokenActors(Toggle):
    """
    In vanilla OoT, some actors fails to load properly in some rooms due to errors in the room files. When this is on, these actors will load.
    """

    display_name = "Restore Broken Actors"

    # condition: function (x) { return hasGame(x, 'oot'); }


class AlterLostWoodsExits(Toggle):
    """
    There are unused exits in the Lost Woods that return you to the lost woods. When this is on, all the "got lost" exits in the Lost Woods that would normally take you to Kokiri Forest instead take you back to the Lost Woods, keeping your compass direction intact.
    """

    display_name = "Alter Lost Woods Exits"

    # condition: function (x) { return hasGame(x, 'oot'); }


class VoidWarpMm(Toggle):
    """
    In vanilla OoT, various code only checks for transitionTrigger, but in MM it also checks for transitionMode. When this is on, MM will no longer check transitionMode in those circumstances.
    """

    display_name = "Void Warp in MM"

    # condition: function (x) { return hasGame(x, 'mm'); }


main_misc_options: dict[str, Option] = {
    "csmc": Csmc,
    "csmc_hearts": CsmcHearts,
    "csmc_extra": CsmcExtra,
    "blast_mask_cooldown": BlastMaskCooldown,
    "clock_speed": ClockSpeed,
    "auto_invert": AutoInvert,
    "keep_items_reset": KeepItemsReset,
    "fast_masks": FastMasks,
    "fierce_deity_anywhere": FierceDeityAnywhere,
    "hookshot_anywhere_oot": HookshotAnywhereOot,
    "hookshot_anywhere_mm": HookshotAnywhereMm,
    "climb_most_surfaces_oot": ClimbMostSurfacesOot,
    "climb_most_surfaces_mm": ClimbMostSurfacesMm,
    "fast_bunny_hood": FastBunnyHood,
    "crit_wiggle_disable": CritWiggleDisable,
    "restore_broken_actors": RestoreBrokenActors,
    "alter_lost_woods_exits": AlterLostWoodsExits,
    "void_warp_mm": VoidWarpMm,
}

main_options: dict[str, Option] = {
    "games": Games,
    "goal": Goal,
    "triforce_goal": TriforceGoal,
    "triforce_pieces": TriforcePieces,
    "item_pool": ItemPool,
    **main_shuffle_options,
    **main_prices_options,
    **main_events_options,
    **main_cross_options,
    **main_misc_options,
}

# category: hints


class ProbabilisticFoolish(DefaultOnToggle):
    """
    If you don't know what this is, leave it ON
    """

    display_name = "Probabilistic Foolish Hints"


class ExtraHintRegions(Toggle):
    """
    Make the region hints more granular: Makes Goron Racetrack and Butler Race into their own regions, and splits Ganon Castle/Tower and Normal/Inverted Stone Tower Temple.
    """

    display_name = "Extra Hint Regions"


class HintImportance(Toggle):
    """
    Hints will tell if an item is foolish, sometimes required, or always required
    """

    display_name = "Hint Importance"


hints_options: dict[str, Option] = {
    "probabilistic_foolish": ProbabilisticFoolish,
    "extra_hint_regions": ExtraHintRegions,
    "hint_importance": HintImportance,
}

# category: items

# category: items.extensions


class FillWallets(Toggle):
    """
    Fills the wallet upon finding a new one
    """

    display_name = "Fill Wallets"


class BottleContentShuffle(Toggle):
    """
    Randomize the content of the bottles
    """

    display_name = "Random Bottle Contents"


class SunSongMm(Toggle):
    """
    Enables Sun's Song as an item in MM. If Songs are on Songs, you must share or start with at least one song
    """

    display_name = "Sun's Song in MM"

    # condition: function (x) { return hasGame(x, 'mm'); }


class FairyOcarinaMm(Toggle):
    """
    Functionally identical as the Ocarina of Time, but now there's 2 Ocarinas for Majora's Mask!
    """

    display_name = "Fairy Ocarina in MM"

    # condition: function (x) { return hasGame(x, 'mm'); }


class BlueFireArrows(Toggle):
    """
    Gives the OOT Ice Arrows the properties of Blue Fire
    """

    display_name = "Blue Fire Arrows"

    # condition: function (x) { return hasGame(x, 'oot'); }


class SunlightArrows(Toggle):
    """
    Gives the OOT Light Arrows the ability to activate most sun switches
    """

    display_name = "Sunlight Arrows"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ShortHookshotMm(Toggle):
    """
    Adds a short hookshot in MM (logic accounts for this). A trick is also there for some of the harder spots
    """

    display_name = "Short Hookshot in MM"

    # condition: function (x) { return hasGame(x, 'mm'); }


class ChildWallets(Toggle):
    """
    Shuffles the starting Wallets... making it so you have to find it to hold anything!
    """

    display_name = "Child Wallets"


class ColossalWallets(Toggle):
    """
    Adds a Wallet that can hold up to 999 rupees in each game
    """

    display_name = "Colossal Wallets"


class BottomlessWallets(Toggle):
    """
    Adds a Wallet that can hold up to 9999 rupees in each game
    """

    display_name = "Bottomless Wallets"

    # condition: function (s) { return s.colossalWallets; }


class RupeeScaling(Toggle):
    """
    Makes rupees worth twice as much with the Colossal Wallet, and twenty times as much with the Bottomless Wallet.
    """

    display_name = "Rupee Scaling"

    # condition: function (s) { return s.colossalWallets; }


class SkeletonKeyOot(Toggle):
    """
    Adds a Skeleton Key that can open every small-key-locked door.
    """

    display_name = "Skeleton Key (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class SkeletonKeyMm(Toggle):
    """
    Adds a Skeleton Key that can open every small-key-locked door.
    """

    display_name = "Skeleton Key (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class MagicalRupee(Toggle):
    """
    Adds a Magical Rupee that can trigger every silver-rupee event.
    """

    display_name = "Magical Rupee"

    # condition: function (s) { return s.silverRupeeShuffle !== 'vanilla'; }


class BombchuBagOot(Toggle):
    """
    Turns the first out-of-shop bombchu pack you find into the bombchu bag. Has logical implications.
    """

    display_name = "Bombchu Bag (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class BombchuBagMm(Toggle):
    """
    Turns the first out-of-shop bombchu pack you find into the bombchu bag. Has logical implications.
    """

    display_name = "Bombchu Bag (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class SpellFireMm(Toggle):
    """
    Adds Din's Fire in Majora's Mask.
    """

    display_name = "Din's Fire (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class SpellWindMm(Toggle):
    """
    Adds Farore's Wind in Majora's Mask.
    """

    display_name = "Farore's Wind (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class SpellLoveMm(Toggle):
    """
    Adds Nayru's Love in Majora's Mask.
    """

    display_name = "Nayru's Love (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class BootsIronMm(Toggle):
    """
    Adds Iron Boots in Majora's Mask.
    """

    display_name = "Iron Boots (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class BootsHoverMm(Toggle):
    """
    Adds Hover Boots in Majora's Mask.
    """

    display_name = "Hover Boots (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class TunicGoronMm(Toggle):
    """
    Adds Goron Tunic in Majora's Mask.
    """

    display_name = "Goron Tunic (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class TunicZoraMm(Toggle):
    """
    Adds Zora Tunic in Majora's Mask.
    """

    display_name = "Zora Tunic (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class ScalesMm(Toggle):
    """
    Adds Silver Scale and Golden Scale in Majora's Mask.
    """

    display_name = "Scales (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class StrengthMm(Toggle):
    """
    Adds Goron's Bracelet, Silver Gauntlets, and Golden Gauntlets in Majora's Mask.
    """

    display_name = "Strength (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class ExtraChildSwordsOot(Toggle):
    """
    Add the various Majora's Mask swords in OoT, as upgrades to the kokiri sword.
    """

    display_name = "Extra Child Swords (OoT)"

    # condition: function (x) { return x.progressiveSwordsOot !== 'progressive' && hasOoT(x); }


class BlastMaskOot(Toggle):
    """
    Add the Blast Mask in Ocarina of Time.
    """

    display_name = "Blast Mask (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class StoneMaskOot(Toggle):
    """
    Add the Stone Mask in Ocarina of Time.
    """

    display_name = "Stone Mask (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class ElegyOot(Toggle):
    """
    Add the Elegy of Emptiness in Ocarina of Time.
    """

    display_name = "Elegy of Emptiness (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class OcarinaButtonsShuffleOot(Toggle):
    """
    Adds the Ocarina Buttons as items that are shuffled.
    """

    display_name = "Ocarina Buttons Shuffle (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class OcarinaButtonsShuffleMm(Toggle):
    """
    Adds the Ocarina Buttons as items that are shuffled.
    """

    display_name = "Ocarina Buttons Shuffle (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class SoulsEnemyOot(Toggle):
    """
    Add enemy souls into the item pool. Enemies won't spawn unless their soul is obtained.
    """

    display_name = "Enemy Souls (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class SoulsEnemyMm(Toggle):
    """
    Add enemy souls into the item pool. Enemies won't spawn unless their soul is obtained.
    """

    display_name = "Enemy Souls (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class SoulsBossOot(Toggle):
    """
    Add boss souls into the item pool. Enemies won't spawn unless their soul is obtained.
    """

    display_name = "Boss Souls (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class SoulsBossMm(Toggle):
    """
    Add boss souls into the item pool. Enemies won't spawn unless their soul is obtained.
    """

    display_name = "Boss Souls (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class SoulsNpcOot(Toggle):
    """
    Add NPC souls into the item pool. NPCs won't spawn unless their soul is obtained.
    """

    display_name = "NPC Souls (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class SoulsNpcMm(Toggle):
    """
    Add NPC souls into the item pool. NPCs won't spawn unless their soul is obtained.
    """

    display_name = "NPC Souls (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class SoulsMiscOot(Toggle):
    """
    Add misc. souls into the item pool. Corresponding actors won't spawn unless their soul is obtained.
    """

    display_name = "Misc. Souls (OoT)"

    # condition: function (x) { return hasGame(x, 'oot'); }


class SoulsMiscMm(Toggle):
    """
    Add misc. souls into the item pool. Corresponding actors won't spawn unless their soul is obtained.
    """

    display_name = "Misc. Souls (MM)"

    # condition: function (x) { return hasGame(x, 'mm'); }


class Clocks(Toggle):
    """
    Add items representing every Majora's Mask half day into the pool. The moon will crash early unless you collect these items.
    """

    display_name = "Clocks as Items"

    # condition: function (x) { return hasGame(x, 'mm'); }


class LenientSpikes(DefaultOnToggle):
    """
    Goron spikes can charge midair and keep their charge. Minimum speed for goron spikes is removed.
    """

    display_name = "Lenient Goron Spikes"

    # condition: function (x) { return hasGame(x, 'mm'); }


class MenuNotebook(Toggle):
    """
    Locks the in-game tracker behind the Bombers' Notebook
    """

    display_name = "Bombers' Tracker"

    # condition: function (x) { return hasGame(x, 'mm'); }


class Coins(Toggle):
    """
    Enable the leftover coin items. These can be used for special conds
    """

    display_name = "Coins"


class CoinsRed(Range):
    """
    How many Red Coins to add to the item pool
    """

    display_name = "Red Coins"

    range_start = 0
    range_end = 999

    default = 0

    # condition: function (s) { return s.coins; }


class CoinsGreen(Range):
    """
    How many Green Coins to add to the item pool
    """

    display_name = "Green Coins"

    range_start = 0
    range_end = 999

    default = 0

    # condition: function (s) { return s.coins; }


class CoinsBlue(Range):
    """
    How many Blue Coins to add to the item pool
    """

    display_name = "Blue Coins"

    range_start = 0
    range_end = 999

    default = 0

    # condition: function (s) { return s.coins; }


class CoinsYellow(Range):
    """
    How many Yellow Coins to add to the item pool
    """

    display_name = "Yellow Coins"

    range_start = 0
    range_end = 999

    default = 0

    # condition: function (s) { return s.coins; }


class TrapRupoor(Toggle):
    """
    Add rupoors to the item pool. They remove 10 rupees when collected
    """

    display_name = "Rupoors"


items_extensions_options: dict[str, Option] = {
    "fill_wallets": FillWallets,
    "bottle_content_shuffle": BottleContentShuffle,
    "sun_song_mm": SunSongMm,
    "fairy_ocarina_mm": FairyOcarinaMm,
    "blue_fire_arrows": BlueFireArrows,
    "sunlight_arrows": SunlightArrows,
    "short_hookshot_mm": ShortHookshotMm,
    "child_wallets": ChildWallets,
    "colossal_wallets": ColossalWallets,
    "bottomless_wallets": BottomlessWallets,
    "rupee_scaling": RupeeScaling,
    "skeleton_key_oot": SkeletonKeyOot,
    "skeleton_key_mm": SkeletonKeyMm,
    "magical_rupee": MagicalRupee,
    "bombchu_bag_oot": BombchuBagOot,
    "bombchu_bag_mm": BombchuBagMm,
    "spell_fire_mm": SpellFireMm,
    "spell_wind_mm": SpellWindMm,
    "spell_love_mm": SpellLoveMm,
    "boots_iron_mm": BootsIronMm,
    "boots_hover_mm": BootsHoverMm,
    "tunic_goron_mm": TunicGoronMm,
    "tunic_zora_mm": TunicZoraMm,
    "scales_mm": ScalesMm,
    "strength_mm": StrengthMm,
    "extra_child_swords_oot": ExtraChildSwordsOot,
    "blast_mask_oot": BlastMaskOot,
    "stone_mask_oot": StoneMaskOot,
    "elegy_oot": ElegyOot,
    "ocarina_buttons_shuffle_oot": OcarinaButtonsShuffleOot,
    "ocarina_buttons_shuffle_mm": OcarinaButtonsShuffleMm,
    "souls_enemy_oot": SoulsEnemyOot,
    "souls_enemy_mm": SoulsEnemyMm,
    "souls_boss_oot": SoulsBossOot,
    "souls_boss_mm": SoulsBossMm,
    "souls_npc_oot": SoulsNpcOot,
    "souls_npc_mm": SoulsNpcMm,
    "souls_misc_oot": SoulsMiscOot,
    "souls_misc_mm": SoulsMiscMm,
    "clocks": Clocks,
    "lenient_spikes": LenientSpikes,
    "menu_notebook": MenuNotebook,
    "coins": Coins,
    "coins_red": CoinsRed,
    "coins_green": CoinsGreen,
    "coins_blue": CoinsBlue,
    "coins_yellow": CoinsYellow,
    "trap_rupoor": TrapRupoor,
}

# category: items.progressive


class ProgressiveShieldsOot(OoTMMChoice):
    """
    Alters OOT Shields behavior

    Separate: They can be found independently from each other
    Progressive: Each Progressive Shield will grant you the next one: Deku Shield -> Hylian Shield -> Mirror Shield. Other Deku and Hylian Shields do not count towards this chain, only the Progressive Shield item.
    """

    display_name = "OoT Shields"

    option_separate = 0
    option_progressive = 1

    default = 0

    display_names = [
        "Separate",
        "Progressive",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class ProgressiveSwordsOot(OoTMMChoice):
    """
    Alters OOT Swords behavior

    Separate: They can be found independently from each other
    Progressive Knife and Biggoron: Kokiri Sword and Master Sword are independent. However Giant's Knife and Biggoron Sword are progressive.
    Progressive: Each Progressive Sword will grant you the next one: Kokiri Sword -> Master Sword -> Giant's Knife -> Biggoron Sword
    """

    display_name = "OoT Swords"

    option_separate = 0
    option_goron = 1
    option_progressive = 2

    default = 0

    display_names = [
        "Separate",
        "Progressive Knife and Biggoron",
        "Progressive",
    ]

    # condition: function (x) { return hasGame(x, 'oot'); }


class ProgressiveShieldsMm(OoTMMChoice):
    """
    Alters MM Shields behavior

    Separate: They can be found independently from each other
    Progressive: Each Progressive Shield will grant you the next one: Hero Shield -> Mirror Shield. Other Hero Shields do not count towards this chain, only the Progressive Shield item. If shields are shared, Hero Shield will be obtained alongside Hylian Shield
    """

    display_name = "MM Shields"

    option_separate = 0
    option_progressive = 1

    default = 0

    display_names = [
        "Separate",
        "Progressive",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class ProgressiveGFS(OoTMMChoice):
    """
    Controls whether Great Fairy Sword is included in sword progression
    """

    display_name = "MM Great Fairy Sword"

    option_separate = 0
    option_progressive = 1

    default = 0

    display_names = [
        "Separate",
        "Progressive",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class ProgressiveGoronLullaby(OoTMMChoice):
    """
    Alters the behavior of Goron Lullaby

    Full Lullaby Only: Only the Goron Lullaby can be found, and when playing with Songs on Song Locations, Baby Goron in MM is no longer a Song Location
    Progressive: Lullaby Intro will be received first before getting the full song
    """

    display_name = "MM Goron Lullaby"

    option_single = 0
    option_progressive = 1

    default = 0

    display_names = [
        "Full Lullaby Only",
        "Progressive",
    ]

    # condition: function (x) { return hasGame(x, 'mm'); }


class ProgressiveClocks(OoTMMChoice):
    """
    Alters the behavior of Clocks

    Separate: Clocks will be independant of each other. If you don	 select a starting clock, one will be given to you at random.
    Ascending: Clocks will be received in ascending order.
    Descending : Clocks will be received in descending order.
    """

    display_name = "Clocks"

    option_separate = 0
    option_ascending = 1
    option_descending = 2

    default = 0

    display_names = [
        "Separate",
        "Ascending",
        "Descending ",
    ]

    # condition: function (s) { return s.clocks; }


items_progressive_options: dict[str, Option] = {
    "progressive_shields_oot": ProgressiveShieldsOot,
    "progressive_swords_oot": ProgressiveSwordsOot,
    "progressive_shields_mm": ProgressiveShieldsMm,
    "progressive_gfs": ProgressiveGFS,
    "progressive_goron_lullaby": ProgressiveGoronLullaby,
    "progressive_clocks": ProgressiveClocks,
}

# category: items.shared


class SharedNutsSticks(Toggle):
    """
    Shared Nuts & Sticks
    """

    display_name = "Shared Nuts & Sticks"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedBows(Toggle):
    """
    Shared Bows
    """

    display_name = "Shared Bows"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedBombBags(Toggle):
    """
    Shared Bomb Bags
    """

    display_name = "Shared Bomb Bags"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedMagic(Toggle):
    """
    Shared Magic
    """

    display_name = "Shared Magic"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedMagicArrowFire(Toggle):
    """
    Shared Fire Arrow
    """

    display_name = "Shared Fire Arrow"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedMagicArrowIce(Toggle):
    """
    Shared Ice Arrow
    """

    display_name = "Shared Ice Arrow"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedMagicArrowLight(Toggle):
    """
    Shared Light Arrow
    """

    display_name = "Shared Light Arrow"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedSongEpona(Toggle):
    """
    Shared Epona's Song
    """

    display_name = "Shared Epona's Song"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedSongStorms(Toggle):
    """
    Shared Song of Storms
    """

    display_name = "Shared Song of Storms"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedSongTime(Toggle):
    """
    Shared Song of Time
    """

    display_name = "Shared Song of Time"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedSongSun(Toggle):
    """
    Shared Sun's Song
    """

    display_name = "Shared Sun's Song"

    # condition: function (s) { return hasOoTMM(s) && s.sunSongMm; }


class SharedHookshot(Toggle):
    """
    Shared Hookshots
    """

    display_name = "Shared Hookshots"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedLens(Toggle):
    """
    Shared Lens of Truth
    """

    display_name = "Shared Lens of Truth"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedOcarina(Toggle):
    """
    Shared Ocarina of Time
    """

    display_name = "Shared Ocarina of Time"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedMaskGoron(Toggle):
    """
    Shared Goron Mask
    """

    display_name = "Shared Goron Mask"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedMaskZora(Toggle):
    """
    Shared Zora Mask
    """

    display_name = "Shared Zora Mask"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedMaskBunny(Toggle):
    """
    Shared Bunny Hood
    """

    display_name = "Shared Bunny Hood"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedMaskKeaton(Toggle):
    """
    Shared Keaton Mask
    """

    display_name = "Shared Keaton Mask"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedMaskTruth(Toggle):
    """
    Shared Mask of Truth
    """

    display_name = "Shared Mask of Truth"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedMaskBlast(Toggle):
    """
    Shared Blast Mask
    """

    display_name = "Shared Blast Mask"

    # condition: function (s) { return hasOoTMM(s) && s.blastMaskOot; }


class SharedMaskStone(Toggle):
    """
    Shared Stone Mask
    """

    display_name = "Shared Stone Mask"

    # condition: function (s) { return hasOoTMM(s) && s.stoneMaskOot; }


class SharedSongElegy(Toggle):
    """
    Shared Elegy of Emptiness
    """

    display_name = "Shared Elegy of Emptiness"

    # condition: function (s) { return hasOoTMM(s) && s.elegyOot; }


class SharedWallets(Toggle):
    """
    Shared Wallets
    """

    display_name = "Shared Wallets"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedHealth(Toggle):
    """
    Shared Health
    """

    display_name = "Shared Health"

    # condition: function (x) { return x.games === 'ootmm'; }


class SharedSwords(Toggle):
    """
    Shared Swords
    """

    display_name = "Shared Swords"

    # condition: function (s) { return hasOoTMM(s) && s.extraChildSwordsOot && s.progressiveGFS !== 'progressive'; }


class SharedShields(Toggle):
    """
    Shared Shields
    """

    display_name = "Shared Shields"

    # condition: function (s) { return hasOoTMM(s) && s.progressiveShieldsOot === s.progressiveShieldsMm; }


class SharedSoulsEnemy(Toggle):
    """
    Shared Enemy Souls
    """

    display_name = "Shared Enemy Souls"

    # condition: function (s) { return hasOoTMM(s) && s.soulsEnemyOot && s.soulsEnemyMm; }


class SharedSoulsNpc(Toggle):
    """
    Shared NPC Souls
    """

    display_name = "Shared NPC Souls"

    # condition: function (s) { return hasOoTMM(s) && s.soulsNpcOot && s.soulsNpcMm; }


class SharedSoulsMisc(Toggle):
    """
    Shared Misc. Souls
    """

    display_name = "Shared Misc. Souls"

    # condition: function (s) { return hasOoTMM(s) && s.soulsMiscOot && s.soulsMiscMm; }


class SharedOcarinaButtons(Toggle):
    """
    Shared Ocarina Buttons
    """

    display_name = "Shared Ocarina Buttons"

    # condition: function (s) { return hasOoTMM(s) && s.ocarinaButtonsShuffleOot && s.ocarinaButtonsShuffleMm; }


class SharedSkeletonKey(Toggle):
    """
    Shared Skeleton Key
    """

    display_name = "Shared Skeleton Key"

    # condition: function (s) { return hasOoTMM(s) && s.skeletonKeyOot && s.skeletonKeyMm; }


class SharedBombchuBags(Toggle):
    """
    Shared Bombchu Bags
    """

    display_name = "Shared Bombchu Bags"

    # condition: function (s) { return hasOoTMM(s) && s.bombchuBagOot && s.bombchuBagMm; }


class SharedSpellFire(Toggle):
    """
    Shared Din's Fire
    """

    display_name = "Shared Din's Fire"

    # condition: function (s) { return hasOoTMM(s) && s.spellFireMm; }


class SharedSpellWind(Toggle):
    """
    Shared Farore's Wind
    """

    display_name = "Shared Farore's Wind"

    # condition: function (s) { return hasOoTMM(s) && s.spellWindMm; }


class SharedSpellLove(Toggle):
    """
    Shared Nayru's Love
    """

    display_name = "Shared Nayru's Love"

    # condition: function (s) { return hasOoTMM(s) && s.spellLoveMm; }


class SharedBootsIron(Toggle):
    """
    Shared Iron Boots
    """

    display_name = "Shared Iron Boots"

    # condition: function (s) { return hasOoTMM(s) && s.bootsIronMm; }


class SharedBootsHover(Toggle):
    """
    Shared Hover Boots
    """

    display_name = "Shared Hover Boots"

    # condition: function (s) { return hasOoTMM(s) && s.bootsHoverMm; }


class SharedTunicGoron(Toggle):
    """
    Shared Goron Tunic
    """

    display_name = "Shared Goron Tunic"

    # condition: function (s) { return hasOoTMM(s) && s.tunicGoronMm; }


class SharedTunicZora(Toggle):
    """
    Shared Zora Tunic
    """

    display_name = "Shared Zora Tunic"

    # condition: function (s) { return hasOoTMM(s) && s.tunicZoraMm; }


class SharedScales(Toggle):
    """
    Shared Scales
    """

    display_name = "Shared Scales"

    # condition: function (s) { return hasOoTMM(s) && s.scalesMm; }


class SharedStrength(Toggle):
    """
    Shared Strength
    """

    display_name = "Shared Strength"

    # condition: function (s) { return hasOoTMM(s) && s.strengthMm; }


items_shared_options: dict[str, Option] = {
    "shared_nuts_sticks": SharedNutsSticks,
    "shared_bows": SharedBows,
    "shared_bomb_bags": SharedBombBags,
    "shared_magic": SharedMagic,
    "shared_magic_arrow_fire": SharedMagicArrowFire,
    "shared_magic_arrow_ice": SharedMagicArrowIce,
    "shared_magic_arrow_light": SharedMagicArrowLight,
    "shared_song_epona": SharedSongEpona,
    "shared_song_storms": SharedSongStorms,
    "shared_song_time": SharedSongTime,
    "shared_song_sun": SharedSongSun,
    "shared_hookshot": SharedHookshot,
    "shared_lens": SharedLens,
    "shared_ocarina": SharedOcarina,
    "shared_mask_goron": SharedMaskGoron,
    "shared_mask_zora": SharedMaskZora,
    "shared_mask_bunny": SharedMaskBunny,
    "shared_mask_keaton": SharedMaskKeaton,
    "shared_mask_truth": SharedMaskTruth,
    "shared_mask_blast": SharedMaskBlast,
    "shared_mask_stone": SharedMaskStone,
    "shared_song_elegy": SharedSongElegy,
    "shared_wallets": SharedWallets,
    "shared_health": SharedHealth,
    "shared_swords": SharedSwords,
    "shared_shields": SharedShields,
    "shared_souls_enemy": SharedSoulsEnemy,
    "shared_souls_npc": SharedSoulsNpc,
    "shared_souls_misc": SharedSoulsMisc,
    "shared_ocarina_buttons": SharedOcarinaButtons,
    "shared_skeleton_key": SharedSkeletonKey,
    "shared_bombchu_bags": SharedBombchuBags,
    "shared_spell_fire": SharedSpellFire,
    "shared_spell_wind": SharedSpellWind,
    "shared_spell_love": SharedSpellLove,
    "shared_boots_iron": SharedBootsIron,
    "shared_boots_hover": SharedBootsHover,
    "shared_tunic_goron": SharedTunicGoron,
    "shared_tunic_zora": SharedTunicZora,
    "shared_scales": SharedScales,
    "shared_strength": SharedStrength,
}

# category: items.ageless


class AgelessSwords(Toggle):
    """
    Allows Link to use swords independently of his age
    """

    display_name = "Ageless Swords"

    # condition: function (x) { return hasGame(x, 'oot'); }


class AgelessShields(Toggle):
    """
    Allows Link to use shields independently of his age
    """

    display_name = "Ageless Shields"

    # condition: function (x) { return hasGame(x, 'oot'); }


class AgelessTunics(Toggle):
    """
    Allows Link to use tunics independently of his age
    """

    display_name = "Ageless Tunics"

    # condition: function (x) { return hasGame(x, 'oot'); }


class AgelessBoots(Toggle):
    """
    Allows Link to use boots independently of his age
    """

    display_name = "Ageless Boots"

    # condition: function (x) { return hasGame(x, 'oot'); }


class AgelessSticks(Toggle):
    """
    Allows Link to use deku sticks independently of his age
    """

    display_name = "Ageless Sticks"

    # condition: function (x) { return hasGame(x, 'oot'); }


class AgelessBoomerang(Toggle):
    """
    Allows Link to use the boomerang independently of his age
    """

    display_name = "Ageless Boomerang"

    # condition: function (x) { return hasGame(x, 'oot'); }


class AgelessHammer(Toggle):
    """
    Allows Link to use the hammer independently of his age
    """

    display_name = "Ageless Hammer"

    # condition: function (x) { return hasGame(x, 'oot'); }


class AgelessHookshot(Toggle):
    """
    Allows Link to use the hookshot independently of his age
    """

    display_name = "Ageless Hookshot"

    # condition: function (x) { return hasGame(x, 'oot'); }


class AgelessChildTrade(Toggle):
    """
    Allows Link to use the child trade items independently of his age
    """

    display_name = "Ageless Child Trade"

    # condition: function (x) { return hasGame(x, 'oot'); }


class AgelessStrength(Toggle):
    """
    Allows Child Link to use adult strength upgrades
    """

    display_name = "Ageless Strength"

    # condition: function (x) { return hasGame(x, 'oot'); }


items_ageless_options: dict[str, Option] = {
    "ageless_swords": AgelessSwords,
    "ageless_shields": AgelessShields,
    "ageless_tunics": AgelessTunics,
    "ageless_boots": AgelessBoots,
    "ageless_sticks": AgelessSticks,
    "ageless_boomerang": AgelessBoomerang,
    "ageless_hammer": AgelessHammer,
    "ageless_hookshot": AgelessHookshot,
    "ageless_child_trade": AgelessChildTrade,
    "ageless_strength": AgelessStrength,
}

items_options: dict[str, Option] = {
    **items_extensions_options,
    **items_progressive_options,
    **items_shared_options,
    **items_ageless_options,
}

ootmm_options: dict[str, Option] = {
    **main_options,
    **hints_options,
    **items_options,
    "death_link": DeathLink,
}

