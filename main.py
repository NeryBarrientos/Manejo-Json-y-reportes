import json
import numpy as np
listacargada = []
ruta = []
opcion = []
maximo = listacargada
max_edad = []
max_promedio = []
n = "Nombre : "
e = "Edad : "
a = "Activo : "
p = "Promedio : "
atributos = []
def cargar_datos(ruta):
    #print(ruta)
    for i in ruta:
        with open(i + ".json") as archivos:
            datos = json.loads(archivos.read())
            listacargada.append(datos)
            print("Archivo: " + i + " cargado")
    contador = 0
    for i in listacargada:
        for j in range(len(i)):
            max_edad.append(listacargada[contador][j]['edad'])
            max_promedio.append(listacargada[contador][j]['promedio'])
        contador += 1

def main():
    print("estas en el menu")
    opcion = input().split(",")
    ruta = opcion
    atributos = opcion
    comando = opcion[0][:6]
    comando1 = opcion[0][:11]
    comando2 = opcion[0][:4]
    opcionsuma = opcion[0][5:]
    todos = opcion[0][12:13]
    ruta[0] = ruta[0].replace(" ","")
    ruta[0] = ruta[0][6:]
    if (comando.lower() == 'cargar'):
        for i in range(len(ruta)):
            ruta[i] = ruta[i].replace(" ", "")
        cargar_datos(ruta)
        print(listacargada)
        main()
    elif (comando1.lower() == 'seleccionar'):
        #print("Que atributos desea buscar")
        #atributos = input().split(',')
        #print(atributos)
        if (todos == '*'):    
            imprimir_todos()
            main()
        else:
            main()
    elif (comando.lower() == 'maximo'):
        for i in range(len(atributos)):
            atributos[i] = atributos[i].replace(" ", "")
            #print(atributos)
            if atributos[0] == 'edad':
                edadmaxima = np.array(max_edad)
                print("La edad maxima es : " + str(np.amax(edadmaxima)))
            elif atributos[0] == 'promedio':
                promediomaximo = np.array(max_promedio)
                print("El promedio maximo es : " + str(np.amax(promediomaximo)))
        main()
    elif (comando.lower() == 'minimo'):
        for i in range(len(atributos)):
            atributos[i] = atributos[i].replace(" ", "")
            #print(atributos)
            if atributos[0] == 'edad':
                edadminima = np.array(max_edad)
                print("La edad minima es : " + str(np.amin(edadminima)))
            elif atributos[0] == 'promedio':
                promediominimo = np.array(max_promedio)
                print("El promedio minimo es : " + str(np.amin(promediominimo)))
        main()
    elif (comando2.lower() == 'suma'):
        print(opcionsuma)
        if opcionsuma == 'edad':
            sumaedad(max_edad)
        elif opcionsuma == 'promedio':
            sumaprom(max_promedio)
        main()
    elif (comando.lower() == 'cuenta'):
        print("opcion 6")
    elif (comando.lower() == 'reportar'):
        print("opcion 7")
    else:
        exit()
        print()

def opcion_cargar(opt):
    if (opt == 'cargar'):
        print("Escriba el nombre del archivo a cargar")
        print()
        ruta = input().split(',')
        listacargada.append(cargar_datos(ruta))
        print(listacargada)

def imprimir_todos():
    print(listacargada)
    contador = 0
    for i in listacargada:
        for j in range(len(i)):
            print("--------------------------")
            print('{}{}'.format(n,listacargada[contador][j]['nombre']))
            print('{}{}'.format(e,listacargada[contador][j]['edad']))
            print('{}{}'.format(a,listacargada[contador][j]['activo']))
            print('{}{}'.format(p,listacargada[contador][j]['promedio']))
            print("--------------------------")
        contador += 1

def sumaedad(listaNumeros):
    misuma = 0
    for i in listaNumeros:
        misuma = misuma + i
    print ("La suma de las edades es : " + str(misuma))

def sumaprom(listapro):
    suma = 0
    for i in listapro:
        suma = suma + i
    print ("La suma de los promedios es : " + str(suma))
main()