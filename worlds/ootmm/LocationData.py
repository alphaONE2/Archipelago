class OoTMMLocationData:
    def __init__(self, id: int, game: str, name: str, type: str, vanilla_item: str):
        if vanilla_item != "NOTHING":
            vanilla_item = f"{game.upper()}_{vanilla_item}"

        self.id = id
        self.game = game
        self.name = f"{name} ({game})"
        self.type = type
        self.vanilla_item = vanilla_item
