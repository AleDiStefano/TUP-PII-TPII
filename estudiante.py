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
    
    def matricular_en_curso(self,curso):
        self.__mis_cursos.append(curso)
    
    def validar_credenciales(self, email, contrasenia):
        pass





