from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
    @property
    @abstractproperty
    def marca(self):
        pass
        
    
class ControleTv(ControleRemoto):
    def ligar(self):
        print("ligando")
        
    def desligar(self):
        print("Desligando")
    @property
    def marca(self):
        return "LG"    

class ControleArcondicionado(ControleRemoto):
    def ligar(self):
        print("ligar ar condicionado")
        
    def desligar(self):
        print("Deligando ar condiconado")    
    @property
    def marca(self):
        return "Dell"    



controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArcondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)