from tkinter import Tk
from kayttoliittyma import Kayttoliittyma
from sovellus import Sovellus


def main():
    sovellus = Sovellus()

    window = Tk()
    window.title("Laskin")

    kayttoliittyma = Kayttoliittyma(sovellus, window)
    kayttoliittyma.kaynnista()

    window.mainloop()

if __name__ == "__main__":
    main()
