import unittest
import generate_keys as gK

class GenerateKeyTest(unittest.TestCase):

    def test_generate_n(self):
        self.assertEquals(gK.generate_n(3784321, 5793197), 21923317064237, "test_generate_n() failed")

    def test_generate_phi(self):
        self.assertEquals(gK.generate_phi(3784321, 5793197), 21923307486720, "test_generate_phi() failed")

    def test_generate_d(self):
        self.assertEquals(gK.generate_d(143429880, 143429800), 1792873, "test_generate_d() failed")