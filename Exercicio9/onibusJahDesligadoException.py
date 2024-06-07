

class OnibusJahDesligadoException(Exception):
    def __init__(self):
        self.mensagem = "O ônibus já está desligado!"
        super().__init__(self.mensagem)
