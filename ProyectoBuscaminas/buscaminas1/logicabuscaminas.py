import random

class Coordenada:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

class Casilla:
    def __init__(self, coordenada):
        self.coordenada = coordenada
        self.contiene_mina = False
        self.minas_adyacentes = 0

class Tablero:
    def __init__(self, filas, columnas, minas):
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.casillas = [[Casilla(Coordenada(fila, columna)) for columna in range(columnas)] for fila in range(filas)]
        self.colocar_minas()

    def colocar_minas(self):
        minas_colocadas = 0
        while minas_colocadas < self.minas:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if not self.casillas[fila][columna].contiene_mina:
                self.casillas[fila][columna].contiene_mina = True
                minas_colocadas += 1

    def contar_minas_adyacentes(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        nueva_fila = fila + i
                        nueva_columna = columna + j

                        if 0 <= nueva_fila < self.filas and 0 <= nueva_columna < self.columnas:
                            if self.casillas[nueva_fila][nueva_columna].contiene_mina:
                                self.casillas[fila][columna].minas_adyacentes += 1
