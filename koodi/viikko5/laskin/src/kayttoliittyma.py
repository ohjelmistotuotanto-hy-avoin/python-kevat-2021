from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self.sovellus = sovellus
        self.root = root

    def suorita_komento(self, komento):
        arvo = 0

        try:
            arvo = int(self.syote_kentta.get())
        except Exception:
            pass

        if komento == Komento.SUMMA:
            self.sovellus.plus(arvo)
        elif komento == Komento.EROTUS:
            self.sovellus.miinus(arvo)
        elif komento == Komento.NOLLAUS:
            self.sovellus.nollaa()
        elif komento == Komento.KUMOA:
            pass

        self.kumoa_painike["state"] = constants.NORMAL

        if self.sovellus.tulos == 0:
            self.nollaus_painike["state"] = constants.DISABLED
        else:
            self.nollaus_painike["state"] = constants.NORMAL

        self.syote_kentta.delete(0, constants.END)
        self.tulos_var.set(self.sovellus.tulos)

    def kaynnista(self):
        self.tulos_var = StringVar()
        self.tulos_var.set(self.sovellus.tulos)
        self.syote_kentta = ttk.Entry(master=self.root)

        tulos_teksti = ttk.Label(textvariable=self.tulos_var)

        summa_painike = ttk.Button(
            master=self.root,
            text="Summa",
            command=lambda: self.suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self.root,
            text="Erotus",
            command=lambda: self.suorita_komento(Komento.EROTUS)
        )

        self.nollaus_painike = ttk.Button(
            master=self.root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self.suorita_komento(Komento.NOLLAUS)
        )

        self.kumoa_painike = ttk.Button(
            master=self.root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self.suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self.syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self.nollaus_painike.grid(row=2, column=2)
        self.kumoa_painike.grid(row=2, column=3)
