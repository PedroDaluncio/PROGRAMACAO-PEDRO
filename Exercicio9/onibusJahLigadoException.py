

class OnibusJahLigadoException(Exception):
    def __init__(self):
        super().__init__("O ônibus já está ligado")
