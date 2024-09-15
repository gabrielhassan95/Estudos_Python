nome = "gabriel"


print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá mundo!   "

print(texto + ".") 
print(texto.strip() + ".")
print(texto.lstrip())
print(texto.rstrip())


menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-Y-T-H-O-N")

for letra in menu:
    print(letra, end="-")
print()

print("-".join(menu))
print(texto.strip() + ".")
print(texto.rstrip())