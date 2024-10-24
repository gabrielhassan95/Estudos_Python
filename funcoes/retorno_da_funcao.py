def calcular_total(n1,n2,n3):
    return sum(n1+n2+n3)
def exibir_resultado(n1, n2, n3,funcao):
    resultado = funcao(n1,n2,n3)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor
n1 = (int(input("Digite um número: ")))
n2 = (int(input("Digite um número: ")))
n3 = (int(input("Digite um número: ")))
resultado = n1+n2+n3
print(f"Soma de {n1,n2,n3} é {resultado}")

numero = (int(input("Digite um número: ")))
print("Antecessor e sucessor do número", (numero), "é",retorna_antecessor_e_sucessor(numero))