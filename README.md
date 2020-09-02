# Practica Única 201807086

## Introduccion

Este proyecto tiene como funcionalidad trabajar con la lectura de archivos en formato .json, en el cual se simula una consola propia en la cual tiene algunos comandos para trabajar con este tipo de archivos.
### Comandos admitidos:
* Cargar
* Seleccionar
* Maximo
* Minimo
* Suma
* Cuenta
* Reportar
Nota: Los comandos pueden escribirse alternando mayusculas y minisculas se utiliza case insensitive.

Se presenta la funcionalidad de cada comando:
### Comando Cargar:
Este comando sirve para cargar en memoria archivos de la extensión .json, el cual tiene la siguiente estructura: **cargar archivo1.json, archivo2.json .... archivoN.json**


### Comando Seleccionar:
El siguiente comando nos sirve para seleccionar todos los datos para mostrar en consola, teniendo como estructura la siguiente forma:	**Seleccionar * **

Nota: Solo esta desarollada la funcionalidad para seleccionar todos los elementos.

### Comando Maximo
Este comando tiene la funcionalidad de calcular el valor maximo del atributo que deseemos, este tiene la siguiente estructura: **maximo edad**
Este comando solo calcula el maximo de los atributos edad y promedio, se calculan de forma independiente en cada linea de la consola.
### Comando Minimo
Este comando tiene la funcionalidad de calcular el valor maximo del atributo que deseemos, este tiene la siguiente estructura: **minimo edad**
Este comando solo calcula el minimo de los atributos edad y promedio, estros traibutos se calculan de forma independiente en cada linea de la consola.
### Comando Suma
Este comando tiene la funcionalidad de calcular la suma del atributo que deseemos en todos los archivos cargados a memoria previamente, este tiene la siguiente estructura: 
**suma edad**
Este comando solo calcula la suma de los atributos edad y promedio, estos atributos se calculan de forma independiente en cada linea de la consola.

### Comando Cuenta
Este comando tiene la funcionalidad de imprimir en pantalla el numero de registros que hemos cargado en nuestra consola, y este comando tiene la siguiente estructura: **cuenta**
###Comando Reportar
Este comando tiene como funcion de mostrar en un archivo html el numero de registros que nosotros solicitemos en consola, este comando tiene la siguiente estructura: **reportar n**
Donde n es el numero de registros que se desea reportar
