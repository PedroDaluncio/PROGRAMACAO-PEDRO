from abc import ABC, abstractmethod
from Carta import *
from Personagem import *
from Jogador import *
from Mesa import *


class AbstractControladorJogo(ABC):
    '''
    Retorna a lista de personagems
    @return a lista de personagems
    '''
    @property
    @abstractmethod
    def personagems(self) -> list:
        pass

    @property
    @abstractmethod
    def baralho(self) -> list:
        pass

    @abstractmethod
    def inclui_personagem_na_lista(self, energia: int, habilidade: int,
                                velocidade: int, resistencia: int,
                                tipo: Tipo) -> Personagem:
        pass

    @abstractmethod
    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        pass

    @abstractmethod
    def jogada(self, mesa: Mesa) -> Jogador:
        pass
