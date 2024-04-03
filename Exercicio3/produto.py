from cliente import Cliente
from categoria_produto import CategoriaProduto


class Produto():
    def __init__(self, codigo, descricao, categoria_produto):
        self.__codigo = None
        self.__descricao = None
        self.__categoria_produto = None
        self.__quantidade = 0
        self.__preco_total = 0
        self.__preco_unitario = 0
        self.__cliente = Cliente
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(categoria_produto, CategoriaProduto):
            self.__categoria_produto = categoria_produto

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def categoria_produto(self):
        return self.__categoria_produto

    @categoria_produto.setter
    def categoria_produto(self, categoria_produto):
        self.__codigo = categoria_produto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    def preco_total(self):
        self.__preco_total = float(self.__preco_unitario * self.__quantidade)
        return self.__preco_total
