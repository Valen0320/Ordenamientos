opcionMenu = int(input("\t1. Mostrar lista\n \t2. Ordenamiento Burbuja\n \t3. Ordenamiento Shell\n \t4. Ordenamiento Inserccion\n Ingrese la opcion que desea: "))

lista = []
cant=int(input("Ingrese la cantidad de numeros que desea que tenga la lista: "))
for i in range(1,cant+1):
    num = int(input("Ingresa los numeros: "))
    lista.append(num)

if(opcionMenu == 1):
    print("Cargar lista: ",lista)
    
if(opcionMenu == 2):
    def ordenamientoBurbuja(unaLista):
        for numPasada in range(len(unaLista)-1,0,-1):
            for i in range(numPasada):
                if unaLista[i]>unaLista[i+1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i+1]
                    unaLista[i+1] = temp
    ordenamientoBurbuja(lista)
    print(lista)
         
elif(opcionMenu == 3):
    def ordenamientoDeShell(unaLista):
        contadorSublistas = len(unaLista)//2
        while contadorSublistas > 0:          
            for posicionInicio in range(contadorSublistas):
                brechaOrdenamientoPorInsercion(unaLista,posicionInicio,contadorSublistas)
            print("Después de los incrementos de tamaño",contadorSublistas,
                                       "La lista es",unaLista)
            contadorSublistas = contadorSublistas // 2
    
    def brechaOrdenamientoPorInsercion(unaLista,inicio,brecha):
        for i in range(inicio+brecha,len(unaLista),brecha):
            valorActual = unaLista[i]
            posicion = i
            while posicion>=brecha and unaLista[posicion-brecha]>valorActual:
                unaLista[posicion]=unaLista[posicion-brecha]
                posicion = posicion-brecha
            unaLista[posicion]=valorActual
    ordenamientoDeShell(lista)
    print(lista)
    
elif(opcionMenu == 4):
    def ordenamientoPorInsercion(unaLista):
        for indice in range(1,len(unaLista)):
            valorActual = unaLista[indice]
            posicion = indice
            while posicion>0 and unaLista[posicion-1]>valorActual:
                unaLista[posicion]=unaLista[posicion-1]
                posicion = posicion-1
            unaLista[posicion]=valorActual
    ordenamientoPorInsercion(lista)
    print(lista)
