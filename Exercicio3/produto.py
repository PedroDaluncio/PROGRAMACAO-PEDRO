from cliente import Cliente
from categoria_produto import CategoriaProduto


class Produto():
    def __init__(self, codigo, descricao, quantidade, preco_unitario, categoria_produto, cliente):
        self.__codigo = None
        self.__descricao = None
        self.__quantidade = None
        self.__preco_unitario = None
        self.__categoria_produto = None
        self.__cliente = None
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(quantidade, int):
            self.__quantidade = quantidade
        if isinstance(preco_unitario, float):
            self.__preco_unitario = preco_unitario
        if isinstance(categoria_produto, CategoriaProduto):
            self.__categoria_produto = CategoriaProduto
        if isinstance(cliente, Cliente):
            self.__cliente = Cliente

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
        return self.__descricao

    @property
    def categoria_produto(self):
        return self.__categoria_produto

    @categoria_produto.setter
    def categoria_produto(self, categoria_produto):
        self.__codigo = categoria_produto
        return self.__categoria_produto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
        return self.__quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario
        return self.__preco_unitario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
        return self.__cliente
