import json

def cargar_datos(ruta):
    with open(ruta) as archivos:
        datos = json.loads(archivos.read())
    for element in datos:
        print(element)

#print("Escriba el nombre del archivo a cargar")
#ruta = input()
#cargar_datos(ruta)

while True:
    print('Escoja una opcion: \n 1.CARGAR \n 2.SELECCIONAR \n 3.MAXIMO \n 4.MINIMO \n 5.SUMA \n 6.CUENTA \n 7.REPORTAR \n 8.SALIR')
    opt = input()
    if opt == '1':
        print("Escriba el nombre del archivo a cargar")
        ruta = input()
        cargar_datos(ruta)
    elif opt == '2':
        print("opcion 2")
    elif opt == '3':
        print("opcion 3")
    elif opt == '4':
        print("opcion 4")
    elif opt == '5':
        print("opcion 5")
    elif opt == '6':
        print("opcion 6")
    elif opt == '7':
        print("opcion 7")
    else:
        exit()
