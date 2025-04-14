class boss:
    def __init__(self, name, hp, nerves, attacks, opening_cutscene, closing_cutscene):
        self.name = name
        self.hp = hp
        self.nerves = nerves
        self.attacks = attacks
        self.opening = opening_cutscene
        self.closing = closing_cutscene

class ally:
    def __init__(self, name, hp, nerves, attacks):
        self.name = name
        self.hp = hp
        self.nerves = nerves
        self.attacks = attacks