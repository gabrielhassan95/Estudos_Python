class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"        

class Mamifero(Animal):
     def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        
class Ave(Animal):
     def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__( **kw)
                
#class Cachorro(Mamifero):
#    pass
#class Gato(Mamifero):
#    pass
#class Leao(Mamifero):
#    pass


class Pombo(Ave):
    pass

#gato = Gato ( 4, " branco")
#print(gato)

#cachorro = Cachorro( 4, " amarelo")
#print(cachorro)

#leao = Leao( 4," amarelo e marrom")
#print(leao)



pombo = Pombo(nro_patas=2, cor_bico="vermelho")
print(pombo)