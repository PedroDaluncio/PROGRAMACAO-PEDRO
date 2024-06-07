from abstractOnibus import AbstractOnibus
from onibusJahCheioException import OnibusJahCheioException
from onibusJahVazioException import OnibusJahVazioException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahDesligadoException import OnibusJahDesligadoException


class Onibus(AbstractOnibus):
    def __init__(self, capacidade: int, total_passageiros: int,
                 ligado: bool):
        self.__capacidade = capacidade
        self.__total_passageiros = total_passageiros
        self.__ligado = ligado

    def ligar(self):
        if self.__ligado:
            raise OnibusJahLigadoException()
        self.__ligado = True

    def desligar(self):
        if self.__ligado is False:
            raise OnibusJahDesligadoException()
        self.__ligado = False

    def embarca_pessoa(self):
        if self.__total_passageiros + 1 > self.__capacidade:
            raise OnibusJahCheioException()
        self.__total_passageiros += 1

    def desembarca_pessoa(self):
        if self.__total_passageiros == 0:
            raise OnibusJahVazioException()
        self.__total_passageiros -= 1

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        if isinstance(capacidade, int):
            self.__capacidade = capacidade

    @property
    def total_passageiros(self):
        return self.__total_passageiros

    @property
    def ligado(self):
        return self.__ligado
