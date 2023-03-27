import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    def test_lataaminen_oikein(self):
        self. maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
    def test_raha_vahenee(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
    def test_saldo_ei_muutu_jos_on_koyha(self):
        self.maksukortti.ota_rahaa(5000000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    def test_True_jos_rahat_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2), True)
    def test_False_jos_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20000), False)