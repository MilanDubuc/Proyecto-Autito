import time
import os

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
        self.__velocidad = self.__velocidad + self.__aceleracion * direccion * frameTime
        
framerate = 60
frameTime = 1/framerate
frameReset = time.time()
golcito = Auto(1500, 3000, 190, 99)
while (time.time() - frameReset) < (frameTime):                      #fps cycle
    print(golcito.get_pos())
    print("    ^W\nA<-- -->D\n    vS\n")
    while (True):       
        entrada = getkey()
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
        else:
            entrada = None