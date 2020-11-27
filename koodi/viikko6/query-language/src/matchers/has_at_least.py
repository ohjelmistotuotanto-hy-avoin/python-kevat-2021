class HasAtLeast:
    def __init__(self, value, attr):
        self.value = value
        self.attr = attr

    def matches(self, player):
        player_value = getattr(player, self.attr)

        return player_value >= self.value
