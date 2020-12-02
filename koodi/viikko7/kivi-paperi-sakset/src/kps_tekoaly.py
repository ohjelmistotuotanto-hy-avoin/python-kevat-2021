from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly:
    def __init__(self):
        self.lue = input
        self.kirjoita = print

    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = Tekoaly()

        ekan_siirto = self.lue("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = tekoaly.anna_siirto()

        self.kirjoita(f"Tietokone valitsi: {tokan_siirto}")

        while self.onko_ok_siirto(ekan_siirto) and self.onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self.kirjoita(tuomari)

            ekan_siirto = self.lue("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = tekoaly.anna_siirto()

            self.kirjoita(f"Tietokone valitsi: {tokan_siirto}")

        self.kirjoita("Kiitos!")
        self.kirjoita(tuomari)

    def onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
