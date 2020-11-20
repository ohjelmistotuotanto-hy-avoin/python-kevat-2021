class Tekoaly:
    def __init__(self):
        self.siirto = 0

    def anna_siirto(self):
        self.siirto = self.siirto + 1
        self.siirto = self.siirto % 3

        if self.siirto == 0:
            return "k"
        elif self.siirto == 1:
            return "p"
        else:
            return "s"

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
