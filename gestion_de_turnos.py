# Proyecto Final Python Inicial
# Autor : Leandro Hernán Ibarra
# Versión: 1.0
# Última fecha de modificación 29/04/22

from datetime import datetime
import turnos
now = datetime.now()

import csv

def agregar_usuario(): 
    nombre = '0' 
    while True :
        
        nombre = input("Ingrese un Nombre. Ingrese 0 para salir\n").capitalize()
        if nombre == '0':
                print("Ha salido del menú ingresar usuario")
                break
        else:
            nombre.capitalize()
            apellido = input("Ingrese el apellido:").capitalize()  
            # Pongo los encabezados del archivo usuario en el mismo orden  
            header = ['nombre','apellido', 'dni']
             # abro el archivo en moso append para poder agregar nuevas filas
            csvfile = open('usuario.csv', 'a', newline='')
            # Generar un "escritor" para modificar el archivo
            writer = csv.DictWriter(csvfile, fieldnames=header)
            # Genero nuevo usuario
            dni = str(input("Ingrese el número de DNI:"))  
            dni_validado = validar_dni(dni)
            if dni_validado == True:
                print("El número de DNI ya fue ingresado.")
                break
            
            nuevo_usuario = {'nombre': nombre, 'apellido':apellido, 'dni': dni}
            # Lo escribirlo en el archivo
            writer.writerow(nuevo_usuario)
            # Cierro el archivo
            csvfile.close()


def validar_dni(dni):
    with open('usuario.csv') as csvfile:
        data = list(csv.DictReader(csvfile))    
        for i in range(len(data)):
            dni_archivo = data[i].get('dni') # Busca en el archivo si el dni ya fue cargado 
            if dni_archivo == dni:
                return True


def logear_usuario(dni_ingresado): 
   fecha =  datetime.today().strftime('%d-%m-%Y')
   
   with open('usuario.csv') as csvfile:
        data = list(csv.DictReader(csvfile)) 
       # dni = input("Ingrese su nro de DNI:")
        for i in range(len(data)):
            dni_archivo = data[i].get('dni') # Si el usuario fue cargado en archivo 'usuario' lo busca por dni y completa los 
            if (dni_archivo == dni_ingresado):           #los datos del archivo 'registro_usuario'
                data[i]
                dni_ingresado = data[i].get('dni')
                nombre = data[i].get('nombre')
                apellido = data[i].get('apellido')
                #hora = now.hour, ':', now.minute
                hora = now.time()
                header = ['fecha', 'hora', 'dni', 'nombre', 'apellido']
                csvfile = open('registro_usuario.csv', 'a', newline='')
                # Generar un "escritor" para modificar el archivo
                writer = csv.DictWriter(csvfile, fieldnames=header)
                # Genero nuevo usuario        
                ingreso_usuario = {'fecha':fecha, 'hora': hora, 'dni':dni_ingresado, 'nombre':nombre, 'apellido':apellido}
                # Lo escribirlo en el archivo
                writer.writerow(ingreso_usuario)
               # Cierro el archivo
                csvfile.close()
                print("Usted se registro exitosamente!")
                mostrar_menu()
            
           
def mostrar_menu():      
   
    print("Cargar un nuevo Usuario : 1 ")
    print("Agregar Pacientes :       2 ")
    print("Entregar Turnos:          3 ")
    print("Cargar profesionales:     4 ")
    print("Consultar turnos:         5 ")
    print("Salir:                    6 ")
    opcion = input()
    if(opcion == '1'):
        agregar_usuario()
    elif (opcion == '2'):
        agregar_paciente()
    elif(opcion == '3'):
        turnos.entregar_turnos()
    elif(opcion == '4'):
        cargar_profesional()
    elif(opcion == '5'):
        consultar_turnos()
    elif(opcion == '6'):
        print("Usted a Salido del sistema:")
        quit
    else:
        print("La opcion seleccionada no es correcta: ")
       
       
def agregar_paciente():
    print("ingresar los datos paciente:")
    #procedimiento igual al de cargar usuario
    #hacemos la tabla con los datos que requiera el potencial cliente
def entregar_turnos():
    print("entregar turno")
def cargar_profesional():
    print("idem a carga de usuario:")

def consultar_turnos():
    print("Los turnos disponibles son:\n")

if __name__ == '__main__':
    print("La fecha de hoy es:")
    print(datetime.today().strftime('%d-%m-%Y'))
    print(f"Es la Hora: {now.hour} :{now.minute} Minutos")
    print("**********************")
    print("BIENVENIDX al Sistema:")
    print("**********************")
    print("Opciones disponibles: ")
    print("Identificarse : 1 ")
    print("Registrarse   : 2 ")
    

    
    entrar = input()
    if(entrar == '1'):
        dni_ingresado = input("Ingrese el DNI: ")
        dni_validado = validar_dni(dni_ingresado)
        if(dni_validado == True):
            logear_usuario(dni_ingresado)
        else:
            print("El usuario no fue ingresado, o datos incorrectos:")
            
    elif(entrar == '2'):
        agregar_usuario()
    else:
        print("Datos incorrectos:")
   # Registramos quien esta usando el sistema en la fecha y hora guardada
   # Por seguridad se podría hacer otro archivito de salida, y antes que salgan 
   #vuelvan a poner su dni. Ahí quedaría el intervalo de tiempo de quien uso el sistema

    