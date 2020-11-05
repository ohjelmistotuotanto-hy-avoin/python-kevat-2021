class Ostoskori:
    def __init__(self):
        self.tuotteet = []
    
    def lisaa(self, tuote):
        self.tuotteet.append(tuote)
    
    def poista(self, tuote):
        self.tuotteet = list(
            filter(lambda t: t.id != tuote.id, self.tuotteet)
        )

    def hinta(self):
        hinnat = map(lambda t: t.hinta, self.tuotteet)

        return sum(hinnat)
