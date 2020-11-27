class PlaysIn:
    def __init__(self, team):
        self.team = team

    def matches(self, player):
        return player.team == self.team
