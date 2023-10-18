from profesor import *
from estudiante import *
from curso import *
# juan@gmail.com
estudiantes = [
    Estudiante("Gaston", "Koch", "gaston@gmail.com", "gaston1", 1, 2020),
    Estudiante("Alejandro", "Di Stefano", "alejandro@gmail.com", "aleandro2", 2, 2019),
    Estudiante("Julian", "Becerra", "julian@gmail.com", "julian3", 3, 2021),
    Estudiante("Juan", "Perez", "j", "juan4", 4, 2018),
    Estudiante("Arturo", "Vidal", "arturo@gmail.com", "arturo5", 5, 2022),
    Estudiante("Enzo", "Perez", "enzo@gmail.com", "enzo6", 6, 2017)
]
# nelson@gmail.com
profesores = [
    Profesor("Nelson", "Andres", "n", "nelson1", "Ingeniero Industrial", 2020),
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
                            
                    if opcion == 1:
                        while True:
                            print("Seleccione el curso")
                            for indice,curso in enumerate(cursos):
                                print(f"{indice + 1} - {curso.nombre}")
                            op = int(input())
                            if opcion >= 1 and opcion <= 5:
                                break
                            else:
                                print("Ingrese una opcion desde el 1 al 5")
                                
                        cursoEst = cursos[op-1]
                        estudiante.matricular_en_curso(cursoEst)
                    elif opcion == 2:
                        mostrarCurso = estudiante.mis_cursos
                        print(mostrarCurso)
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
                        nombre_curso = input("Ingrese el nombre del curso que desea dictar: ")
                        curso_nuevo = profesor.dictar_cursos(nombre_curso)
                    elif opcion == 2:
                        mostrarCursoDictado = profesor.mis_cursos
                        print(mostrarCursoDictado)
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
        break
