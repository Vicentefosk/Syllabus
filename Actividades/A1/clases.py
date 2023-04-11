from abc import ABC, abstractmethod
from secrets import choice



class Animal(ABC):

    def __init__(self, peso, nombre, *args,**kwargs):
        self.peso = peso
        self.nombre = nombre
        self.__energia = 100
        self.__identificador = 0

    @abstractmethod
    def desplazarse(self):
        pass   
    @property
    def energia(self, __energia):       
        if self.__energia >= 0:
            return self.energia       
        else:
            return None
class Terrestre(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cantidad_patas = 4

    @property
    def energia_gastada_por_desplazamiento(self):
        energia_requerida = (self.peso*5)
        return energia_requerida
    @property
    def desplazarse(self):
        caminar=print("caminando...")
        self.energia -= Terrestre.energia_gastada_por_desplazamiento
        return caminar


class Acuatico(Animal):
    @property
    def energia_gastada_por_desplazamiento(self):
        energia_requerida= (self.peso*2)
        return energia_requerida
    @property
    def desplazarse(self):
        nadar = print("nadando...")
        self.__energia -= Acuatico.energia_gastada_por_desplazamiento
        return nadar

class Perro(Terrestre):
    def ladrar(self):
        guau=print("guau guau")
        return guau

class Pez(Acuatico):
    def nadar(self):
        nadar=print("moviendo aleta")
        return nadar
    

class Ornitorrinco(Terrestre,Acuatico):
    def desplazarse(self):
        energia_requerida = ((self.peso*2)+(self.peso*5))//2
        return energia_requerida


if __name__ == '__main__':
    perro = Perro(nombre='Pongo', raza='Dalmata', peso=3)
    pez = Pez(nombre='Nemo', color='rojo', peso=1)
    ornitorrinco = Ornitorrinco(nombre='Perry', peso=2)

    perro.desplazarse()
    pez.desplazarse()
    ornitorrinco.desplazarse()