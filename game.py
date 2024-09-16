class Game():
    def __init__(self):
        self.life = 3
        self.game_is_on = True
        self.new_game = False
        self.pause = True

    def add_life(self):
        self.life += 1
