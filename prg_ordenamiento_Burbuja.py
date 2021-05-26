
# Ordenamiento burbuja

# Definicion del vector
#listaEnteros=[3,45,21,2,34,22,11,33,12,56]

listaEnteros=[]

def cargarDatos (listaEnteros):   
    print("Cargar Datos")
    for i in range (1,10):
        dato=int(input("Ingrese valor: "))
        listaEnteros.append(dato)
    print(listaEnteros)

# Funcion que realiza el ordenamiento burbuja
def ordBurbuja (listaDesordenada):
    print("Ordenar Datos")
    for i in range (1,len(listaDesordenada)-1):
        for j in range (0,len(listaDesordenada)-1):
            if listaDesordenada[j] > listaDesordenada[j+1]:
                aux=listaDesordenada[j]
                listaDesordenada[j]=listaDesordenada[j+1]
                listaDesordenada[j+1]=aux   
    print(listaEnteros)
#Fin del ordenamiento

#Llamar l funcion que carga los datos
cargarDatos(listaEnteros)

# Llamar la funcion ordenar burbuja
ordBurbuja(listaEnteros)
