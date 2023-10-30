from archivo import *
from carrera import * # REVISAR QUE NO PINCHE
from curso import *
from data import *
from data_cursos import *
from data_carreras import *
from datetime import *
from estudiante import *
from profesor import *


def menu():
    while True:
        print("1. Ingresar cómo alumno")
        print("2. Ingresar cómo profesor")
        print("3. Ver cursos")
        print("4. Salir")
        opt = int(input())
        if opt >= 1 and opt <= 4:
            return opt
        else:
            print("Ingrese una opcion desde el 1 al 4")

while True:
    opt = menu()
    if opt == 1:
        encontrado = False
        contrasenia_valida = False
        emailEst = input("Ingrese su email: ")
        contraseniaEst = input("Ingrese su contraseña: ")
        for estudiante in estudiantes:
            if estudiante.email.upper() == emailEst.upper():
                encontrado = True
                valido = estudiante.validar_credenciales(emailEst, contraseniaEst)
                if valido:
                    while True:
                        print("1. Matricularse a un curso")
                        print("2. Desmatricularse a un curso")
                        print("3. Ver curso")
                        print("4. Volver al menú principal")
                        opcion = int(input())
                        if opcion >= 1 and opcion <= 4:
                            break
                        else:
                            print("Ingrese una opcion desde el 1 al 3")
                            
                    if opcion == 1:
                        while True:
                            print("Seleccione el curso")
                            # for indice,curso in enumerate(cursos):
                            #     # borrar contraseña (es testing)
                            #     print(f"{indice + 1} - {curso.nombre} - {curso.contrasenia_matricula}")
                            carrera = estudiante.get_carrera
                            for carrera_iterador in carreras:
                                if carrera == carrera_iterador.nombre:
                                    for index,curso in enumerate(carrera_iterador.curso):
                                        print(f"{str(index+1)} - {curso.nombre} {curso.contrasenia_matricula}")
                            op = int(input())
                            if op >= 1 and op <= index+1:
                                # cursoEst = cursos[op-1].nombre
                                cursoEst = carrera_iterador.curso[op-1].nombre
                                contraseniaEst = input("Ingrese la matricula del curso: ")
                                msg_agregado = estudiante.matricular_en_curso(cursoEst,contraseniaEst)
                                print(msg_agregado)
                            else:
                                print("Ingrese una opcion desde el 1 al 5")
                            break
                    elif opcion == 2:
                        i = 0
                        for indice,estudiante in enumerate(estudiantes):
                            if emailEst == estudiantes[i].email:
                                #curso es igual al nombre del arreglo mis cursos, con eso hago el remove
                                curso = estudiante.mis_cursos
                                msg_borrado = estudiante.desmatricular_curso(curso)
                                print(msg_borrado)
                            i += 1
                    elif opcion == 3:
                        # ARREGLAR
                        # Si no tiene ningun curso tiraba error de que esta variable no estaba definida (se define solo si entra al bucle)
                        # hay que intentar arreglarlo desde la clase de estudiante, pero si no tiene cursos no entra directamente
                        
                        i = 0
                        archivos_ordenados = [] 
                        for indice,estudiante in enumerate(estudiantes):
                            if emailEst == estudiantes[i].email:
                                curso = estudiante.mis_cursos
                                for cursoItera in cursos:
                                    if curso == cursoItera.nombre:
                                        archivos_ordenados = sorted(cursoItera.archivo, key=lambda archivo: archivo.fecha)
                                        for archivo in archivos_ordenados:
                                            print(archivo)
                                break
                            i += 1
                else:
                    print("Error de ingreso, por favor intente nuevamente")
        if encontrado == False:
            print("Usuario no cargado, debe darse de alta en el alumnado")
            
    elif opt == 2:
        emailPro = input("Ingrese su email: ")
        contraseniaPro = input("Ingrese su contraseña: ")
        encontrado = False
        contrasenia_valida = False
        for profesor in profesores:
            if profesor.email.upper() == emailPro.upper():
                encontrado = True
                valido = profesor.validar_credenciales(emailPro,contraseniaPro)
                if valido:
                    while True:
                        print("1. Dictar curso")
                        print("2. Ver curso")
                        print("3. Volver al menú principal")
                        opcion = int(input())
                        if opcion >= 1 and opcion <= 3:
                            break
                        else:
                            print("Ingrese una opcion desde el 1 al 3")
                    if opcion == 1:
                        # ARREGLAR: CUANDO DOY DE ALTA EL CURSO NO LO ESTOY DANDO DE ALTA EN LA CARRERA, la mayuscula parecia que estaba gritando perdon JAJJAJAJA
                        while True:
                            for index,carrera in enumerate(carreras):
                                print(f"{str(index+1)} - {carrera.nombre}")
                            op_carrera = int(input())
                            if op_carrera >= 1 and op_carrera <= index+1:
                                break
                            else:
                                print("Numero de indice invalido")
                        carrera_elejida = carreras[op_carrera-1]
                        
                        nombre_curso = input("Ingrese el nombre del curso que desea dictar: ")
                        curso_nuevo,valido = profesor.dictar_cursos(nombre_curso)
                        if valido:
                            # Voy a hacer que profesor, ademas de retornar el curso objeto me devuelva un bool, asi solamente se agregue el curso a la carrera si el proceso tuvo exito
                            carrera_elejida.set_nuevo_curso(curso_nuevo) # Una vez seleccionado el curso recien se valida, hay que ver
                            # for x in carrera_elejida.curso:
                            #     print(x)
                        else:
                            print("El proceso no tuvo exito")
                    elif opcion == 2:
                        tiene_cursos,mostrarCursoDictado,curso_elejido,lista_cursos = profesor.mis_cursos
                        if tiene_cursos:
                            print(mostrarCursoDictado)
                            op = input("\n Desea ingresar un archivo adjunto? S/N: ").upper()
                            if op == "S":
                                nombre_archivo = input("Ingrese el nombre: ")
                                formato_archivo = input("Ingrese el formato: ")
                                nombre_archivo = f"{nombre_archivo}.{formato_archivo}"
                                lista_cursos[curso_elejido].nuevo_archivo(Archivo(nombre_archivo,formato_archivo))
                                break
                            elif op == "N":
                                break
                            else:
                                print("Opcion invalida")
                        else:
                            print("Usted no a dictado ningun curso")
                    elif opcion == 3:
                        break
                else:
                    print("Error de ingreso, por favor intente nuevamente")
                    
        if encontrado == False:
            codigo_admin = input("Usuario no cargado, si desea darlo de alta ingrese el código de administrador: ")
            if codigo_admin == 'admin':
                nombrePro = input("Ingrese su nombre: ")
                apellidoPro = input("Ingrese su apellido: ")
                tituloPro = input("Ingrese su titulo: ")
                anio_egresoPro = int(input("Ingrese su año de egreso: "))
                nuevo_profesor = Profesor(nombrePro, apellidoPro, emailPro, contraseniaPro, tituloPro, anio_egresoPro)
                profesores.append(nuevo_profesor)
                print("Usuario agregado exitosamente, inicie sesion por primera vez")
            else:
                print("Código de administrador incorrecto")
        
    elif opt == 3:
        cursos_ordenados = sorted(cursos, key=lambda curso: curso.nombre)
        for curso in cursos_ordenados:
            print(f"Materia:{curso.nombre}       Carrera: Tecnicatura Universitaria en Programación")
            
    elif opt == 4:
        break