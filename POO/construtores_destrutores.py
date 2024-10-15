class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print(" Inicializando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print("Removendo a instância da classe")
        
    def falar(self):
        print("auauuu")
    def __str__(self):
        return f"Cachorro: nome={self.nome} cor={self.cor}"    
        
def criar_cachorro():
    c = Cachorro("Zeus", "Branco e Preto,", False)       
    print(c)    
#c = Cachorro("Chappie", "amarelo")
#c.falar()    
criar_cachorro()           