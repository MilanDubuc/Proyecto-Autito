import time
import os
import pygame

#inicializacion:
pygame.init()
pygame.display.set_mode([100, 100])
framerate = 10  #fps
frameTime = 1/framerate

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
    
    def get_vel(self):
        return self.__velocidad
    
    def acelerar(self, direccion):
        self.__velocidad = self.__velocidad + self.__aceleracion * direccion * frameTime


while True:
    frameReset = time.time()
    golcito = Auto(1500, 3000, 190, 99)
    while (time.time() - frameReset) < (frameTime):                      #fps cycle
        os.system("cls")
        print(golcito.get_pos())
        print(golcito.get_vel())
        print("    ^W\nA<-- -->D\n    vS\n")
        while (True):       
            entrada = pygame.key.get_pressed()
            if entrada[pygame.K_a]:
                golcito.acelerar([-1,0])
            elif entrada[pygame.K_d]:
                golcito.acelerar([1,0])
            elif entrada[pygame.K_w]:
                golcito.acelerar([0,1])
            elif entrada[pygame.K_s]:
                golcito.acelerar([0,-1])
            elif entrada[pygame.K_ESCAPE]:
                break
            else:
                entrada = None
        break