"""
Participantes: 
- Manuel Velazco 29.830.787
- Nicola Amoruso 31.747.565
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar(self, valor, posicion=None):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        elif posicion is None or posicion <= 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for i in range(posicion - 1):
                if actual.siguiente:
                    actual = actual.siguiente
                else:
                    break
            nuevo_nodo.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            if nuevo_nodo.siguiente is None:
                self.cola = nuevo_nodo

    def eliminar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def revertir(self):
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza

    def eliminar_duplicados(self):
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            while siguiente:
                if siguiente.valor == actual.valor:
                    if siguiente.anterior:
                        siguiente.anterior.siguiente = siguiente.siguiente
                    if siguiente.siguiente:
                        siguiente.siguiente.anterior = siguiente.anterior
                    if siguiente == self.cola:
                        self.cola = siguiente.anterior
                siguiente = siguiente.siguiente
            actual = actual.siguiente

    def buscar(self, valor):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" <-> ")
            actual = actual.siguiente
        print("None")

lista = ListaDoblementeEnlazada()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(2)
lista.insertar(4)
lista.insertar(4)
lista.imprimir()  

lista.eliminar(3)
lista.imprimir()  

lista.revertir()
lista.imprimir()  

lista.eliminar_duplicados()
lista.imprimir()  

print(lista.buscar(1))  