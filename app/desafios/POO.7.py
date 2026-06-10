# questoes de POO, questão 7 08/06/2026

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome):
        self.contatos.append(nome)

    def listar_contatos(self):
        print(self.contatos)


agenda = Agenda()

agenda.adicionar_contato("João")
agenda.adicionar_contato("Maria")

agenda.listar_contatos()