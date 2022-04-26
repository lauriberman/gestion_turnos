from datetime import datetime
#La idea es que el paciente pida un turno para un determinado profesional
#ingresaría al archivo scv turnos de ese profesional consulto si hay turnos disponible en la fecha
#y horario solicitado. Si hay, ingreso el Dni del paciente y me completa los datos necesarios 
#de forma automatica. Dichos datos fueron validados en carga de paciente.
#Para generar el turno la idea sería saber si determinado profesional atiende todos los día y en que horario- 
#En base a eso armo de forma automatica para una determinada fecha, los horarios que el cliente indique
#En general habría que validar más datos que la fecha no sea menor a la actual. Los espacios en blanco,que los
# intervalos generados sean válido, etc.En general el archivo de turno seria os datos que tiene el diccionario básicamente
turno_generado = {'fecha': '' , 'hora': '','paciente': '','profesional':'', 'consultorio': '' }
lista_turnos =[]
nombre_profesional  = ''
def entregar_turnos():
        while True:
                nombre_profesional = input("Ingrese el nombre del Profesional. Ingrese 0 y sale del menú:\n ").capitalize()
                if (nombre_profesional == '0'):
                        print("Carga de turnos finalizada:")
                        break
                else:
                        turno_generado['fecha'] = datetime.today().strftime('%d-%m-%Y')
                        turno_generado['hora'] = input("Ingrese la hora: ")
                        turno_generado['paciente'] = input("Ingrese el nombre del paciente:").capitalize()
                        turno_generado['profesional'] = nombre_profesional
                        turno_generado['consultorio'] = input("Ingrese el Nro de consultorio: ")
                        lista_turnos.append(turno_generado)
        print(lista_turnos)

