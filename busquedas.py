from collections import deque
import copy as cpy
import numpy as np
#Clase que define un nodo en el 8-puzzle.
class Nodo:
    def __init__(self, estado, padre, movimiento, profundidad, piezas_correctas):        
        self.estado = estado                        #Posición atual de las piezas.
        self.padre = padre                          #Nodo desde el que se llega a este nodo.
        self.movimiento = movimiento                #Movimiento para encontrar este nodo desde el padre.
        self.profundidad = profundidad              #Posición del nodo en el árbol de búsqueda.
        self.piezas_correctas = piezas_correctas    #Total de piezas en su lugar para este estado.

    #Mover la pieza que está a la izquierda
    def movIzqBlco(self,t,posBlanco):
        x = cpy.deepcopy(t)
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not col-1 < 0):
                pivote = x[fila][col-1]
                x[fila][col-1] = 0
                x[fila][col] = pivote
                y = []
                y.extend(x[0])
                y.extend(x[1])
                y.extend(x[2])
                return tuple(y)
            else:
                return None
        except:
            pass

        #Mover la pieza que está a la derecha    
    def movDerBlco(self,t,posBlanco):
        x = cpy.deepcopy(t)
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not col+1 > 2):
                pivote = x[fila][col+1]
                x[fila][col+1] = 0
                x[fila][col] = pivote
                y = []
                y.extend(x[0])
                y.extend(x[1])
                y.extend(x[2])
                return tuple(y)
            else:
                return None
        except:
            pass
    
    #Mover la pieza que está arriba
    def movArrBlco(self,t,posBlanco):
        x = cpy.deepcopy(t)
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not fila-1 < 0):
                pivote = x[fila-1][col]
                x[fila-1][col] = 0
                x[fila][col] = pivote
                y = []
                y.extend(x[0])
                y.extend(x[1])
                y.extend(x[2])
                return tuple(y)
            else:
                return None
        except:
            pass

    #Mover la pieza que está abajo
    def movAbjBlco(self,t,posBlanco):
        x = cpy.deepcopy(t)
        fila = int(str(posBlanco[0])[1])
        col = int(str(posBlanco[1])[1])
        try:
            if(not fila+1 > 2):
                pivote = x[fila+1][col]
                x[fila+1][col] = 0
                x[fila][col] = pivote
                y = []
                y.extend(x[0])
                y.extend(x[1])
                y.extend(x[2])
                return tuple(y)
            else:
                return None
        except:
            pass        

    #Método que encuentra y regresa todos los nodos sucesores del nodo actual.
    def encontrar_sucesores(self):
        matriz = np.array(self.estado)
        matriz = [list(matriz[0:3]),list(matriz[3:6]),list(matriz[6:9])]
        matriz = np.array(matriz)
        pos = np.where(matriz == 0)

        sucesores = []
        sucesorN = self.movArrBlco(matriz,pos)
        sucesorS = self.movAbjBlco(matriz,pos)
        sucesorE = self.movIzqBlco(matriz,pos)
        sucesorO = self.movDerBlco(matriz,pos)
        

        sucesores.append(Nodo(sucesorN, self, "arriba", self.profundidad + 1, calcular_heurisitica(sucesorN)))
        sucesores.append(Nodo(sucesorS, self, "abajo", self.profundidad + 1, calcular_heurisitica(sucesorS)))
        sucesores.append(Nodo(sucesorE, self, "derecha", self.profundidad + 1, calcular_heurisitica(sucesorE)))
        sucesores.append(Nodo(sucesorO, self, "izquierda", self.profundidad + 1, calcular_heurisitica(sucesorO)))
        
        sucesores = [nodo for nodo in sucesores if nodo.estado != None]  
        return sucesores

    #Método que encuentra el camino desde el nodo inicial hasta el actual.
    def encontrar_camino(self, inicial):
        camino = []
        nodo_actual = self
        while nodo_actual.profundidad >= 1:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        camino.reverse()
        return camino

    #Método que imprime ordenadamente el estado (piezas) de un nodo.
    def imprimir_nodo(self):
        renglon = 0
        for pieza in self.estado:
            if pieza == 0:
                print(" ", end = " ")
            else:
                print (pieza, end = " ")
            renglon += 1
            if renglon == 3:
                print()
                renglon = 0       

#Función que calcula la cantidad de piezas que están en su lugar para un estado dado.
def calcular_heurisitica(estado):
    correcto = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    valor_correcto = 0
    piezas_correctas = 0
    if estado:
        for valor_pieza, valor_correcto in zip(estado, correcto):
            if valor_pieza == valor_correcto:
                piezas_correctas += 1
            valor_correcto += 1
    return piezas_correctas   

#Algoritmo Breadth First Search.
def bfs(inicial, meta):
    visitados = set()   #Conjunto de estados visitados para no visitar el mismo estado más de una vez.
    frontera = deque()  #Cola de nodos aún por explorar. Se agrega el nodo inicial.  
    frontera.append(Nodo(inicial, None, None, 0, calcular_heurisitica(inicial)))
    contnodos = 0
    while frontera:                         #Mientras haya nodos por explorar:
        nodo = frontera.popleft()           #Se toma el primer nodo de la cola.

        if nodo.estado not in visitados:    #Si no se había visitado, 
            visitados.add(nodo.estado)      #se agrega al conjunto de visitados.
            contnodos = contnodos +1
        else:                               #Si ya se había visitado
            continue                        #se ignora.
            contnodos = contnodos +1
        
        if nodo.estado == meta:                         #Si es una meta, 
            print("\n¡Se encontró el estado meta final")
            print("********************************************************")
            print("\n¡La cantidad de nodos totales fue:",contnodos-1)     
            print("********************************************************")     
            return nodo.encontrar_camino(inicial)       #se regresa el camino para llegar a él y termina el algoritmo.        
        else:                                           #Si no es una meta, 
            frontera.extend(nodo.encontrar_sucesores()) #se agregan sus sucesores a los nodos por explorar.

#Algoritmo Depth First Search.
def dfs(inicial, meta, profundidad_max):
    visitados = set()   #Conjunto de estados visitados para no visitar el mismo estado más de una vez.
    frontera = deque()  #Pila de nodos aún por explorar. Se agrega el nodo inicial.
    frontera.append(Nodo(inicial, None, None, 0, calcular_heurisitica(inicial)))
    contnodos = 0
    while frontera:                         #Mientras haya nodos por explorar:
        nodo = frontera.pop()               #Se toma el primer nodo de la pila.
        
        if nodo.estado not in visitados:    #Si no se había visitado, 
            visitados.add(nodo.estado)      #se agrega al conjunto de visitados.
            contnodos = contnodos +1
        else:                               #Si ya se visitó,
            continue                        #se ignora.
            contnodos = contnodos +1
        
        if nodo.estado == meta:             #Si es una meta, se regresa el camino para llegar a él y termina el algoritmo.
            print("\n¡Se encontró el estado meta final")
            print("********************************************************")
            print("\n¡La cantidad de nodos totales fue:",contnodos-1)     
            print("********************************************************")    
            return nodo.encontrar_camino(inicial)
        else:                               #Si no es una meta:             
            if profundidad_max > 0:                             #Si se estableció una búsqueda con profundidad limitada
                if nodo.profundidad < profundidad_max:          #y no se ha llegado al límite,                 
                    frontera.extend(nodo.encontrar_sucesores()) #se agregan los sucesores a los nodos por explorar.
            else:                                               #Si no se estableció una búsqueda con profundidad limitada,
                frontera.extend(nodo.encontrar_sucesores())     #se agregan los sucesores a los nodos por explorar.

#Algoritmo Hill Climbing.
def hc(inicial):
    visitados = set()  #Conjunto de estados visitados para no visitar el mismo estado más de una vez.
    nodo_actual = Nodo(inicial, None, None, 0, calcular_heurisitica(inicial))
    contnodos = 0
    while nodo_actual.piezas_correctas < 9:             #Mientras el estado actual no tenga todas las piezas en su lugar:
        sucesores = nodo_actual.encontrar_sucesores()   #Se buscan los sucesores del estado actual
        max_piezas_correctas = -1

        #Para cada nodo en los sucesores, se busca el que tenga más piezas en su lugar.
        
        for nodo in sucesores:   
            contnodos = contnodos +1
            if nodo.piezas_correctas >= max_piezas_correctas and nodo not in visitados:
                max_piezas_correctas = nodo.piezas_correctas
                nodo_siguiente = nodo

            visitados.add(nodo_actual)

        #Si el nodo encontrado tiene más piezas en su lugar que el nodo actual, 
        #se asigna como nodo actual para repetir la búsqueda sobre éste.
        if nodo_siguiente.piezas_correctas >= nodo_actual.piezas_correctas:
            nodo_actual = nodo_siguiente
        #Si no, significa que se llegó a un máximo local y el algoritmo no debe seguir.
        else:
            print("*********************************")
            print("\nNo se encontró el estado final.")
            print("*********************************")
            break
    else:
        print("********************************************************")
        print("\n¡La cantidad de nodos totales fue:",contnodos-1)     
        print("********************************************************")
    return nodo_actual.encontrar_camino(inicial)

#Función main.
def main():
    estado_final = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    estado_inicial = (1, 2, 3, 4, 5, 6, 0, 7,8)


    #Menú principal
    print("Programa para dar solución al puzzle 8")
    print("Estado inicial por defecto: ")
    (Nodo(estado_inicial, None, None, 0, calcular_heurisitica(estado_inicial))).imprimir_nodo()
    print("Estado final por defecto: ")
    (Nodo(estado_final, None, None, 0, calcular_heurisitica(estado_inicial))).imprimir_nodo()
    print("¿Desea crear un nuevo estado inicial?")
    estadoInic = input("Ingrese 1 para crear nuevos estados, 2 para utilizar estados predefinidos \n")

    if estadoInic == '2':

        print("\nDigite el número para elegir el tipo de búsqueda a compilar: ")
        print("1. Búsqueda de Primero en Amplitud (BPA)")
        print("2. Búsqueda de Primero en Profundidad (BPP)")
        print("3. Búsqueda de Ascenso de Colina")
        print("4. Salir")
        algoritmo = input("Digite una opción: ")
        if algoritmo == "1":
            print("Corriendo busqueda de primero en amplitud. Por favor espere.")
            nodos_camino = bfs(estado_inicial, estado_final)

        elif algoritmo == "2":
            print("\n¿Establecer un límite de profundidad?")
            print("Escriba el límite como un entero mayor que 0")
            print("o cualquier otro entero para continuar sin límite.")
            profundidad_max = int(input("Profundidad: "))
            print("Corriendo busqueda de primero en profundidad. Por favor espere.")
            nodos_camino = dfs(estado_inicial, estado_final, profundidad_max)

        elif algoritmo == "3":
            print("\nCorriendo Hill Climbing. Por favor espere...")
            nodos_camino = hc(estado_inicial)
        
        else:
            return 0

    #Se imprime el camino si existe y si el usuario lo desea.
        if nodos_camino:
            print ("El camino tiene", len(nodos_camino), "movimientos.")
            print("\nEstado inicial:")
            (Nodo(estado_inicial, None, None, 0, calcular_heurisitica(estado_inicial))).imprimir_nodo()
            print ("numeros ubicados correctamente:", calcular_heurisitica(estado_inicial), "\n")
            listaMov = []   
            for nodo in nodos_camino:
                print("\nSiguiente movimiento:", nodo.movimiento)
                listaMov.append(nodo.movimiento)
                print("Estado actual:")
                nodo.imprimir_nodo()
                print("numeros ubicados correctamente:", nodo.piezas_correctas, "\n")   
            print("Todos los movimientos para llegar a solución",listaMov)
            print("Para consultar el total de nodos efectuados en la ejecución, navegue hasta el inicio de los recorridos")
        else:
            print ("\nNo se encontró un camino con las condiciones dadas.")

        return 0   

    elif estadoInic == '1':
        listaI = []
        contador = 9
        for x in range(9):
            print("Faltan",contador-x,"números")
            valor=int(input("Ingrese un valor entero: entre 0 y 8 sin repetir: \n"))
            listaI.append(valor)
            
        nuevoEstado = tuple(listaI)
        estado_inicial = nuevoEstado
        print("Estado inicial nuevo: ")
        (Nodo(estado_inicial, None, None, 0, calcular_heurisitica(estado_inicial))).imprimir_nodo()
        listaF = []
        print("Ingreso de estado final")
        for x in range(9):
            valor=int(input("Ingrese un valor entero: entre 0 y 8 sin repetir: \n"))
            print("Faltan",contador-x,"números")
            listaF.append(valor)
        nuevoEstadoF = tuple(listaF)
        estado_final = nuevoEstadoF
        print("-------------------------------------")
        print("Estado inicial nuevo: ")
        (Nodo(estado_inicial, None, None, 0, calcular_heurisitica(estado_inicial))).imprimir_nodo()
        print("Estado Final nuevo: ")
        (Nodo(estado_final, None, None, 0, calcular_heurisitica(estado_inicial))).imprimir_nodo()
        print("-------------------------------------")
        print("\nDigite el número para elegir el tipo de búsqueda a compilar: ")
        print("1. Búsqueda de Primero en Amplitud (BPA)")
        print("2. Búsqueda de Primero en Profundidad (BPP)")
        print("3. Búsqueda de Ascenso de Colina")
        print("4. Salir")
        algoritmo = input("Digite una opción: ")
        if algoritmo == "1":
            print("Corriendo busqueda de primero en amplitud. Por favor espere.")
            nodos_camino = bfs(estado_inicial, estado_final)

        elif algoritmo == "2":
            print("\n¿Establecer un límite de profundidad?")
            print("Escriba el límite como un entero mayor que 0")
            print("o cualquier otro entero para continuar sin límite.")
            profundidad_max = int(input("Profundidad: "))
            print("Corriendo busqueda de primero en profundidad. Por favor espere.")
            nodos_camino = dfs(estado_inicial, estado_final, profundidad_max)

        elif algoritmo == "3":
            print("\nCorriendo Hill Climbing. Por favor espere...")
            nodos_camino = hc(estado_inicial)
        
        else:
            return 0

    #Se imprime el camino si existe y si el usuario lo desea.
    if nodos_camino:
        print ("El camino tiene", len(nodos_camino), "movimientos.")
        print("\nEstado inicial:")
        (Nodo(estado_inicial, None, None, 0, calcular_heurisitica(estado_inicial))).imprimir_nodo()
        print ("numeros ubicados correctamente:", calcular_heurisitica(estado_inicial), "\n")
        listaMov = []   
        for nodo in nodos_camino:
            print("\nSiguiente movimiento:", nodo.movimiento)
            listaMov.append(nodo.movimiento)
            print("Estado actual:")
            nodo.imprimir_nodo()
            print("numeros ubicados correctamente:", nodo.piezas_correctas, "\n")   
        print("Todos los movimientos para llegar a solución",listaMov)
        print("Para consultar el total de nodos efectuados en la ejecución, navegue hasta el inicio de los recorridos")
    else:
        print ("\nNo se encontró un camino con las condiciones dadas.")

    return 0   
 

if __name__ == "__main__":
    main()