def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}"for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
        "Domingo, 15 de Setembro de 2024",
        "Zen of Python",
        "Beutiful is better than ugly.",
        "Explicit is better than complex.",
        "Simple is better than complex.",

        autor="Tim Peters",
        ano=1999,
    )