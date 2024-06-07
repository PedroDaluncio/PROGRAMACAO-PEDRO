

class ComandoInvalidoException(Exception):
    def __init__(self):
        self.mensagem = "COMANDO INVALIDO"
        super().__init__(self.mensagem)
