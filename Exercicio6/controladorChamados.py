from datetime import date as Date
from collections import defaultdict
from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from cliente import Cliente
from tecnico import Tecnico


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__lista_chamados = []
        self.__lista_tipos_chamado = []

    def total_chamados_por_tipo(self, tipo: TipoChamado):
        qt_chamados_do_tipo = 0
        if isinstance(tipo, TipoChamado):
            if self.__lista_chamados:
                for chamado in self.__lista_chamados:
                    if chamado.tipo == tipo:
                        qt_chamados_do_tipo += 1
            return qt_chamados_do_tipo

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str):
        if isinstance(codigo, int) and isinstance(nome, str) and \
                isinstance(descricao, str):
            if self.__lista_tipos_chamado:
                for tipo_chamado in self.__lista_tipos_chamado:
                    if tipo_chamado.codigo == codigo:
                        return
            self.__lista_tipos_chamado.append(
                TipoChamado(codigo, descricao, nome))
            return self.__lista_tipos_chamado[-1]

    def inclui_chamado(self, data: Date, cliente: Cliente,
                       tecnico: Tecnico, titulo: str, descricao: str,
                       prioridade: int, tipo: TipoChamado):
        if isinstance(data, Date) and isinstance(cliente, Cliente) and \
                isinstance(tecnico, Tecnico) and isinstance(titulo, str) and \
            isinstance(descricao, str) and isinstance(prioridade, int) \
                and isinstance(tipo, TipoChamado):
            if self.__lista_chamados:
                for chamado in self.__lista_chamados:
                    if chamado.data == data and chamado.cliente == cliente \
                            and chamado.tecnico == tecnico and chamado.tipo == tipo:
                        return
            self.__lista_chamados.append(Chamado(data, cliente, tecnico,
                                                 titulo, descricao,
                                                 prioridade, tipo))
            return self.__lista_chamados[-1]

    @property
    def tipos_chamados(self):
        return self.__lista_tipos_chamado
