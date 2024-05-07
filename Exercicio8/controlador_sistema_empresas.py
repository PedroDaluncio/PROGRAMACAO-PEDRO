from empresa import Empresa


class ControladorSistemaEmpresas():
    def __init__(self):
        self.__empresas = []

    def inclui_empresa(self, empresa: Empresa):
        if isinstance(empresa, Empresa):
            if self.__empresas:
                for elemento in self.__empresas:
                    if elemento.cnpj == empresa.cnpj:
                        return
            self.__empresas.append(empresa)

    def exclui_empresa(self, empresa: Empresa):
        if isinstance(empresa, Empresa):
            if self.__empresas and empresa in self.__empresas:
                self.__empresas.remove(empresa)

    def busca_empresa_pelo_cnpj(self, cnpj: int) -> Empresa:
        if isinstance(cnpj, int) and self.__empresas:
            for empresa in self.__empresas:
                if empresa.cnpj == cnpj:
                    return empresa

    @property
    def empresas(self) -> list:
        return self.__empresas

    '''
    Calcula o total de impostos de todas as empresas.
    Invoca a operacao total_impostos() de cada uma das empresas,
        somando os resultados
    @return somatorio dos impostos calculados de todas as empresas
    '''
    def calcula_total_impostos(self) -> float:
        total_impostos = 0
        for empresa in self.__empresas:
            total_impostos += empresa.total_impostos()
        return total_impostos
