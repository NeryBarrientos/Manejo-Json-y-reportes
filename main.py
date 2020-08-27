import json
import re
listacargada = []
ruta = []
def cargar_datos(ruta):
    #print(ruta)
    for i in ruta:
        contador = 0
        with open(i + ".json") as archivos:
            datos = json.loads(archivos.read())
            listacargada.append(datos)
            print("Archivo: " + i + " cargado")

def main():
    print("estas en el menu")
    opcion = input().split(" ")
    ruta = opcion[::]
    ruta.pop(0)
    #print(ruta)
    if (opcion[0].lower() == 'cargar'):
        cargar_datos(ruta)
        print(listacargada[0][0]['nombre'])
        #print(listacargada)
        main()
    elif opt == '2':
        print("hola")
        print(listacargada)
    elif opt == 'maximo':
        print("opcion 3")
    elif opt == 'minimo':
        print("opcion 4")
    elif opt == 'suma':
        print("opcion 5")
    elif opt == 'cuenta':
        print("opcion 6")
    elif opt == 'reportar':
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

main()