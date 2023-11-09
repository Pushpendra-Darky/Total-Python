class Player:

    alive = False
    @classmethod
    def revive(cls):
        cls.alive = True
