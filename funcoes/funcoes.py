def exibir_mensagem():
    print("Olá mudo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!") 

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")



exibir_mensagem()       
exibir_mensagem_2(nome="Gabriel")
exibir_mensagem_3(nome="Hassan")