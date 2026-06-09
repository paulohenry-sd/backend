#questões de POO, questão 2 08/06/2026

class aluno:
    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia
    def apresentar(self):
        print(f"nome do individuo: {self.nome}, materia que estuda: {self.materia}")
aluno1 = aluno("João", "Matemática")
aluno1.apresentar()

aluno2 = aluno("Maria", "Português")
aluno2.apresentar()

aluno3 = aluno("Carlos", "História")
aluno3.apresentar()