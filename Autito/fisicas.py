import time

class Auto:
    def __init__(self, peso, torque, velocidadMaxima, agarre):
        self.peso = peso
        self.torque = torque
        self.velocidadMaxima = velocidadMaxima
        self.agarre = agarre
        self.__aceleracion = torque/peso
        self.__posicion = [0,0]
        self.__velocidad = [0,0]
        
    def get_pos(self):
        return self.__posicion
    
    def acelerar(self, direccion, inicio):
        self.__velocidad = self.__velocidad + self.__aceleracion * direccion * (time.time() - inicio)
        

frameReset = time.time()
while (time.time() - frameReset) < (1/60):                      #60 fps cycle
    golcito = Auto(1500, 3000, 190, 99)
    while (True):
        entrada = input("    ^W\nA<-- -->D\n    vS\n")
        inicio = time.time()
        if entrada == "a":
            golcito.acelerar([-1,0], inicio)
        elif entrada == "d":
            golcito.acelerar([1,0], inicio)
        elif entrada == "w":
            golcito.acelerar([0,1], inicio)
        elif entrada == "s":
            golcito.acelerar([0,-1], inicio)
        elif entrada == "stop":
            break