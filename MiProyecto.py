import numpy as np
import copy as cpy

estadoInicial = [[1,2,3],
                 [4,5,6],
                 [7,'□',8]]

estadoFinal = [[1,2,3],
               [4,5,6],
               [7,8,'□']]

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

    def movIzqBlco(self,t,posBlanco):
        x = cpy.deepcopy(t)
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not col-1 < 0):
                pivote = x[fila][col-1]
                x[fila][col-1] = '□'
                x[fila][col] = pivote
                return x
            else:
                return None
        except:
            pass

    def movDerBlco(self,t,posBlanco):
        x = cpy.deepcopy(t)
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not col+1 > 2):
                pivote = x[fila][col+1]
                x[fila][col+1] = '□'
                x[fila][col] = pivote
                return x
            else:
                return None
        except:
            pass
    
    def movArrBlco(self,t,posBlanco):
        x = cpy.deepcopy(t)
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not fila-1 < 0):
                pivote = x[fila-1][col]
                x[fila-1][col] = '□'
                x[fila][col] = pivote
                return x
            else:
                return None
        except:
            pass

    def movAbjBlco(self,t,posBlanco):
        x = cpy.deepcopy(t)
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not fila+1 > 2):
                pivote = x[fila+1][col]
                x[fila+1][col] = '□'
                x[fila][col] = pivote
                return x
            else:
                return None
        except:
            pass
                
    def BPA(self,estadoActual,estadosRecorridos):
        print(estadoActual)
        matriz = np.array(estadoActual)
        pos = np.where(matriz == '□')
        if(estadoActual == None): 
                return None
        try:
            estadosRecorridos.index(estadoActual)
            return None
        except:
            estadosRecorridos.append(estadoActual)
            if(estadoActual == estadoFinal):
                return estadoActual
            else:
                self.BPA(self.movDerBlco(estadoActual,pos),estadosRecorridos)
                self.BPA(self.movIzqBlco(estadoActual,pos),estadosRecorridos)
                self.BPA(self.movArrBlco(estadoActual,pos),estadosRecorridos)
                self.BPA(self.movAbjBlco(estadoActual,pos),estadosRecorridos)
            
def main():
    
    proc = Procesamiento()
    proc.BPA(estadoInicial,[])
    
if __name__ == "__main__":
    main()
