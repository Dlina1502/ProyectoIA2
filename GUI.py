import copy
from operator import truediv
from sys import maxsize
from textwrap import fill
import tkinter as tk
from tkinter import Button, Canvas, Entry, Label, ttk
from typing_extensions import IntVar

from defer import return_value
from requests import delete
import State
import IA

class App():

    def __init__(self, L_CUADRO):
        self.gs = State.GameState()
        self.tablero = self.gs.piezas
        self.L_CUADRO = L_CUADRO
        self.imagenes = {}


        self.anteriorXJ2 = self.gs.xJugador
        self.anteriorYJ2 = self.gs.yJugador

        self.anteriorXM = self.gs.xMaquina
        self.anteriorYM = self.gs.yMaquina

        self.remainingGrass = self.gs.remainingGrass
        self.remainingFlowers = self.gs.remainingFlowers
        self.remainingApples = self.gs.remainingApples

        #print(self.posXJ2," / ", self.posYJ2)
        self.turno = 1

        self.puntosJM = 0
        self.puntosJH = 0

        self.ventana = tk.Tk()
        self.ventana.title("Hungry Horses")

        # AnchoxAlto
        #self.ventana.configure(background='pink')
        self.ventana.geometry(f"{str(L_CUADRO * 15)}x{str(L_CUADRO * 9)}")
        self.ventana.resizable(0,0)
        self.interfaz = tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)

        #Valores ingresados por el jugador 
        self.filaX = tk.IntVar()
        self.filaY = tk.IntVar()

    def __call__(self):
        self.ventana.mainloop()

    def moverJ2(self):
        pass

    def winCheck(self):
        if(self.remainingGrass == 0 and self.remainingFlowers==0 and self.remainingApples==0):
            print("humano: ", self.puntosJH, " maquina: ", self.puntosJM)
            return True
        else:
            print("humano: " , self.puntosJH , " maquina: " , self.puntosJM)
            return False

    def elementosVentana(self):
        filaX = 0
        filaY = 0
        texto1 = tk.Label(self.ventana, text = "Ingresa la posición donde quieres \nmover el caballo:", font='Helvetica 16')
        texto1.place (x=670, y=60)

        textoX=  tk.Label(self.ventana, text = "Posición en fila :", font='Helvetica 15')
        textoX.place (x=650, y=200)

        textoY=  tk.Label(self.ventana, text = "Posición en columna :", font='Helvetica 15')
        textoY.place (x=650, y=270)

        cajaX = Entry(self.ventana, textvariable=self.filaX)
        cajaX.place (x=850, y =200)

        cajaY = Entry(self.ventana, textvariable=self.filaY)
        cajaY.place (x=850, y =270)

        botonPos = Button(self.interfaz, text= "Jugar movida", command= self.movHumano)
        botonPos.place(x=780, y=500)

    def dibujarTablero(self):
        # p = pasto, f = flor, m = manzana, jH = jugador humano, jM = jugador máquina
        numerosX = "        0       1        2        3        4        5        6        7"
        numerosy = "0\n\n\n1\n\n\n2\n\n\n3\n\n\n4\n\n\n5\n\n\n6\n\n\n7"


        for i in range(8):
            for j in range(8):
                self.interfaz.create_rectangle((i*self.L_CUADRO)+50, (j*self.L_CUADRO)+50, ((i+1)*self.L_CUADRO)+50, ((j+1)*self.L_CUADRO)+50, fill="#ffffff")
        lblposx = tk.Label(self.ventana, text = numerosX, justify=tk.CENTER, font='Helvetica 19 bold')
        lblposy = tk.Label(self.ventana, text = numerosy, justify=tk.CENTER, font='Helvetica 18 bold')
        lblposx.place(x=0,y=0,width=610,height=50)
        lblposy.place(x=0,y=30,width=50,height=610)

    def cargarImagenes(self):
        piezas = ["p", "f", "m", "jM", "jH"]
        for pieza in piezas:
            self.imagenes[pieza] = tk.PhotoImage(file="./iconos/"+pieza+".png")
        self.mostrarPiezas(self.tablero)

    def mostrarPiezas(self, tablero):
        for indice_i, i in enumerate(tablero):
            for indice_j, j in enumerate(i):
                if j != "--":
                    indice_j2 = indice_j +1
                    indice_i2 = indice_i +1
                    self.interfaz.create_image((indice_j2*self.L_CUADRO)-20, (indice_i2*self.L_CUADRO)-20, image=self.imagenes[j], anchor="nw")


    def setTurno(self, bool):
        if(bool):
            turno = -1
        else:
            turno = 1

        #self.movHumano()


    def movHumano(self):
        auxX = 0
        auxY = 0

        self.posXJ2 = self.filaX.get()
        self.posYJ2 = self.filaY.get()
        
        #Movimiento 1
        if (self.posXJ2<8 and self.posYJ2<8 and self.posXJ2>=0 and self.posYJ2 >= 0 and (not self.winCheck())):
            if(self.posYJ2 == self.anteriorYJ2+1 and self.posXJ2 == self.anteriorXJ2+2):
                auxX = self.posXJ2
                auxY = self.posYJ2

                self.validarMov(auxX, auxY, self.anteriorXJ2, self.anteriorYJ2)
                print(auxX," / ", auxY)
            elif(self.posYJ2 == self.anteriorYJ2-1 and self.posXJ2 == self.anteriorXJ2-2):
                auxX = self.posXJ2
                auxY = self.posYJ2

                self.validarMov(auxX, auxY, self.anteriorXJ2, self.anteriorYJ2)
                print(auxX," / ", auxY)
            elif(self.posYJ2 == self.anteriorYJ2+1 and self.posXJ2 == self.anteriorXJ2-2):
                auxX = self.posXJ2
                auxY = self.posYJ2

                self.validarMov(auxX, auxY, self.anteriorXJ2, self.anteriorYJ2)
                print(auxX," / ", auxY)
            elif(self.posYJ2 == self.anteriorYJ2+2 and self.posXJ2 == self.anteriorXJ2-1):
                auxX = self.posXJ2
                auxY = self.posYJ2

                self.validarMov(auxX, auxY, self.anteriorXJ2, self.anteriorYJ2)
                print(auxX," / ", auxY)
            elif(self.posYJ2 == self.anteriorYJ2+2 and self.posXJ2 == self.anteriorXJ2+1):
                auxX = self.posXJ2
                auxY = self.posYJ2

                self.validarMov(auxX, auxY, self.anteriorXJ2, self.anteriorYJ2)
                print(auxX," / ", auxY)
            elif(self.posYJ2 == self.anteriorYJ2-1 and self.posXJ2 == self.anteriorXJ2+2):
                auxX = self.posXJ2
                auxY = self.posYJ2             

                self.validarMov(auxX, auxY, self.anteriorXJ2, self.anteriorYJ2)
                print(auxX," / ", auxY)
            elif(self.posYJ2 == self.anteriorYJ2-2 and self.posXJ2 == self.anteriorXJ2+1):
                auxX = self.posXJ2
                auxY = self.posYJ2          
                
                self.validarMov(auxX, auxY, self.anteriorXJ2, self.anteriorYJ2)
                print(auxX," / ", auxY)
            elif(self.posYJ2 == self.anteriorYJ2-2 and self.posXJ2 == self.anteriorXJ2-1):
                auxX = self.posXJ2
                auxY = self.posYJ2

                self.validarMov(auxX, auxY, self.anteriorXJ2, self.anteriorYJ2)
                print(auxX," / ", auxY)
            else:
                print("EERRROOOOOR")
        else:
            print("EERRROOOOOR")
    
    def validarMov(self, x, y, xAnt, yAnt):

        if (self.tablero[x][y]== "--"):
            print("ENTRA")
            self.tablero[x][y]= "jH"
            self.tablero[xAnt][yAnt]= "--"

            self.anteriorXJ2 = x
            self.anteriorYJ2 = y

        elif (self.tablero[x][y]== "p"):
            self.tablero[x][y]= "jH"
            self.tablero[xAnt][yAnt]= "--"
            self.puntosJH = self.puntosJH + 1

            self.anteriorXJ2 = x
            self.anteriorYJ2 = y
        elif (self.tablero[x][y]== "f"):
            self.tablero[x][y]= "jH"
            self.tablero[xAnt][yAnt]= "--"
            self.puntosJH = self.puntosJH + 3

            self.anteriorXJ2 = x
            self.anteriorYJ2 = y
        elif (self.tablero[x][y]== "m"):
            self.tablero[x][y]= "jH"
            self.tablero[xAnt][yAnt]= "--"
            self.puntosJH = self.puntosJH + 5

            self.anteriorXJ2 = x
            self.anteriorYJ2 = y
        else:
            print("error, es la casilla del otro jugador")


        maquina = IA.Node(self.turno, 5, self.tablero[:], self.anteriorXJ2, self.anteriorYJ2, self.puntosJH ,self.anteriorXM, self.anteriorYM, self.puntosJM, self.remainingGrass,
        self.remainingFlowers, self.remainingApples, 0)

        

        bestChoice, bestValue = self.minimax(maquina, 5, -self.turno)
        self.tablero = maquina.children[bestChoice].getBoard()
        self.remainingGrass = maquina.children[bestChoice].getRemaininGrass()
        self.remainingFlowers = maquina.children[bestChoice].getRemaininFlowers()
        self.remainingApples = maquina.children[bestChoice].getRemaininApples()

        self.anteriorXM = maquina.children[bestChoice].getPosXM()
        self.anteriorYM = maquina.children[bestChoice].getPosYM()

        self.puntosJM = maquina.children[bestChoice].getPuntosJM()


        self.winCheck()

        print(x,y)
        print(self.tablero)
        self.interfaz.delete("all")
        self.dibujarTablero()
        self.mostrarPiezas(self.tablero)

    
    def minimax(self, node, depth, player):

        if (depth == 0 or abs(node.value) == maxsize):
            return None ,node.value

        bestChoice = -1000
        
        if (player == -1):
            maxValue = -maxsize
            for i in range(len(node.children)):
                child = node.children[i]
                val = self.minimax(child, depth - 1, -player)[1]
                if (val > maxValue):
                    maxValue = val
                    bestChoice = copy.deepcopy(i)
            return bestChoice, maxValue
        else:
            minValue = maxsize
            for i in range(len(node.children)):
                child = node.children[i]
                val = self.minimax(child, depth - 1, -player)[1]
                if (val < minValue):
                    minValue = val
                    bestChoice = copy.deepcopy(i)
            return bestChoice, minValue






MotorJuego = App(70)
MotorJuego.setTurno(False)
MotorJuego.elementosVentana()
MotorJuego.dibujarTablero()
MotorJuego.cargarImagenes()
#MotorJuego.mostrarPiezas()

MotorJuego()
