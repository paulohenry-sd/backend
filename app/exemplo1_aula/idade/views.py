from django.shortcuts import render

def home(request):
    mensagem =""
    conteudo = False

    if request.metod == "POST":
        idade = int(request.POST.get("idade"))

        if idade>=18:
            conteudo = True
        else:
            mensagem = "você não permitido."

        return render(
            request,
            "index.html",
            {
                "mensagem": mensagem,
                "conteudo": conteudo
            }
        )