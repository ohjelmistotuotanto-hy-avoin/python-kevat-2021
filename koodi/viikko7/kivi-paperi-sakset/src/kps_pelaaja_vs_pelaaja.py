from tuomari import Tuomari


class KPSPelaajaVsPelaaja:
    def __init__(self):
        self.lue = input
        self.kirjoita = print

    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self.lue("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self.lue("Toisen pelaajan siirto: ")

        while self.onko_ok_siirto(ekan_siirto) and self.onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self.kirjoita(tuomari)

            ekan_siirto = self.lue("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self.lue("Toisen pelaajan siirto: ")

        self.kirjoita("Kiitos!")
        self.kirjoita(tuomari)

    def onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
