from abc import ABC, abstractmethod
from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        self.__nome = nome
        self.__cartas = []

    @property
    def nome(self) -> str:
        return self.__nome

    def baixa_carta_da_mao(self) -> Carta:
        if self.__cartas:
            posicao_carta_ah_remover = random.randint(0, len(self.__cartas) - 1)
            carta_ah_remover = self.__cartas[posicao_carta_ah_remover]
            self.__cartas.remove(carta_ah_remover)
            return carta_ah_remover

    @property
    def mao(self) -> list:
        return self.__cartas

    def inclui_carta_na_mao(self, carta:Carta):
        if isinstance(carta, Carta):
            self.__cartas.append(carta)
