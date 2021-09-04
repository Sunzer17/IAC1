import numpy as np

estadoInicial = [[3,2,8],
                 [6,5,1],
                 [4,7,'□']]

class Estado:
    def __init__(self,estadoActual,isRaiz,estadoPadre,reglaUsada):
        self.matriz = estadoActual
        self.isRaiz = isRaiz
        self.padre = estadoPadre
        self.reglaUtilizada = reglaUsada

class Regla:
    def __init__(self,num,dir):
        self.numero = num
        self.direccion = dir

class Procesamiento:
    def __init__(self):
        pass

    def movIzqBlco(self,estadoActual,posBlanco):
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not col-1 < 0):
                pivote = estadoActual[fila][col-1]
                estadoActual[fila][col-1] = '□'
                estadoActual[fila][col] = pivote
        except:
            pass
        print(np.array(estadoActual))

    def movDerBlco(self,estadoActual,posBlanco):
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not col+1 > 2):
                pivote = estadoActual[fila][col+1]
                estadoActual[fila][col+1] = '□'
                estadoActual[fila][col] = pivote
        except:
            pass
        print(np.array(estadoActual))
    
    def movArrBlco(self,estadoActual,posBlanco):
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not fila-1 < 0):
                pivote = estadoActual[fila-1][col]
                estadoActual[fila-1][col] = '□'
                estadoActual[fila][col] = pivote
        except:
            pass
        print(np.array(estadoActual))

    def movAbjBlco(self,estadoActual,posBlanco):
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not fila+1 > 2):
                pivote = estadoActual[fila+1][col]
                estadoActual[fila+1][col] = '□'
                estadoActual[fila][col] = pivote
        except:
            pass
        print(np.array(estadoActual))


    def procesarRegla(estadoActual,regla):
        print('procesarRegla')

def main():
    matriz = np.array(estadoInicial)
    pos = np.where(matriz == '□')
    proc = Procesamiento()
    
    
if __name__ == "__main__":
    main()
