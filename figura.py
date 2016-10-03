#sasasas
import math
class Figuras:

    def cuadrado(self,lado):
        try:
            if lado > 0:
                return lado * lado
            else:
                return 'Datos incorrectos'
        except Exception ,e:
            return 'Datos incorrectos'

    def rectangulo(self,largo,ancho):
        try:
            if largo > 0 and ancho > 0:
                return largo * ancho
            else:
                return 'Datos incorrectos'
        except Exception ,e:
            return 'Datos incorrectos'

    def triangulo(self,base,altura):
        try:
            if base > 0 and altura > 0:
                return (base * altura)/2
            else:
                return 'Datos incorrectos'
        except Exception ,e:
            return 'Datos incorrectos'

    def circulo(self,radio):
        try:
            if radio > 0:
                return math.pi * (radio*radio)
            else:
                return 'Datos incorrectos'
        except Exception ,e:
            return 'Datos incorrectos'
