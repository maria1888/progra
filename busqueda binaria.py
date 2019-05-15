def binaria(lista,elemento):
    if isinstance (lista,list):
        return busqueda(lista,elemento,0,len(lista)-1)
    else: return "error"

def busqueda(lista, elemento, indice1, indice2):
    if indice2 < indice1:
        return False
    mitad = (indice1+indice2)//2
    if lista[mitad]== elemento:
        return True
    elif lista[mitad] < elemento:
        return busqueda(lista,elemento,mitad+1,indice2)
    else: return busqueda(lista,elemento,indice1,mitad-1)
