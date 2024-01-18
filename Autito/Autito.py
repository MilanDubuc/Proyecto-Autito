import os

mundo = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pos_x = 0
pos_y = 0
class Auto:
    def __init__(self, peso, aceleracion, velocidadMaxima, agarre):
        self.peso = peso
        self.aceleracion = aceleracion
        self.velocidadMaxima = velocidadMaxima
        self.agarre = agarre


def acelerar_x():
    global pos_x
    pos_x += 1       
def frenar_x():
    global pos_x
    pos_x -= 1
def acelerar_y():
    global pos_y
    pos_y -= 1       
def frenar_y():
    global pos_y
    pos_y += 1
                    

def render():
    global mundo
    pantalla = mundo.copy()
    pantalla[pos_y][pos_x] = "X"
    
    for i in range(len(pantalla)):
        print(pantalla[i])
    
while True:
    os.system("cls")
    render()
    entrada = input("    ^W\nA<-- -->D\n    vS\n")
    if entrada == "a":
        frenar_x()
    elif entrada == "d":
        acelerar_x()
    elif entrada == "w":
        acelerar_y()
    elif entrada == "s":
        frenar_y()
    elif entrada == "stop":
        break