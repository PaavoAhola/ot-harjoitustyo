import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.riittava_kortti = Maksukortti(1000)
        self.koyha_kortti = Maksukortti(100)

    def test_alussa_oikea_rahamaara(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_alussa_oikeat_lounaat(self):
        self.assertEqual(self.kassa.edulliset + self.kassa.maukkaat, 0)

    def test_kassa_kasvaa_kateisella_edullisesti(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_kassa_kasvaa_kateisella_maukkaasti(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_vaihtoraha_edullisesti(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300), 60)

    def test_vaihtoraha_maukkaasti(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)

    def test_myydyt_kateisella_edullisesti(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_myydyt_kateisella_maukkaasti(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kassa_ei_muutu_jos_rahat_ei_riita_edulliseen(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassa_ei_muutu_jos_rahat_ei_riita_maukkaaseen(self):
        self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_myydyt_ei_muutu_jos_rahat_ei_riita_edulliseen(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_myydyt_ei_muutu_jos_rahat_ei_riita_maukkaaseen(self):
        self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_oikea_vaihtoraha_kun_rahat_ei_riita_edulliseen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(100), 100)

    def test_oikea_vaihtoraha_kun_rahat_ei_riita_maukkaaseen(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(100), 100)

    def test_veloita_kortilta_jos_kortilla_rahaa_edulliseen(self):
        self.kassa.syo_edullisesti_kortilla(self.riittava_kortti)
        self.assertEqual(self.riittava_kortti.saldo, 760)

    def test_veloita_kortilta_jos_kortilla_rahaa_maukkaaseen(self):
        self.kassa.syo_maukkaasti_kortilla(self.riittava_kortti)
        self.assertEqual(self.riittava_kortti.saldo, 600)

    def test_palauta_true_kortilla_edullisesti(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.riittava_kortti), True)

    def test_palauta_true_kortilla_maukkaasti(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.riittava_kortti), True)

    def test_kasvata_edullisia_jos_kortilla_rahaa_edulliseen(self):
        self.kassa.syo_edullisesti_kortilla(self.riittava_kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kasvata_maukkaita_jos_kortilla_rahaa_maukkaaseen(self):
        self.kassa.syo_maukkaasti_kortilla(self.riittava_kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_ala_veloita_kortilta_jos_kortilla_ei_rahaa_edulliseen(self):
        self.kassa.syo_edullisesti_kortilla(self.koyha_kortti)
        self.assertEqual(self.koyha_kortti.saldo, 100)

    def test_ala_veloita_kortilta_jos_kortilla_ei_rahaa_maukkaaseen(self):
        self.kassa.syo_maukkaasti_kortilla(self.koyha_kortti)
        self.assertEqual(self.koyha_kortti.saldo, 100)

    def test_palauta_false_kortilla_edullisesti(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.koyha_kortti), False)

    def test_palauta_false_kortilla_maukkaasti(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.koyha_kortti), False)

    def test_ala_kasvata_edullisia_jos_kortilla_ei_rahaa_edulliseen(self):
        self.kassa.syo_edullisesti_kortilla(self.koyha_kortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_ala_kasvata_maukkaita_jos_kortilla_ei_rahaa_maukkaaseen(self):
        self.kassa.syo_maukkaasti_kortilla(self.koyha_kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kassa_ei_muutu_kortilla_edullisesti(self):
        self.kassa.syo_edullisesti_kortilla(self.riittava_kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassa_ei_muutu_kortilla_maukkaasti(self):
        self.kassa.syo_maukkaasti_kortilla(self.riittava_kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortin_saldo_ok_latauksessa(self):
        self.kassa.lataa_rahaa_kortille(self.riittava_kortti, 100)
        self.assertEqual(self.riittava_kortti.saldo, 1100)

    def test_kassan_rahat_ok_latauksessa(self):
        self.kassa.lataa_rahaa_kortille(self.riittava_kortti, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)

    def test_kassan_rahat_ok_latauksessa_negatiivista(self):
        self.kassa.lataa_rahaa_kortille(self.riittava_kortti, -100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
