from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__lista_clientes = []
        self.__lista_tecnicos = []

    @property
    def clientes(self):
        return self.__lista_clientes

    @property
    def tecnicos(self):
        return self.__lista_tecnicos

    def inclui_cliente(self, codigo: int, nome: str):
        if isinstance(codigo, int) and isinstance(nome, str):
            if self.__lista_clientes:
                for cliente in self.__lista_clientes:
                    if cliente.codigo == codigo:
                        return
            self.__lista_clientes.append(Cliente(nome, codigo))
            return self.__lista_clientes[-1]

    def inclui_tecnico(self, codigo: int, nome: str):
        if isinstance(codigo, int) and isinstance(nome, str):
            if self.__lista_tecnicos:
                for tecnico in self.__lista_tecnicos:
                    if tecnico.codigo == codigo:
                        return
            self.__lista_tecnicos.append(Tecnico(nome, codigo))
            return self.__lista_tecnicos[-1]
