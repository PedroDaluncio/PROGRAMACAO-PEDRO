from imposto import Imposto
from ipi import IPI
from icms import ICMS
from irpj import IRPJ
from iss import ISS


class Empresa:
    def __init__(self, cnpj: int, nome_de_fantasia: str):
        self.__cnpj = cnpj
        self.__nome_de_fantasia = nome_de_fantasia
        self.__impostos = []
        self.__faturamento_servicos = 0
        self.__faturamento_producao = 0
        self.__faturamento_vendas = 0

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def nome_de_fantasia(self):
        return self.__nome_de_fantasia

    @nome_de_fantasia.setter
    def nome_de_fantasia(self, nome_de_fantasia: str):
        if isinstance(nome_de_fantasia, str):
            self.__nome_de_fantasia = nome_de_fantasia

    @property
    def impostos(self):
        return self.__impostos

    def inclui_imposto(self, imposto: Imposto):
        if isinstance(imposto, Imposto) and imposto not in self.__impostos \
              and imposto is not None:
            self.__impostos.append(imposto)

    def remove_imposto(self, imposto: Imposto):
        if isinstance(imposto, Imposto) and imposto in self.__impostos:
            self.__impostos.remove(imposto)

    @property
    def faturamento_servicos(self):
        return self.__faturamento_servicos

    @property
    def faturamento_producao(self):
        return self.__faturamento_producao

    @property
    def faturamento_vendas(self):
        return self.__faturamento_vendas

    def faturamento_total(self) -> float:
        if self.__faturamento_producao is not None and \
              self.__faturamento_servicos is not None and \
              self.__faturamento_vendas is not None:
            faturamento_total = self.__faturamento_producao + \
                self.__faturamento_servicos + self.__faturamento_vendas
            return faturamento_total

    def total_impostos(self) -> float:
        if self.__impostos:
            total_impostos = 0.0
            for imposto in self.__impostos:
                if isinstance(imposto, IPI):
                    total_impostos += self.__faturamento_producao * \
                        (imposto.calcula_aliquota() / 100)
                elif isinstance(imposto, ICMS):
                    total_impostos += self.__faturamento_vendas * \
                        (imposto.calcula_aliquota() / 100)
                elif isinstance(imposto, ISS):
                    total_impostos += self.__faturamento_servicos * \
                        (imposto.calcula_aliquota() / 100)
                elif isinstance(imposto, IRPJ):
                    total_impostos += self.faturamento_total() * \
                        (imposto.calcula_aliquota() / 100)
            return total_impostos

    def set_faturamentos(self,
                         fat_servicos: float,
                         fat_producao: float,
                         fat_vendas: float):
        if isinstance(fat_producao, float) and \
             isinstance(fat_servicos, float) and \
             isinstance(fat_vendas, float):
            self.__faturamento_producao = fat_producao
            self.__faturamento_servicos = fat_servicos
            self.__faturamento_vendas = fat_vendas
