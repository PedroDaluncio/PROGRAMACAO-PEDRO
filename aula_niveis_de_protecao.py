


class Aluno:
    def __init__(self,matricula: int,nome: str):
        self.__matricula = matricula
        self.__nome = nome

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self,matricula):
        if matricula > 0:
            self.__matricula = matricula
        else:
            #retorna um erro
            raise Exception('comando inválido')
        return self.__matricula