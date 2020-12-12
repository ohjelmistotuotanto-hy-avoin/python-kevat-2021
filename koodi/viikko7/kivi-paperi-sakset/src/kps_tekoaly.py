from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly:
    def __init__(self):
        self._lue = input
        self._kirjoita = print

    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = Tekoaly()

        ekan_siirto = self._lue("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = tekoaly.anna_siirto()

        self._kirjoita(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self._kirjoita(tuomari)

            ekan_siirto = self._lue("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = tekoaly.anna_siirto()

            self._kirjoita(f"Tietokone valitsi: {tokan_siirto}")

        self._kirjoita("Kiitos!")
        self._kirjoita(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
