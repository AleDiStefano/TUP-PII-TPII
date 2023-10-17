from usuario import *
from curso import *

class Profesor(Usuario):
    def __init__(self,nombre:str,apellido:str,email:str,contrasenia:str,titulo:str,anio_egreso:int) -> None:
        super().__init__(nombre,apellido,email,contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []
    @property
    def titulo(self) -> str:
        return self.__titulo.title()

    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        self.__titulo = nuevo_titulo
    
    @property
    def anio_egreso(self) -> str:
        return self.__anio_egreso.title()

    @anio_egreso.setter
    def anio_egreso(self, nuevo_anio_egreso: str):
        self.__anio_egreso = nuevo_anio_egreso
        
    def __str__(self) -> str:
        return f"El profesor se llama: {self.nombre} {self.apellido} con titulo {self.__titulo}"
    
    def validar_credenciales(self, email, contrasenia):
        pass

    def dictar_cursos(self,nombre_curso):
        curso = Curso(nombre_curso) 
        self.__mis_cursos.append(curso)
        return curso



