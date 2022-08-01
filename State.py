from random import randint
class GameState():
    def __init__(self):
        self.xJugador = 0
        self.yJugador = 0

        self.xMaquina = 0
        self.yMaquina = 0

        self.posX = 0
        self.posY = 0

        self.piezas = [
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]

        for i in range (14):
            GameState.posElementoP(self)
        
        for i in range (5):
            GameState.posElementoF(self)
        
        for i in range (2):
            GameState.posElementoM(self)

        GameState.posJugadorH(self)
        GameState.posJugadorM(self)

    def posElementoP(self):
        #Asignar posiciones a pasto

        posX = randint(0,7)
        posY = randint(0,7)

        if (self.piezas[posX][posY] == "--"):
            self.piezas[posX][posY] = "p"
        else:
            self.posElementoP()
    
    def posElementoF(self):
        #Asignar posiciones a flores

        posX = randint(0,7)
        posY = randint(0,7)

        if (self.piezas[posX][posY] == "--"):
            self.piezas[posX][posY] = "f"
        else:
            self.posElementoF()
    
    def posElementoM(self):
        #Asignar posiciones a Manzanas

        posX = randint(0,7)
        posY = randint(0,7)

        if (self.piezas[posX][posY] == "--"):
            self.piezas[posX][posY] = "m"
        else:
            self.posElementoM()


    def posJugadorH(self):
        self.xJugador = randint(0,7)
        self.yJugador = randint(0,7)

        if (self.piezas[self.xJugador][self.yJugador] == "--"):
            self.piezas[self.xJugador][self.yJugador] = "jH"
        else: 
            self.posJugadorH()
    
    def posJugadorM(self):
        self.xMaquina = randint(0,7)
        self.yMaquina = randint(0,7)

        if (self.piezas[self.xMaquina][self.yMaquina] == "--"):
            self.piezas[self.xMaquina][self.yMaquina] = "jM"
        else: 
            self.posJugadorM()
        