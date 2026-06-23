from django.shortcuts import render

 def home(request):
    mensagem = ""
    conteudo = False

    if request.metod == "POST":
        idade_raw = request.POST.get("idade", "")
        try:
            idade = int(idade_raw)
        except (ValueError, TypeError):
            mensagem = "Por favor insira uma idade valida."
        else:
            if idade >= 18:
                conteudo = True
            else:
                mensagem = "Você é menor de idade. Acesso não permitido"

    return render(
        request,
        "index.html",
        {
            "mensagem": mensagem,
            "conteudo": conteudo
        }
    )