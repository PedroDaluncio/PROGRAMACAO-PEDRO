"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""


class Ordenacao:

    def __init__(self, array_para_ordenar: []):
        self.array = array_para_ordenar
        self.novo_array = []

    def ordena(self):
        while len(self.array) > 0 :
            menor_numero = self.array[0]
            for number in self.array:
                if number < menor_numero:
                    menor_numero = number
            self.novo_array.append(menor_numero)
            self.array.remove(menor_numero)
        return self.novo_array

    def toString(self):
        texto = ''
        array = self.ordena()
        contador = 0
        while contador < len(array):
            texto += str(array[contador])
            if contador != len(array) - 1:
                texto += ','
            contador += 1
        return texto
