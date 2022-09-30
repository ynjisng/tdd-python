def bee_1132(a, b):
    if a > b: a, b=b, a
    soma = 0
    for i in range(a, b+1):
        if i % 13 != 0:soma += i
    return soma

import unittest

class Multiplos13(unittest.TestCase):

    def test_multiplos13_1(self):
        self.assertEqual(bee_1132(100, 200), 13954)
        
    def test_multiplos13_2(self):
        self.assertEqual(bee_1132(80, 100), 1799)
        
    def test_multiplos13_3(self):
        self.assertEqual(bee_1132(17, 176), 14270)
        
    def test_multiplos13_4(self):
        self.assertEqual(bee_1132(500, 550), 24669)
        
    def test_multiplos13_5(self):
        self.assertEqual(bee_1132(-137, -243), -18822)
        
    def test_multiplos13_6(self):
        self.assertEqual(bee_1132(100, 80), 1799)
        
    def test_multiplos13_7(self):
        self.assertEqual(bee_1132(-127, -129), -384)

if __name__ == '__main__':
    unittest.main()