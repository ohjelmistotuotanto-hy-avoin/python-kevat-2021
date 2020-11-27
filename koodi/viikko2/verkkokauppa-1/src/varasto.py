from tuote import Tuote
from kirjanpito import Kirjanpito


class Varasto:
    __instanssi = None

    @staticmethod
    def get_instance():
        if not Varasto.__instanssi:
            Varasto.__instanssi = Varasto()

        return Varasto.__instanssi

    def __init__(self):
        self.kirjanpito = Kirjanpito.get_instance()
        self.saldot = {}
        self.alusta_tuotteet()

    def hae_tuote(self, id):
        tuotteet = self.saldot.keys()

        for tuote in tuotteet:
            if tuote.id == id:
                return tuote

        return None

    def saldo(self, id):
        tuote = self.hae_tuote(id)

        return self.saldot[tuote]

    def ota_varastosta(self, tuote):
        saldo = self.saldo(tuote.id)

        self.saldot[tuote] = saldo - 1

        self.kirjanpito.lisaa_tapahtuma(f"otettiin varastosta {tuote}")

    def palauta_varastoon(self, tuote):
        saldo = self.saldo(tuote.id)

        self.saldot[tuote] = saldo + 1

        self.kirjanpito.lisaa_tapahtuma(f"palautettiin varastoon {tuote}")

    def alusta_tuotteet(self):
        self.saldot[Tuote(1, "Koff Portteri", 3)] = 100
        self.saldot[Tuote(2, "Fink Bräu I", 1)] = 25
        self.saldot[Tuote(3, "Sierra Nevada Pale Ale", 5)] = 30
        self.saldot[Tuote(4, "Mikkeller not just another Wit", 7)] = 40
        self.saldot[Tuote(5, "Weihenstephaner Hefeweisse", 4)] = 15
