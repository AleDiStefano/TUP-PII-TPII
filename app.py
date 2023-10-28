from archivo import *
from curso import *
from data import *
from data_cursos import *
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
                            for indice,curso in enumerate(cursos):
                                # borrar contraseña (es testing)
                                print(f"{indice + 1} - {curso.nombre} - {curso.contrasenia_matricula}")
                            op = int(input())
                            if opcion >= 1 and opcion <= 5:
                                break
                            else:
                                print("Ingrese una opcion desde el 1 al 5")
                        contraseniaEst = input("Ingrese la matricula del curso: ")
                        cursoEst = cursos[op-1].nombre
                        estudiante.matricular_en_curso(cursoEst,contraseniaEst)
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
                        i = 0
                        for indice,estudiante in enumerate(estudiantes):
                            if emailEst == estudiantes[i].email:
                                curso = estudiante.mis_cursos
                                for cursoItera in cursos:
                                    if curso == cursoItera.nombre:
                                        for archivo in cursoItera.archivo:
                                            archivos_ordenados = sorted(cursoItera.archivo, key=lambda archivo: archivo.fecha)
                            i += 1
                        for archivos_ordenados in archivos_ordenados:
                            print(archivos_ordenados)
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
                        nombre_curso = input("Ingrese el nombre del curso que desea dictar: ")
                        curso_nuevo = profesor.dictar_cursos(nombre_curso)
                    elif opcion == 2:
                        mostrarCursoDictado,curso_elejido,lista_cursos = profesor.mis_cursos
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
                    elif opcion == 3:
                        break
                else:
                    print("Error de ingreso, por favor intente nuevamente")
                    
        if encontrado == False:
            print("Usuario no cargado, debe darse de alta en el alumnado")
        
    elif opt == 3:
        cursos_ordenados = sorted(cursos, key=lambda curso: curso.nombre)
        for curso in cursos_ordenados:
            print(f"Materia:{curso.nombre}       Carrera: Tecnicatura Universitaria en Programación")
            
    elif opt == 4:
        break