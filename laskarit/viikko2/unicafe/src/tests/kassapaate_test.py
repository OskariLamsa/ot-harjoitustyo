import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    def test_kassa_rahat_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    def test_kassa_ostokset_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
    def test_edullinen_osto_riittaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassa.edulliset, 1)
    def test_edullinen_osto_ei_riittaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassa.edulliset, 0)
    def test_maukas_osto_riittaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassa.maukkaat, 1)
    def test_maukas_osto_ei_riittaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(399), 399)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_osta_edullinen(self):
        if self.kassa.syo_edullisesti_kortilla(self.maksukortti):
            self.assertEqual(self.maksukortti.saldo, 760)
            self.kassa.kassassa_rahaa += 240
            self.assertEqual(self.kassa.kassassa_rahaa, 100240)
            self.assertEqual(self.kassa.edulliset, 1)

    def test_osta_maukkaasti(self):
        if self.kassa.syo_maukkaasti_kortilla(self.maksukortti):
            self.assertEqual(self.maksukortti.saldo, 600)
            self.kassa.kassassa_rahaa += 400
            self.assertEqual(self.kassa.kassassa_rahaa, 100400)
            self.assertEqual(self.kassa.maukkaat, 1)


    def test_rahan_lisays_onnistuu(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.maksukortti.saldo, 1200)

    def test_rahan_lisays_ei_onnistu(self):
        self.kassa.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_liian_koyha_edullinen(self):
            kortti = Maksukortti(100)
            self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), False)
            self.assertEqual(self.kassa.kassassa_rahaa, 100000)
            self.assertEqual(self.kassa.edulliset, 0)

    def test_liian_koyha_maukas(self):
            kortti = Maksukortti(100)
            self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), False)
            self.assertEqual(self.kassa.kassassa_rahaa, 100000)
            self.assertEqual(self.kassa.maukkaat, 0)