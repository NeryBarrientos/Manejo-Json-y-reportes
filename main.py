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
    print('Escoja una opcion: \n CARGAR \n SELECCIONAR \n MAXIMO \n MINIMO \n SUMA \n CUENTA \n REPORTAR \n 8.SALIR')
    opt = input()
    if opt == 'CARGAR':
        print("Escriba el nombre del archivo a cargar")
        print()
        ruta = input()
        ruta = ruta + '.json'
        cargar_datos(ruta)
    elif opt == 'SELECCIONAR':
        print("opcion 2")
    elif opt == 'MAXIMO':
        print("opcion 3")
    elif opt == 'MINIMO':
        print("opcion 4")
    elif opt == 'SUMA':
        print("opcion 5")
    elif opt == 'CUENTA':
        print("opcion 6")
    elif opt == 'REPORTAR':
        print("opcion 7")
    else:
        exit()
        print()
