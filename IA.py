import random
from math import inf
from GUI import *

def evaluar(self, jugador):
    if jugador == "jM":
        return self.puntosJM - self.puntosJH
    else: 
        return self.puntosJH - self.puntosJM
    
def minimax():
    pass

