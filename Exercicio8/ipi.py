from imposto import Imposto


class IPI(Imposto):
    def __init__(self, aliquota, tem_aliquota_adicional):
        super().__init__(aliquota)
        self.__tem_aliquota_adicional = tem_aliquota_adicional

    def calcula_aliquota(self):
        if self.__tem_aliquota_adicional:
            valor = self.aliquota + self.aliquota * 0.1
        return valor
