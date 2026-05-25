class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def estudar(self):
        print(self.nome, "está estudando!")

aluno1 = Aluno("Maria")

aluno1.estudar()