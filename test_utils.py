import unittest
import utils

class GenerateKeyTest(unittest.TestCase):

    def test_pgcd(self):
        self.assertEquals(utils.pgcd(36, 24), 12, "test_pgcd_1() failed")
        self.assertEquals(utils.pgcd(57, 97), 1, "test_pgcd_2() failed")

    def test_puissance(self):
        self.assertEquals(utils.puissance(2, 5, 6), 2, "test_puissance_1() failed")
        self.assertEquals(utils.puissance(8, 5, 15), 8, "test_puissance_2() failed")
        self.assertEquals(utils.puissance(43, 5, 53), 11, "test_puissance_3() failed")

    def test_prime_number(self):
        self.assertEquals(utils.test_prime_number(97), True, "test_prime_number_1() failed")
        self.assertEquals(utils.test_prime_number(406), False, "test_prime_number_2() failed")

    def test_bezout(self):
        self.assertEquals(utils.bezout(100, 1000), 1.0, "test_bezout_1() failed")
        self.assertEquals(utils.bezout(1000150, 100100), 471, "test_bezout_2() failed")
        

        