import unittest
from figura import Figuras


class TestFiguras(unittest.TestCase):

    def setUp(self):
        self.figura = Figuras()

    def test_area_cuadrado_lado_5(self):
        resultado = self.figura.cuadrado(5)
        self.assertEqual(25, resultado)

    def test_area_cuadrado_lado_5(self):
        resultado = self.figura.cuadrado(4)
        self.assertEqual(16, resultado)

    def test_area_cuadrado_lado_6(self):
        resultado = self.figura.cuadrado(6)
        self.assertEqual(36, resultado)

    def test_area_cuadrado_lado_g(self):
        resultado = self.figura.cuadrado('g')
        self.assertEqual('Datos incorrectos', resultado)

    def test_area_cuadrado_lado_4_punto_5(self):
        resultado = self.figura.cuadrado(4.5)
        self.assertEqual(20.25, resultado)

    def test_area_cuadrado_lado_menos_5(self):
        resultado = self.figura.cuadrado(-5)
        self.assertEqual('Datos incorrectos', resultado)

    def test_area_rectangulo_largo_6_ancho_4(self):
        resultado = self.figura.rectangulo(6, 4)
        self.assertEqual(24, resultado)

    def test_area_rectangulo_largo_10_punto_5_ancho_6_punto_2(self):
        resultado = self.figura.rectangulo(10.5, 6.2)
        self.assertEqual(65.10000000000001, resultado)

    def test_area_rectangulo_largo_10_ancho_j(self):
        resultado = self.figura.rectangulo(10.5, 'j')
        self.assertEqual('Datos incorrectos', resultado)

    def test_area_rectangulo_largo_menos_8_ancho_5(self):
        resultado = self.figura.rectangulo(-8, 5)
        self.assertEqual('Datos incorrectos', resultado)

    def test_area_triangulo_base_3_altura_2(self):
        resultado = self.figura.triangulo(3, 2)
        self.assertEqual(3, resultado)

    def test_area_triangulo_base_3_5_altura_2_2(self):
        resultado = self.figura.triangulo(3.5, 2.2)
        self.assertEqual(3.8500000000000005, resultado)

    def test_area_triangulo_base_g_altura_2_2(self):
        resultado = self.figura.triangulo('g', 2.2)
        self.assertEqual('Datos incorrectos', resultado)

    def test_area_circulo_radio_5(self):
        resultado = self.figura.circulo(5)
        self.assertEqual(78.53981633974483, resultado)

    def test_area_circulo_radio_g(self):
        resultado = self.figura.circulo('g')
        self.assertEqual('Datos incorrectos', resultado)

    def test_area_circulo_radio_4_punto_cinco(self):
        resultado = self.figura.circulo(4.5)
        self.assertEqual(63.61725123519331, resultado)

if __name__ == '__main__':
    unittest.main()
