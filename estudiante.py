from usuario import *
from curso import *
from data_cursos import *

class Estudiante(Usuario):
    def __init__(self,nombre:str,apellido:str,email:str,contrasenia:str,legajo:int,anio_inscripcion_carrera:int) -> None:
        super().__init__(nombre,apellido,email,contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos = []
        
    def __str__(self) -> str:
        return f"El estudiante se llama: {self.nombre} {self.apellido} con legajo {str(self.__legajo)}"
    
    @property
    def legajo(self) -> str:
        return self.__legajo.title()
    @legajo.setter
    def legajo(self, nuevo_legajo: str):
        self.__legajo = nuevo_legajo
    
    @property
    def anio_inscripcion_carrera(self) -> str:
        return self.__anio_inscripcion_carrera.title()
    
    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, nuevo_anio_inscripcion_carrera: str):
        self.__anio_inscripcion_carrera = nuevo_anio_inscripcion_carrera
    
    @property
    def mis_cursos(self):
        if self.__mis_cursos: 
            while True:
                indice = 0
                print("Ingrese que curso desea ver")
                for indice,curso in enumerate(self.__mis_cursos):
                    print(f"{indice + 1} - {curso}")
                opcion = int(input())
                if opcion >= 1 and opcion <= indice + 1:
                    return f"Nombre: {self.__mis_cursos[opcion - 1]}" # Esto tiene devolver solo el nombre del curso, sin la contraseña
                else:
                    print("Debe ingresar un numero de indice valido")
        else:
            return "Usted no se encuentra anotado a ningun curso"

    def matricular_en_curso(self,curso,contrasenia):
        curso_valido = False
        if curso in self.__mis_cursos:
            print(f"Usted ya se encuentra inscripto en {curso}")
        else:
            for i in cursos:
                if i.nombre == curso and i.contrasenia_matricula == contrasenia:
                    self.__mis_cursos.append(curso)
                    curso_valido = True
                    break
            if (curso_valido):
                print("Curso agregado con exito") 
            else:
                print("La contraseña es invalida")

    def validar_credenciales(self, email, contrasenia):
        return self.email == email and self.contrasenia == contrasenia




