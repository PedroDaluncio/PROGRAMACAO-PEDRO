"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""


class Ordenacao:

    def __init__(self, array_para_ordenar: []):
        self.array = array_para_ordenar
        self.novo_array = []

    def ordena(self):
        maior_num = self.array[0]
        while len(self.novo_array) < len(self.array):
            menor_num = self.array[0]
            for number in self.array:
                if menor_num > number and number not in self.novo_array:
                    menor_num = number
                elif menor_num < number and number not in self.novo_array:
                    print(maior_num)
                    maior_num = number

            if menor_num not in self.novo_array:
                self.novo_array.append(menor_num)
            elif maior_num not in self.novo_array:
                self.novo_array.append(maior_num)
        return self.novo_array

    def toString(self):
        texto = ''
        array = self.ordena()
        for number in array:
            texto += str(number)
            if number != array[-1]:
                texto += ','
        return texto

sla = Ordenacao([1,2,3,4,5])
print(sla.ordena())