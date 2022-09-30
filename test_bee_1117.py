def bee_1117(nota_1, nota_2):
    somatorioNotas=0

    if(nota_1>10 or nota_1<0 or nota_2>10 or nota_2<0):
        return "nota invalida"
    
    somatorioNotas = nota_1 + nota_2
    return "media = {0:.2f}".format(somatorioNotas/2)

import unittest

class ValidacaoNota(unittest.TestCase):

    def test_validacaonota_valor_negativo_1(self):
        self.assertEqual(bee_1117(-3.5, 3.5), "nota invalida")
        
    def test_validacaonota_valor_acima_1(self):
        self.assertEqual(bee_1117(3.5, 11.0), "nota invalida")
        
    def test_validacaonota_1(self):
        self.assertEqual(bee_1117(3.5, 10.0), "media = 6.75")
        
    def test_validacaonota_2(self):
        self.assertEqual(bee_1117(8.0, 4.0), "media = 6.00")
        
    def test_validacaonota_acima_2(self):
        self.assertEqual(bee_1117(62.0, 2.0), "nota invalida")
        
    def test_validacaonota_3(self):
        self.assertEqual(bee_1117(3.7, 7.3), "media = 5.50")
        
    def test_validacaonota_valor_negativo_2(self):
        self.assertEqual(bee_1117(13.5, -4.5), "nota invalida")

if __name__ == '__main__':
    unittest.main()