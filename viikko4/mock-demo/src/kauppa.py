class Kauppa:
    def __init__(self, pankki, viitegeneraattori):
        self.pankki = pankki
        self.viitegeneraattori = viitegeneraattori
        self.yhteishinta = 0

    def aloita_ostokset(self):
        self.yhteishinta = 0

    def lisaa_ostos(self, hinta):
        self.yhteishinta = self.yhteishinta + hinta

    def maksa(self, tilinumero):
        self.pankki.maksa(
            tilinumero,
            self.yhteishinta,
            self.viitegeneraattori.uusi()
        )
