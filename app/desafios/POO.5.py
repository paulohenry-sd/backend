#questões de POO, questão 5 08/06/2026
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True


livro1 = Livro("Dom Casmurro")

print(livro1.disponivel)  # True

livro1.emprestar()
print(livro1.disponivel)  # False

livro1.devolver()
print(livro1.disponivel)  # True