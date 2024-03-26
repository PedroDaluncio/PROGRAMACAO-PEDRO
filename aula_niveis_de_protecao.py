


class Aluno:
    def __init__(self,matricula: int,nome: str):
        self.__matricula = matricula
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self,matricula):
        if matricula > 0:
            self.__matricula = matricula
        else:
            #o raise Exception faz um erro ocorrer
            raise Exception('comando inválido')
        return self.__matricula