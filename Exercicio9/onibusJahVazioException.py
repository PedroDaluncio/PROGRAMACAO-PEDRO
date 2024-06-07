

class OnibusJahVazioException(Exception):
    def __init__(self):
        self.mensagem = "O ônibus já está vazio"
        super().__init__(self.mensagem)
