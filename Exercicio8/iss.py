from imposto import Imposto


class ISS(Imposto):
    def __init__(self, aliquota: float):
        super().__init__(aliquota)
        self.__servicos = []

    def inclui_servico(self, nome: str):
        if isinstance(nome, str):
            self.__servicos.append(nome)

    def exclui_servico(self, nome: str):
        if isinstance(nome, str) and nome in self.__servicos:
            self.__servicos.remove(nome)

    def calcula_aliquota(self):
        if self.__servicos:
            qt_ah_ser_reduzida = 0
            for servicos in self.__servicos:
                qt_ah_ser_reduzida += 0.1
        valor = self.aliquota - qt_ah_ser_reduzida
        return valor
