class Viitegeneraattori:
    __instanssi = None

    @staticmethod
    def get_instance():
        if not Viitegeneraattori.__instanssi:
            Viitegeneraattori.__instanssi = Viitegeneraattori()

        return Viitegeneraattori.__instanssi

    def __init__(self):
        self.seuraava = 1

    def uusi(self):
        self.seuraava = self.seuraava + 1

        return self.seuraava
