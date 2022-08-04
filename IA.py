import random
from math import inf

from sys import maxsize
import gc

import copy

class Node(object):
    # player es un entero 1 para humano -1 para maquina
    def __init__(self, player, depth, board, posXJ, posYJ, puntosJH, posXM, posYM, puntosJM, remainingGrass, remainingFlowers, remainingApples, value):
        self.player = player
        self.depth = depth

        self.board = board
        self.posXJ = posXJ
        self.posYJ = posYJ
        self.puntosJH = puntosJH

        self.posXM = posXM
        self.posYM = posYM
        self.puntosJM = puntosJM

        self.remaininGrass = remainingGrass
        self.remainingFlowers = remainingFlowers
        self.remainingApples = remainingApples

        self.value = value
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

    def evaluar(self):
        if (self.player == 1):
            return self.puntosJH - self.puntosJM
        else:
            return self.puntosJM - self.puntosJH
        

    def createChildren(self):
        possibleMoves = [1, 2, 3, 4, 5, 6, 7, 8] #[1, 2, 3, 4, 5, 6, 7, 8]
        if self.depth >= 0:
            for i in possibleMoves:
                if (i == 1):
                    nuevoNodo = Node(-self.player, self.depth - 1, copy.deepcopy(self.board), self.posXJ, self.posYJ,
                                     self.puntosJH, self.posXM, self.posYM, self.puntosJM, self.remaininGrass, self.remainingFlowers, self.remainingApples, self.value)
                    #m es una variable que identifica con 0 si el nodo no se movio
                    m = nuevoNodo.arribaDerecha()

                    if m != 0:
                        self.children.append(nuevoNodo)

                    del nuevoNodo
                    gc.collect()
                elif (i == 2):
                    nuevoNodo = Node(-self.player, self.depth - 1, copy.deepcopy(self.board), self.posXJ, self.posYJ,
                                     self.puntosJH, self.posXM, self.posYM, self.puntosJM, self.remaininGrass, self.remainingFlowers, self.remainingApples,
                                     self.value)

                    m = nuevoNodo.arribaIzquierda()
                    if m != 0:
                        self.children.append(nuevoNodo)

                    del nuevoNodo
                    gc.collect()
                elif (i == 3):
                    nuevoNodo = Node(-self.player, self.depth - 1, copy.deepcopy(self.board), self.posXJ, self.posYJ,
                                     self.puntosJH, self.posXM, self.posYM, self.puntosJM, self.remaininGrass, self.remainingFlowers, self.remainingApples,
                                     self.value)

                    m = nuevoNodo.derechaArriba()
                    if m != 0:
                        self.children.append(nuevoNodo)

                    del nuevoNodo
                    gc.collect()
                elif (i == 4):
                    nuevoNodo = Node(-self.player, self.depth - 1, copy.deepcopy(self.board), self.posXJ, self.posYJ,
                                     self.puntosJH, self.posXM, self.posYM, self.puntosJM, self.remaininGrass, self.remainingFlowers, self.remainingApples,
                                     self.value)

                    m = nuevoNodo.derechaAbajo()
                    if m != 0:
                        self.children.append(nuevoNodo)

                    del nuevoNodo
                    gc.collect()
                elif (i == 5):
                    nuevoNodo = Node(-self.player, self.depth - 1, copy.deepcopy(self.board), self.posXJ, self.posYJ,
                                     self.puntosJH, self.posXM, self.posYM, self.puntosJM, self.remaininGrass, self.remainingFlowers, self.remainingApples,
                                     self.value)

                    m = nuevoNodo.abajoDerecha()
                    if m != 0:
                        self.children.append(nuevoNodo)

                    del nuevoNodo
                    gc.collect()
                elif (i == 6):
                    nuevoNodo = Node(-self.player, self.depth - 1, copy.deepcopy(self.board), self.posXJ, self.posYJ,
                                     self.puntosJH, self.posXM, self.posYM, self.puntosJM, self.remaininGrass, self.remainingFlowers, self.remainingApples,
                                     self.value)

                    m = nuevoNodo.abajoIzquierda()
                    if m != 0:
                        self.children.append(nuevoNodo)

                    del nuevoNodo
                    gc.collect()
                elif (i == 7):
                    nuevoNodo = Node(-self.player, self.depth - 1, copy.deepcopy(self.board), self.posXJ, self.posYJ,
                                     self.puntosJH, self.posXM, self.posYM, self.puntosJM, self.remaininGrass, self.remainingFlowers, self.remainingApples,
                                     self.value)

                    m = nuevoNodo.izquierdaArriba()
                    if m != 0:
                        self.children.append(nuevoNodo)

                    del nuevoNodo
                    gc.collect()
                elif (i == 8):
                    nuevoNodo = Node(-self.player, self.depth - 1, copy.deepcopy(self.board), self.posXJ, self.posYJ,
                                     self.puntosJH, self.posXM, self.posYM, self.puntosJM, self.remaininGrass, self.remainingFlowers, self.remainingApples,
                                     self.value)

                    m = nuevoNodo.izquierdaAbajo()
                    if m != 0:
                        self.children.append(nuevoNodo)

                    del nuevoNodo
                    gc.collect()
                
                print("fila ", self.posXM, "columna ", self.posYM)

    def arribaDerecha(self):
        if (self.player == 1):
            if (self.posXJ-2 < 8 and self.posYJ+1 < 8 and self.posXJ-2 >= 0 and self.posYJ+1 >= 0):
                auxX = self.posXJ-2
                auxY = self.posYJ+1
                m = self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0
        else:
            if (self.posXM-2 < 8 and self.posYM+1 < 8 and self.posXM-2 >= 0 and self.posYM+1 >= 0):
                auxX = self.posXM-2
                auxY = self.posYM+1
                m = self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0

    def arribaIzquierda(self):
        if (self.player == 1):
            if (self.posXJ-2 < 8 and self.posYJ-1 < 8 and self.posXJ-2 >= 0 and self.posYJ-1 >= 0):
                auxX = self.posXJ-2
                auxY = self.posYJ-1
                m = self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0
        else:
            if (self.posXM-2 < 8 and self.posYM-1 < 8 and self.posXM-2 >= 0 and self.posYM-1 >= 0):
                auxX = self.posXM-2
                auxY = self.posYM-1
                m = self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0

    def derechaArriba(self):
        if (self.player == 1):
            if (self.posXJ+1 < 8 and self.posYJ+2 < 8 and self.posXJ+1 >= 0 and self.posYJ+2 >= 0):
                auxX = self.posXJ+1
                auxY = self.posYJ+2
                m = self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0
        else:
            if (self.posXM+1 < 8 and self.posYM+2 < 8 and self.posXM+1 >= 0 and self.posYM+2 >= 0):
                auxX = self.posXM+1
                auxY = self.posYM+2
                m = self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0

    def derechaAbajo(self):
        if (self.player == 1):
            if (self.posXJ-1 < 8 and self.posYJ+2 < 8 and self.posXJ-1 >= 0 and self.posYJ+2 >= 0):
                auxX = self.posXJ-1
                auxY = self.posYJ+2
                m = self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0
        else:
            if (self.posXM-1 < 8 and self.posYM+2 < 8 and self.posXM-1 >= 0 and self.posYM+2 >= 0):
                auxX = self.posXM-1
                auxY = self.posYM+2
                m = self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0

    def abajoDerecha(self):
        if (self.player == 1):
            if (self.posXJ+2 < 8 and self.posYJ+1 < 8 and self.posXJ+2 >= 0 and self.posYJ+1 >= 0):
                auxX = self.posXJ+2
                auxY = self.posYJ+1
                m = self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0
        else:
            if (self.posXM+2 < 8 and self.posYM+1 < 8 and self.posXM+2 >= 0 and self.posYM+1 >= 0):
                auxX = self.posXM+2
                auxY = self.posYM+1
                m = self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0

    def abajoIzquierda(self):
        if (self.player == 1):
            if (self.posXJ+2 < 8 and self.posYJ-1 < 8 and self.posXJ+2 >= 0 and self.posYJ-1 >= 0):
                auxX = self.posXJ+2
                auxY = self.posYJ-1
                m = self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0
        else:
            if (self.posXM+2 < 8 and self.posYM-1 < 8 and self.posXM+2 >= 0 and self.posYM-1 >= 0):
                auxX = self.posXM+2
                auxY = self.posYM-1
                m = self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0

    def izquierdaArriba(self):
        if (self.player == 1):
            if (self.posXJ-1 < 8 and self.posYJ-2 < 8 and self.posXJ-1 >= 0 and self.posYJ-2 >= 0):
                auxX = self.posXJ-1
                auxY = self.posYJ-2
                m = self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0
        else:
            if (self.posXM-1 < 8 and self.posYM-2 < 8 and self.posXM-1 >= 0 and self.posYM-2 >= 0):
                auxX = self.posXM-1
                auxY = self.posYM-2
                m = self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0

    def izquierdaAbajo(self):
        if (self.player == 1):
            if (self.posXJ+1 < 8 and self.posYJ-2 < 8 and self.posXJ+1 >= 0 and self.posYJ-2 >= 0):
                auxX = self.posXJ+1
                auxY = self.posYJ-2
                m = self.validar_movimiento(auxX, auxY, self.posXJ, self.posYJ)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0
        else:
            if (self.posXM+1 < 8 and self.posYM-2 < 8 and self.posXM+1 >= 0 and self.posYM-2 >= 0):
                auxX = self.posXM+1
                auxY = self.posYM-2
                m = self.validar_movimiento(auxX, auxY, self.posXM, self.posYM)
                print(auxX, " / ", auxY)
                return m
            else:
                return 0

    def validar_movimiento(self, x, y, xAnt, yAnt):
        if (self.board[x][y] == "--"):
            if self.player == 1:
                self.board[x][y] = "jH"
                self.posXJ = x
                self.posYJ = y
            else:
                self.board[x][y] = "jM"
                self.posXM = x
                self.posYM = y
            self.player = -self.player
            self.board[xAnt][yAnt] = "--"
            self.value = self.evaluar()

        elif (self.board[x][y] == "p"):
            if self.player == 1:
                self.board[x][y] = "jH"
                self.posXJ = x
                self.posYJ = y
                self.remaininGrass -= 1
                self.puntosJH = self.puntosJH + 1
            else:
                self.board[x][y] = "jM"
                self.posXM = x
                self.posYM = y
                self.remaininGrass -= 1
                self.puntosJM = self.puntosJM + 1
                print("pasto ", self.puntosJM)

            self.player = -self.player
            self.board[xAnt][yAnt] = "--"
            self.value = self.evaluar()

        elif (self.board[x][y] == "f"):

            if self.player == 1:
                self.board[x][y] = "jH"
                self.posXJ = x
                self.posYJ = y
                self.remainingFlowers -= 1
                self.puntosJH = self.puntosJH + 3
            else:
                self.board[x][y] = "jM"
                self.posXM = x
                self.posYM = y
                self.remainingFlowers -= 1
                self.puntosJM = self.puntosJM + 3
            self.player = -self.player
            self.board[xAnt][yAnt] = "--"
            self.value = self.evaluar()

        elif (self.board[x][y] == "m"):
            if self.player == 1:
                self.board[x][y] = "jH"
                self.posXJ = x
                self.posYJ = y
                self.remainingApples -= 1
                self.puntosJH = self.puntosJH + 5
            else:
                self.board[x][y] = "jM"
                self.posXM = x
                self.posYM = y
                self.remainingApples -= 1
                self.puntosJM = self.puntosJM + 5
            self.player = -self.player
            self.board[xAnt][yAnt] = "--"
            self.value = self.evaluar()
        else:
            return 0



