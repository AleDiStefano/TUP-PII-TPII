from usuario import *
from curso import *


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
                    print(f"{indice + 1} - {curso.nombre}")
                opcion = int(input())
                if opcion >= 1 and opcion <= indice + 1:
                    return f"Nombre: {self.__mis_cursos[opcion - 1].nombre}" # Esto tiene devolver solo el nombre del curso, sin la contraseña
                else:
                    print("Debe ingresar un numero de indice valido")
        else:
            return "Usted no se encuentra anotado a ningun curso"
        # for curso in self.__mis_cursos:
        #     print(curso)
    
    # @mis_cursos.setter
    # def mis_cursos(self,curso):
    #     self.__mis_cursos.append(curso)

    # def matricular_en_curso(self,curso):
    #     if curso in self.__mis_cursos:
    #         print(f"Usted ya se encuentra inscripto en {curso}")
    #     else:
    #         self.__mis_cursos.append(curso)
        # FALTA VALIDACION DE MATRICULA PREGUNTAR
        # Como hacer para saber cual es la contraseña de los cursos desde aca
        # Como parametro tenemos que enviar la contrasenia tambien. 
        # Hay que cargar cursos con profesor y probarlo despues aca
    
    # Testing 1
    def matricular_en_curso(self,curso,contrasenia):
        if curso in self.__mis_cursos:
            print(f"Usted ya se encuentra inscripto en {curso}")
        else:
            if contrasenia == Curso.contrasenia_matricula:
                self.__mis_cursos.append(curso)
    
    def validar_credenciales(self, email, contrasenia):
        return self.email == email and self.contrasenia == contrasenia




