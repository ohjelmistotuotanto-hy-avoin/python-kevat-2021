def laske_summa(luku1, luku2):
    return luku1 + luku2


class Laskin:
    def __init__(self, io):
        self.io = io

    def suorita(self):
        while True:
            luku1 = int(self.io.lue("Luku 1:"))

            if luku1 == -9999:
                return

            luku2 = int(self.io.lue("Luku 2:"))

            if luku2 == -9999:
                return

            vastaus = laske_summa(luku1, luku2)

            self.io.kirjoita(f"Summa: {vastaus}")
