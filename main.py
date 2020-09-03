import json
import numpy as np
import webbrowser
listacargada = []
ruta = []
opcion = []
maximo = listacargada
max_edad = []
max_promedio = []
num_nombres = []
table_activo = []
titulo = ['Nombre' , 'Edad' , 'Activo' , 'Promedio']
n = "Nombre : "
e = "Edad : "
a = "Activo : "
p = "Promedio : "
atributos = []
def cargar_datos(ruta):
    #print(ruta)
    ruta[0] = ruta[0].replace(" ","")
    ruta[0] = ruta[0][6:]
    for i in ruta:
        with open(i) as archivos:
            datos = json.loads(archivos.read())
            listacargada.append(datos)
            print("Archivo: " + i + " cargado")
    contador = 0
    for i in listacargada:
        for j in range(len(i)):
            max_edad.append(listacargada[contador][j]['edad'])
            max_promedio.append(listacargada[contador][j]['promedio'])
            num_nombres.append(listacargada[contador][j]['nombre'])
            table_activo.append(listacargada[contador][j]['activo'])
        contador += 1

def main():
    print(">>>>>" , end='')
    lectura  = input()
    opcion = lectura.split(",")
    ruta = opcion
    atributos = opcion
    comando = opcion[0][:6]
    comando1 = opcion[0][:11]
    comando2 = opcion[0][:4]
    comando3 = opcion[0][:8]
    opcionsuma = opcion[0][5:]
    todos = opcion[0][12:13]
    if (comando.lower() == 'cargar'):
        for i in range(len(ruta)):
            ruta[i] = ruta[i].replace(" ", "")
        cargar_datos(ruta)
        print("")
        main()
    elif (comando1.lower() == 'seleccionar'):
        if (todos == '*'):    
            imprimir_todos()
            main()
        else:
            main()
    elif (comando.lower() == 'maximo'):
        atributos[0] = atributos[0][6:]
        for i in range(len(atributos)):
            atributos[i] = atributos[i].replace(" ", "")
            if atributos[0][:6] == 'edad':
                edadmaxima = np.array(max_edad)
                print("La edad maxima es : " + str(np.amax(edadmaxima)))
                print("")
            elif atributos[0] == 'promedio':
                promediomaximo = np.array(max_promedio)
                print("El promedio maximo es : " + str(np.amax(promediomaximo)))
                print("")
        main()
    elif (comando.lower() == 'minimo'):
        atributos[0] = atributos[0][6:]
        for i in range(len(atributos)):
            atributos[i] = atributos[i].replace(" ", "")
            if atributos[0][:6] == 'edad':
                edadminima = np.array(max_edad)
                print("La edad minima es : " + str(np.amin(edadminima)))
                print("")
            elif atributos[0] == 'promedio':
                promediominimo = np.array(max_promedio)
                print("El promedio minimo es : " + str(np.amin(promediominimo)))
                print("")
        main()
    elif (comando2.lower() == 'suma'):
        if opcionsuma == 'edad':
            sumaedad(max_edad)
            print("")
        elif opcionsuma == 'promedio':
            sumaprom(max_promedio)
            print("")
        main()
    elif (comando.lower() == 'cuenta'):
        print("El numero de registros es : " + str(len(num_nombres)))
        print("")
        main()
    elif (comando3.lower() == 'reportar'):
        n = lectura.replace(" " , "")
        n = n[8:]
        html = '<!DOCTYPE html> \n <html lang="en"> \n <head> \n <meta charset="utf-8"> \n <title>Datos reportados</title> \n <link rel="stylesheet" href="css/bootstrap.min.css">'
        html = html + '<style> \n body { background-image: url("fondo.jpg");\n background-size: cover;}\n .container{ margin-top: 200px;}\n </style> \n</head> \n <body> \n <div class="container"> \n <h1 class="text-center bg-info text-primary"><strong>Tabla de Datos</strong></h1> \n <table class="table table-bordered text-center"> \n <tr class="info">'
        for aux in range(len(titulo)):
            nomb = '<th class="text-center">' + titulo[aux] + '</th>'
            html = html + nomb
        m = int(n)
        for elem in range(m):
            temp = '<tr class="warning"> \n <td>' + str(num_nombres[elem]) + '</td> <td>' + str(max_edad[elem]) + '</td> <td>' + str(table_activo[elem]) + '</td> <td>' + str(max_promedio[elem]) + '</td>'  
            temp = temp + '\n </tr> \n'
            html = html + temp
        html = html + ' </table> \n </div> \n </body> \n </html>'
        crear = open('reportes.html' , 'w')
        crear.write(html)
        crear.close()
        webbrowser.open_new_tab('reportes.html')
        main()
    else:
        exit()

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