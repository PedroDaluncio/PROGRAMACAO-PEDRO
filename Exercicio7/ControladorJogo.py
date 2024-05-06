from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__personagems = []
        self.__baralho = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagems

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        if isinstance(energia, int) and isinstance(habilidade, int) and \
            isinstance(velocidade, int) and isinstance(resistencia, int) \
            and isinstance(tipo, Tipo):
            self.__personagems.append(Personagem(energia, habilidade,
                                                 velocidade, resistencia, tipo))
            return self.__personagems[-1]

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        if isinstance(personagem, Personagem):
            self.__baralho.append(Carta(personagem))
            return self.__baralho[-1]

    '''
    Realiza uma jogada, ou seja:
    1. Recebe a mesa onde estao as cartas lancadas pelo Jogador 1
    e pelo Jogador 2

    2. Compara os valores totais das cartas dos jogadores que estao
    na mesa
    - O jogador que ganhar a rodada recebe a carta do jogador perdedor,
    sendo assim ele deve chamar o metodo inclui_carta_na_mao para as
    duas cartas que estao na mesa
    - Caso ocorra empate ambos os jogadores devem chamar o metodo
    inclui_carta_na_mao com suas respectivas cartas da mesa

    3.Ao final do metodo o jogador que estiver com a mao vazia
    perde o jogo (retornar o jogador vencedor). Caso ambos ainda tenham
    cartas na mao retorne None para indicar que ninguem venceu o jogo.

    @param mesa Mesa atual, contendo: Jogador 1, Jogador 2,
    Carta do Jogador 1 e Carta do Jogador 2

    @return Retorna o Jogador vencedor da rodada.
    Caso ocorra empate entre os jogadores, retorna None
    '''

    def jogada(self, mesa: Mesa) -> Jogador:
        if isinstance(mesa, Mesa):
            cartas_jogador1 = mesa.carta_jogador1
            cartas_jogador2 = mesa.carta_jogador2
            if cartas_jogador1.valor_total_carta > cartas_jogador2.valor_total_carta:
                

