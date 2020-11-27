from varasto import Varasto
from pankki import Pankki
from ostoskori import Ostoskori
from viitegeneraattori import Viitegeneraattori


class Kauppa:
    def __init__(self):
        self.varasto = Varasto.get_instance()
        self.pankki = Pankki.get_instance()
        self.viitegeneraattori = Viitegeneraattori.get_instance()
        self.kaupan_tili = "33333-44455"

    def aloita_asiointi(self):
        self.ostoskori = Ostoskori()

    def poista_korista(self, id):
        tuote = self.varasto.hae_tuote(id)
        self.ostoskori.poista(tuote)
        self.varasto.palauta_varastoon(tuote)

    def lisaa_koriin(self, id):
        if self.varasto.saldo(id) > 0:
            tuote = self.varasto.hae_tuote(id)
            self.ostoskori.lisaa(tuote)
            self.varasto.ota_varastosta(tuote)

    def tilimaksu(self, nimi, tili_numero):
        viite = self.viitegeneraattori.uusi()
        summa = self.ostoskori.hinta()

        return self.pankki.tilisiirto(nimi, viite, tili_numero, self.kaupan_tili, summa)
