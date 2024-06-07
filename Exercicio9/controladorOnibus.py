from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):
    def __init__(self):
        self.__onibus = ''

    def ligar(self):
        self.__onibus.ligar()

    def desligar(self):
        self.__onibus.desligar()

    def embarca_pessoa(self):
        self.__onibus.embarca_pessoa()

    def desembarca_pessoa(self):
        self.__onibus.desembarca_pessoa()

    @property
    def onibus(self):
        return self.__onibus

    def inicializar_onibus(self, capacidade, total_passageiros, ligado):
        if not isinstance(capacidade, int) or not \
                isinstance(total_passageiros, int) or not \
                isinstance(ligado, bool):
            raise ComandoInvalidoException()
        elif (capacidade < 0 or total_passageiros < 0):
            raise ComandoInvalidoException()
        elif total_passageiros > capacidade:
            raise ComandoInvalidoException()
        elif ligado is False:
            raise ComandoInvalidoException()
        self.__onibus = Onibus(capacidade, total_passageiros, ligado)
