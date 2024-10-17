class Passaro:
    def voar(self):
        print("Voando..")
        
class Pardal(Passaro):
    def voar(self):
        #super().voar() método para pegar direto do "pai"
        print("Pardal está voando")
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")         
# FIXME: exemplo ruim para ganhar o metodo ganhar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando")


def plano_voo(obj):
    obj.voar()
    
plano_voo(Aviao())    
plano_voo(Pardal())  
plano_voo(Avestruz())
                