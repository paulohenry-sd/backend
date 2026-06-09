#questões de POO, questão 5 08/06/2026

class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.disponivel = ()

pessoa1 = livro()


    def emprestar(self):
        if self.disponivel:
            print(f"O livro {self.titulo} já está emprestado.")
        else:
            self.disponivel = True
            print(f"O livro {self.titulo} foi emprestado com sucesso.")