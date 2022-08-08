from platform import node
import random
from math import inf

from sys import maxsize
import gc

import copy
from typing_extensions import Self

class Node(object):
    # player es un entero 1 para humano -1 para maquina
    def __init__(self, player, depth, board, posXJ, posYJ, puntosJH, posXM, posYM, puntosJM, remainingGrass, remainingFlowers, remainingApples, value, primerMov):
        
        self.player = player
        self.depth = depth
        self.depthIni = depth

        self.board = board
        self.posXJ = posXJ
        self.posYJ = posYJ
        self.puntosJH = puntosJH

        self.primerMov = primerMov

        self.posXM = posXM
        self.posYM = posYM
        self.puntosJM = puntosJM

        self.remaininGrass = remainingGrass
        self.remainingFlowers = remainingFlowers
        self.remainingApples = remainingApples

        self.value = self.evaluar(self.depth, self.primerMov, self.player)
        print("profundidad: ", depth, " heuristica: ", self.value)
        self.children = []
        self.createChildren()

    def getRemaininGrass(self):
        return self.remaininGrass


    def getRemaininFlowers(self):
        return self.remainingFlowers

    def getRemaininApples(self):
        return self.remainingApples

    def getPuntosJM (self):
        return self.puntosJM

    def getPosXM(self):
        return self.posXM
    
    def getPosYM(self):
        return self.posYM

    def getBoard(self):
        return self.board

    def evaluar(self, depth, primerMov, player):
        if primerMov:
            if depth == self.depthIni-1 and player == -1:
                return self.puntosJM*10 - self.puntosJH
            elif depth == self.depthIni-2 and player == 1:
                return self.puntosJM - self.puntosJH*10
            else:
                return self.puntosJM - self.puntosJH
        else:
            return self.puntosJM - self.puntosJH
            
        

    def createChildren(self):
        possibleMoves = [1, 2, 3, 4, 5, 6, 7, 8] #[1, 2, 3, 4, 5, 6, 7, 8]
        if self.depth > 0:
            for i in possibleMoves:
                if (i == 1):
                    
                    aux = self.player * (-1)
                    #m es una variable que identifica con 0 si el nodo no se movio
                    
                    m = self.arribaDerecha(aux)

                elif (i == 2):
                    
                    aux = self.player * (-1)
                   
                    m = self.arribaIzquierda(aux)
                    
                elif (i == 3):

                    aux = self.player * (-1)
                    
                    m = self.derechaArriba(aux)
                    

                    
                elif (i == 4):
                    aux = self.player * (-1)
                    
                    m = self.derechaAbajo(aux)
                    

                    
                elif (i == 5):
                    aux = self.player * (-1)
                    
                    m = self.abajoDerecha(aux)

                elif (i == 6):
                    aux = self.player * (-1)
                    
                    m = self.abajoIzquierda(aux)
    
                elif (i == 7):
                    aux = self.player *(-1)
                    
                    m = self.izquierdaArriba(aux)
                elif (i == 8):
                    aux = self.player * (-1)
                    
                    m = self.izquierdaAbajo(aux)
                    
                
                

    def arribaDerecha(self, aux):
        if (aux == 1):
            if (self.posXJ-2 < 8 and self.posYJ+1 < 8 and self.posXJ-2 >= 0 and self.posYJ+1 >= 0):
                
                
                auxX = self.posXJ-2
                auxY = self.posYJ+1
                self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
                
            else:
                return 0
        else:
            if (self.posXM-2 < 8 and self.posYM+1 < 8 and self.posXM-2 >= 0 and self.posYM+1 >= 0):
                auxX = self.posXM-2
                auxY = self.posYM+1
                self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
            else:
                return 0

    def arribaIzquierda(self, aux):
        if (aux == 1):
            
            if (self.posXJ-2 < 8 and self.posYJ-1 < 8 and self.posXJ-2 >= 0 and self.posYJ-1 >= 0):
                auxX = self.posXJ-2
                auxY = self.posYJ-1
                self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
            else:
                return 0
        else:
            if (self.posXM-2 < 8 and self.posYM-1 < 8 and self.posXM-2 >= 0 and self.posYM-1 >= 0):
                auxX = self.posXM-2
                auxY = self.posYM-1
                self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
            else:
                return 0

    def derechaArriba(self, aux):
        if (aux == 1):
            if (self.posXJ-1 < 8 and self.posYJ+2 < 8 and self.posXJ-1 >= 0 and self.posYJ+2 >= 0):
                auxX = self.posXJ-1
                auxY = self.posYJ+2
                self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
            else:
                return 0
        else:
            if (self.posXM-1 < 8 and self.posYM+2 < 8 and self.posXM-1 >= 0 and self.posYM+2 >= 0):
                auxX = self.posXM-1
                auxY = self.posYM+2
                self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
            else:
                return 0

    def derechaAbajo(self, aux):
        if (aux == 1):
            if (self.posXJ+1 < 8 and self.posYJ+2 < 8 and self.posXJ+1 >= 0 and self.posYJ+2 >= 0):
                auxX = self.posXJ+1
                auxY = self.posYJ+2
                self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
            else:
                return 0
        else:
            if (self.posXM+1 < 8 and self.posYM+2 < 8 and self.posXM+1 >= 0 and self.posYM+2 >= 0):
                auxX = self.posXM+1
                auxY = self.posYM+2
                self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
            else:
                return 0

    def abajoDerecha(self, aux):
        if (aux == 1):
            if (self.posXJ+2 < 8 and self.posYJ+1 < 8 and self.posXJ+2 >= 0 and self.posYJ+1 >= 0):
                auxX = self.posXJ+2
                auxY = self.posYJ+1
                self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
            else:
                return 0
        else:
            if (self.posXM+2 < 8 and self.posYM+1 < 8 and self.posXM+2 >= 0 and self.posYM+1 >= 0):
                auxX = self.posXM+2
                auxY = self.posYM+1
                self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
            else:
                return 0

    def abajoIzquierda(self, aux):
        if (aux == 1):
            if (self.posXJ+2 < 8 and self.posYJ-1 < 8 and self.posXJ+2 >= 0 and self.posYJ-1 >= 0):
                auxX = self.posXJ+2
                auxY = self.posYJ-1
                self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
            else:
                return 0
        else:
            if (self.posXM+2 < 8 and self.posYM-1 < 8 and self.posXM+2 >= 0 and self.posYM-1 >= 0):
                auxX = self.posXM+2
                auxY = self.posYM-1
                self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
            else:
                return 0

    def izquierdaArriba(self, aux):
        if (aux == 1):
            if (self.posXJ-1 < 8 and self.posYJ-2 < 8 and self.posXJ-1 >= 0 and self.posYJ-2 >= 0):
                auxX = self.posXJ-1
                auxY = self.posYJ-2
                self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
            else:
                return 0
        else:
            if (self.posXM-1 < 8 and self.posYM-2 < 8 and self.posXM-1 >= 0 and self.posYM-2 >= 0):
                auxX = self.posXM-1
                auxY = self.posYM-2
                self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
            else:
                return 0

    def izquierdaAbajo(self, aux):
        if (aux == 1):
            if (self.posXJ+1 < 8 and self.posYJ-2 < 8 and self.posXJ+1 >= 0 and self.posYJ-2 >= 0):               
                auxX = self.posXJ+1
                auxY = self.posYJ-2
                self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
            else:
                return 0
        else:
            if (self.posXM+1 < 8 and self.posYM-2 < 8 and self.posXM+1 >= 0 and self.posYM-2 >= 0):
                auxX = self.posXM+1
                auxY = self.posYM-2
                self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
            else:
                return 0

    def validar_movimiento(self, x, y, antX, antY):
        copyBoard = copy.deepcopy(self.board)
        if (copyBoard[x][y] == "--"):
            if -self.player == 1:
                copyBoard[x][y] = "jH"
                copyBoard[antX][antY] = "--"

                nuevoNodo = Node(-self.player, self.depth - 1, copyBoard, x, y,
                                     self.puntosJH, self.posXM, self.posYM, self.puntosJM, self.remaininGrass, self.remainingFlowers, self.remainingApples, self.value, False)
                self.children.append(nuevoNodo)
            
            else:
                copyBoard[x][y] = "jM"
                copyBoard[antX][antY] = "--"
                nuevoNodo = Node(-self.player, self.depth - 1, copyBoard, self.posXJ, self.posYJ,
                                     self.puntosJH, x, y, self.puntosJM, self.remaininGrass, self.remainingFlowers, self.remainingApples, self.value, False)
                self.children.append(nuevoNodo)


        elif (copyBoard[x][y] == "p"):
            if -self.player == 1:
                copyBoard[x][y] = "jH"
                copyBoard[antX][antY] = "--"
                nuevoNodo = Node(-self.player, self.depth - 1, copyBoard, x, y,
                                     self.puntosJH + 1, self.posXM, self.posYM, self.puntosJM, self.remaininGrass - 1, self.remainingFlowers, self.remainingApples, self.value, True)
                self.children.append(nuevoNodo)

            else:
                copyBoard[x][y] = "jM"
                copyBoard[antX][antY] = "--"
                nuevoNodo = Node(-self.player, self.depth - 1, copyBoard, self.posXJ, self.posYJ,
                                     self.puntosJH, x, y, self.puntosJM + 1, self.remaininGrass - 1, self.remainingFlowers, self.remainingApples, self.value, True)
                self.children.append(nuevoNodo)

            


        elif (copyBoard[x][y] == "f"):

            if -self.player == 1:
                copyBoard[x][y] = "jH"
                copyBoard[antX][antY] = "--"
                nuevoNodo = Node(-self.player, self.depth - 1, copyBoard, x, y,
                                     self.puntosJH + 3, self.posXM, self.posYM, self.puntosJM, self.remaininGrass, self.remainingFlowers - 1, self.remainingApples, self.value,True)
                self.children.append(nuevoNodo)

            else:
                copyBoard[x][y] = "jM"
                copyBoard[antX][antY] = "--"
                nuevoNodo = Node(-self.player, self.depth - 1, copyBoard, self.posXJ, self.posYJ,
                                     self.puntosJH, x, y, self.puntosJM + 3, self.remaininGrass, self.remainingFlowers - 1, self.remainingApples, self.value, True) 
                self.children.append(nuevoNodo)           
            

        elif (copyBoard[x][y] == "m"):
            if -self.player == 1:
                copyBoard[x][y] = "jH"
                copyBoard[antX][antY] = "--"
                nuevoNodo = Node(-self.player, self.depth - 1, copyBoard, x, y,
                                     self.puntosJH + 5, self.posXM, self.posYM, self.puntosJM, self.remaininGrass, self.remainingFlowers, self.remainingApples - 1, self.value, True)
                self.children.append(nuevoNodo)
            else:
                copyBoard[x][y] = "jM"
                copyBoard[antX][antY] = "--"
                nuevoNodo = Node(-self.player, self.depth - 1, copyBoard, self.posXJ, self.posYJ,
                                     self.puntosJH, x, y, self.puntosJM + 5, self.remaininGrass, self.remainingFlowers, self.remainingApples - 1, self.value, True)
                self.children.append(nuevoNodo)

        else:
            return 0



