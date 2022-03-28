import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(5)

        self.assertEqual(str(self.maksukortti), "saldo: 0.15")

    def vahenee_oikein(self):
        self.maksukortti.ota_rahaa(5)

        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(20)

        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def ottaminen_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

    def ottaminen_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)
