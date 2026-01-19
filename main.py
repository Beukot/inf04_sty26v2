import unittest
from enum import Enum
import random

# to jest enum. używamy go do nazwania pewnych wartości liczbowych.
# czyli tam gdzie umieścimy RozmiarSkrytki.Maly python traktuje to jak 10
# i analogicznie dla RozmiarSkrytki.Sredni i RozmiarSkrytki.Duzy
# np. RozmiarSkrytki.Sredni + RozmiarSkrytki.Duzy = 50
class RozmiarSkrytki(Enum):
    Maly = 10
    Sredni = 20
    Duzy = 30


class Skrytka:
    instancje_klasy = 0

    def __init__(self, rozmiar_skrytki):
        Skrytka.instancje_klasy += 1

        self.rozmiar_skrytki = rozmiar_skrytki
        self.zawartosc = None
        self.kod_dostepu = None

    # tak się robi metodę statyczną - używa się ją Skrytka.generuj_kod() - nie należy do instancji klasy
    # nie używa też self, bo nie wpływa zazwyczaj na pola funkcji
    @staticmethod
    def generuj_kod():
        nowyKod = ""

        for i in range(5):
            nowyKod += str(random.randint(0, 9))

        return nowyKod

    def czy_pusta(self):
        if self.zawartosc is None:
            print("skrytka pusta!")
            return True
        else:
            print("Skrytka nie jest pusta!")
            return False

    def umiesc_paczke(self, zawartosc):
        if self.czy_pusta() and len(zawartosc) <= self.rozmiar_skrytki.value:
            self.zawartosc = zawartosc
            self.kod_dostepu = Skrytka.generuj_kod()
            return self.kod_dostepu
        else:
            return False

    def otworz_skrytke(self, podany_kod):
        if self.kod_dostepu == podany_kod:
            self.zawartosc = None
            self.kod_dostepu = None
            return self.zawartosc
        else:
            return False

class testy_skrytki(unittest.TestCase):
    def test_licznika_instancji(self):
        skrytka1 = Skrytka(RozmiarSkrytki.Maly)
        skrytka2 = Skrytka(RozmiarSkrytki.Sredni)

        self.assertEqual(2, Skrytka.instancje_klasy)

    def test_generowanie_kodu(self):
        kod = Skrytka.generuj_kod()

        self.assertTrue(len(kod) == 5 and kod.isnumeric())
    def test_umieszczenie_paczki(self):
        skrytka3 = Skrytka(RozmiarSkrytki.Maly)
        kod = skrytka3.umiesc_paczke("paczka")

        self.assertTrue(kod.isascii())

    def test_umieszczenie_paczki_w_zajetej_skrytce(self):
        skrytka4 = Skrytka(RozmiarSkrytki.Sredni)
        skrytka4.umiesc_paczke("paczka srednia")

        self.assertFalse(skrytka4.umiesc_paczke("paczka srednia"))
    def test_umieszczenie_zbyt_duzej_paczki(self):
        skrytka5 = Skrytka(RozmiarSkrytki.Maly)

        self.assertFalse(skrytka5.umiesc_paczke("paczka troche za duza jak na skrytke"))

    def test_otwieranie_skrytki_poprawnym_kodem(self):
        skrytka6 = Skrytka(RozmiarSkrytki.Duzy)
        zawartosc = "paczka do odbioru"
        kod = skrytka6.umiesc_paczke(zawartosc)

        self.assertEqual(zawartosc, skrytka6.otworz_skrytke(kod))

    def test_otwieranie_skrytki_blednym_kodem(self):
        skrytka7 = Skrytka(RozmiarSkrytki.Duzy)
        poprawny_kod = skrytka7.umiesc_paczke("paczka do odbioru")
        bledny_kod = "11111"

        if poprawny_kod == bledny_kod:
            bledny_kod = "22222"

        self.assertFalse(skrytka7.otworz_skrytke(bledny_kod))
