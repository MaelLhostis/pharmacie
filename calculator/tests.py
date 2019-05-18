from django.test import TestCase

import unittest
from .models import Calculator


class TestStringMethods(unittest.TestCase):
    def test_taux_remise(self):
        self.assertEqual(Calculator.taux_remise(100, 50), 50)

    def test_prix_achat_net(self):
        self.assertEqual(Calculator.prix_achat_net(10, 100), 90)

    def test_prix_vente_net(self):
        self.assertEqual(Calculator.prix_vente_net(100, 2), 200)

    def test_coef(self):
        self.assertEqual(Calculator.coef(100, 50), 2)

    def test_compute(self):
        json_strings = [
            '{"taux_remise": 10, "prix_achat_net": 90.0, "prix_vente_net": 180.0, "coef": 2}',
            '{"taux_remise": 10, "prix_achat_net": 90.0, "prix_vente_net": 180.0, "coef": 2}',
            '{"taux_remise": 10.0, "prix_achat_net": 90, "prix_vente_net": 180.0, "coef": 2}',
            '{"taux_remise": 10, "prix_achat_net": 90, "prix_vente_net": 180, "coef": 2.0}',
            '{"taux_remise": 10, "prix_achat_net": 90, "prix_vente_net": 180.0, "coef": 2}',
        ]

        ids = ["prix_brut", "taux_remise", "prix_achat_net", "prix_vente_net", "coef"]

        for i in range(5):
            self.assertEqual(
                Calculator.compute(ids[i], 100, 10, 90, 180, 2), json_strings[i]
            )


if __name__ == "__main__":
    unittest.main()
