nome = "Gabriel"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.548

dados = {"nome": "Gabriel", "idade": 28}

print("nome: %s Idade: %d" %(nome,idade))
print("nome: {} Idade {}".format(nome,idade))

print("nome: {1} Idade {0}".format(idade,nome))
print("nome{1} Idade{0} Nome: {1}".format(idade,nome))

print("nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("name: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("nome: {nome} Idade: {idade}".format(**dados))

print(f"nome: {nome} Idade: {idade}")
print(f"nome: {nome} Idade: {idade} saldo: {saldo:.2f}")
print(f"nome: {nome} Idade: {idade} saldo: {saldo:10.1f}")
