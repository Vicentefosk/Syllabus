from abc import ABC, abstractmethod
from secrets import choice



class Animal(ABC):

    def __init__(self,peso,nombre,energia,identificador):
        self.peso = peso
        self.nombre=nombre
        self.__energia=100
        self.identificador=identificador
    
    @abstractmethod
    def desplazarse(self):
        pass
    
    @property
    def energia(self,energia):
        if self.energia >= 0:
            return self.energia
        
        else:
            return None


class Terrestre(Animal):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.cantidad_patas=cantidad_patas

    def energia_gastada_por_desplazamiento(self):
        peso = self.peso
        energia_requerida = (peso*5)
        return energia_requerida
    
    def desplazarse(self):
        caminar=print("caminando...")
        self.energia -= Terrestre.energia_gastada_por_desplazamiento
        return caminar


class Acuatico(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def energia_gastada_por_desplazamiento(self):
        peso=self.peso
        energia_requerida= (peso*2)
        return energia_requerida
    def desplazarse(self):
        nadar = print("nadando...")
        self.energia -= Acuatico.energia_gastada_por_desplazamiento
        return nadar

class Perro(Terrestre):
    def __init__(*args,**kwargs):
        super().__init__(self, *args, **kwargs)
        self.raza=raza
    
    def ladrar(self):
        guau=print("guau guau")
        return guau

class Pez(Acuatico):
    def __init__(self,*args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.color=color

    def nadar(self):
        nadar=print("moviendo aleta")
        return nadar
    

class Ornitorrinco(Terrestre,Acuatico):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        
    def desplazarse(self):
        peso=self.peso
        energia_requerida = ((peso*2)+(peso*5))//2
        return energia_requerida


if __name__ == '__main__':
    perro = Perro(nombre='Pongo', raza='Dalmata', peso=3)
    pez = Pez(nombre='Nemo', color='rojo', peso=1)
    ornitorrinco = Ornitorrinco(nombre='Perry', peso=2)

    perro.desplazarse()
    pez.desplazarse()
    ornitorrinco.desplazarse()