from unittest import result


def bee_1143(n):

    result = ''
    for i in range(n):
        result += ("{} {} {}\n".format(i+1,pow(i+1,2),pow(i+1,3)))
    
    return result

import unittest

class QuadradoeaoCubo(unittest.TestCase):

    def test_quadradoeaocubo_5(self):
        self.assertEqual(bee_1143(5), '1 1 1\n2 4 8\n3 9 27\n4 16 64\n5 25 125\n')
    
    def test_quadradoeaocubo_1(self):
        self.assertEqual(bee_1143(1), '1 1 1\n')
    
    def test_quadradoeaocubo_10(self):
        self.assertEqual(bee_1143(10), '1 1 1\n2 4 8\n3 9 27\n4 16 64\n5 25 125\n6 36 216\n7 49 343\n8 64 512\n9 81 729\n10 100 1000\n')
        
    def test_quadradoeaocubo_7(self):
        self.assertEqual(bee_1143(7), '1 1 1\n2 4 8\n3 9 27\n4 16 64\n5 25 125\n6 36 216\n7 49 343\n')
    
    def test_quadradoeaocubo_9(self):
        self.assertEqual(bee_1143(9), '1 1 1\n2 4 8\n3 9 27\n4 16 64\n5 25 125\n6 36 216\n7 49 343\n8 64 512\n9 81 729\n')

if __name__ == '__main__':
    unittest.main()