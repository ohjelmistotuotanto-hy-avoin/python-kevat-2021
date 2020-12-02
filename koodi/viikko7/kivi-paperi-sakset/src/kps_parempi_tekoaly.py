from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly:
    def __init__(self):
        self.lue = input
        self.kirjoita = print

    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = TekoalyParannettu(10)

        ekan_siirto = self.lue("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = tekoaly.anna_siirto()

        self.kirjoita(f"Tietokone valitsi: {tokan_siirto}")

        while self.onko_ok_siirto(ekan_siirto) and self.onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self.kirjoita(tuomari)

            ekan_siirto = self.lue("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = tekoaly.anna_siirto()

            self.kirjoita(f"Tietokone valitsi: {tokan_siirto}")
            tekoaly.aseta_siirto(ekan_siirto)

        self.kirjoita("Kiitos!")
        self.kirjoita(tuomari)

    def onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
