from urllib import request
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.file = request.urlopen(url)

    def get_players(self):
        players = []

        for line in self.file:
            decoded_line = line.decode("utf-8")
            parts = decoded_line.split(";")

            if len(parts) > 3:
                player = Player(
                    parts[0].strip(),
                    parts[1].strip(),
                    int(parts[3].strip()),
                    int(parts[4].strip())
                )

                players.append(player)

        return players
