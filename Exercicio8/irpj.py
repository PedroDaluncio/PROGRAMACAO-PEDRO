from imposto import Imposto


class IRPJ(Imposto):
    def __init__(self, aliquota: float, desconto: float):
        super().__init__(aliquota)
        self.__desconto = desconto

    def calcula_aliquota(self):
        valor = self.aliquota - self.__desconto
        return valor
