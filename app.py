from profesor import *
from estudiante import *
from curso import *

estudiantes = [
    Estudiante("Gaston", "Koch", "gaston@gmail.com", "gaston1", 1, 2020),
    Estudiante("Alejandro", "Di Stefano", "alejandro@gmail.com", "aleandro2", 2, 2019),
    Estudiante("Julian", "Becerra", "julian@gmail.com", "julian3", 3, 2021),
    Estudiante("Juan", "Perez", "juan@gmail.com", "juan4", 4, 2018),
    Estudiante("Arturo", "Vidal", "arturo@gmail.com", "arturo5", 5, 2022),
    Estudiante("Enzo", "Perez", "enzo@gmail.com", "enzo6", 6, 2017)
]

profesores = [
    Profesor("Nelson", "Andres", "nelson@gmail.com", "nelson1", "Ingeniero Industrial", 2020),
    Profesor("Jorge", "Magallan", "jorge@gmail.com", "jorge2", "Ingeniero Civil", 2019),
    Profesor("Pedro", "Ruiz", "pedro@gmail.com", "pedro3", "Abogado", 2021),
    Profesor("Lionel", "Suarez", "lionel@gmail.com", "lionel4", "Contador", 2018),
    Profesor("Marcos", "Raiti", "marcos@gmail.com", "marcos5", "Medico", 2022),
    Profesor("Norberto", "Ochoa", "norberto@gmail.com", "norberto6", "Programador", 2017)
]

cursos = [
    Curso("Programación I"),
    Curso("Programación II"),
    Curso("Laboratorio II"),
    Curso("Ingles I"),
    Curso("Ingles II")
]

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
            if estudiante.email == emailEst:
                encontrado = True
                valido = estudiante.validar_credenciales(emailEst, contraseniaEst)
                if valido:
                    while True:
                        print("1. Matricularse a un curso")
                        print("2. Ver curso")
                        print("3. Volver al menú principal")
                        opcion = int(input())
                        if opcion >= 1 and opcion <= 3:
                            break
                        else:
                            print("Ingrese una opcion desde el 1 al 3")
                            
                    # SE CONTINUA ACA
                    if opcion == 1:
                        pass
                    elif opcion == 2:
                        pass
                    elif opcion == 3:
                        pass
                else:
                    print("Error de ingreso")
                
        if encontrado == False:
            print("Debe darse de alta en el alumnado")
            
    elif opt == 2:
        emailPro = input("Ingrese su email: ")
        contraseniaPro = input("Ingrese su contraseña: ")
        encontrado = False
        contrasenia_valida = False
        for profesor in profesores:
            if profesor.email == emailPro:
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
                            pass
                        elif opcion == 2:
                            pass
                        elif opcion == 3:
                            pass
                else:
                    print("Error de ingreso")
                    
        if encontrado == False:
            print("Debe darse de alta en el alumnado")
        
    elif opt == 3:
        cursos_ordenados = sorted(cursos, key=lambda curso: curso.nombre)
        for curso in cursos_ordenados:
            print(f"Materia:{curso.nombre} Carrera: Tecnicatura Universitaria en Programación")
            
    elif opt == 4:
        pass



    # encontrado = False
    # contrasenia_valida = False
    # email = input("Ingrese su email: ")
    # contrasenia = input("Ingrese su contraseña: ")
    # for estudiante in estudiantes:
    #     if estudiante.email == email:
    #         encontrado = True
    #         for password in estudiantes:
    #             if password.contrasenia == contrasenia:
    #                 print("Acceso al sistema ")
    #                 contrasenia_valida = True
    #                 # while True:
    #                 #     print("1. Matricularse a un curso")
    #                 #     print("2. Ver curso")
    #                 #     print("3. Volver al menú principal")
    #                 #     opcion = int(input())
    #                 #     if opcion >= 1 and opcion <= 3:
    #                 #         break
    #                 #     else:
    #                 #         print("Ingrese una opcion desde el 1 al 3")
                    
                    
                    
    #         if(contrasenia_valida == False):
    #             print("Error de ingreso")
                    
    # if(encontrado == False):
    #     print("Debe darse de alta en el alumnado")
    
    
    
                # for password in profesores:
            #     if password.contrasenia == contraseniaPro:
            #         print("Credenciales validas")
            #         contrasenia_valida = True
                    
            # if contrasenia_valida == False: