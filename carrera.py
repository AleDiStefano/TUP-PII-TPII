from curso import *
from data_cursos import *
from estudiante import *

class Carrera:
    def __init__(self,nombre:str,cant_anios:int)->None:
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        self.__curso = []
        self.__estudiantes = []
    
    @property
    def nombre(self)->str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre) ->None:
        self.__nombre = nuevo_nombre
    
    @property
    def cant_anios(self)->int:
        return self.__cant_anios
    
    @cant_anios.setter
    def cant_anios(self,nuevo_cant_anios) ->None:
        self.__cant_anios = nuevo_cant_anios
    
    @property
    def curso(self) -> list:
        return self.__curso
    
    @property
    def estudiantes(self) -> list:
        return self.__estudiantes
    
    # Al intentar utilizar sus setters para realizar un append, me daba error.
    # Por lo que cree metodos para poder agregar
    
    # @curso.setter
    # def curso(self,nuevo_curso) ->None:
    #     self.curso.append(nuevo_curso)
    
    # @estudiantes.setter
    # def estudiantes(self,nuevo_estudiante) ->None:
    #     self.__estudiantes.append(nuevo_estudiante)
    
    def set_nuevo_curso(self,curso) -> None:
        self.__curso.append(curso)
        
    def set_nuevo_estudiante(self,estudiante) -> None:
        self.__estudiantes.append(estudiante)
        
    def __str__(self)->str:
        return f"Nombre: {self.__nombre} \nCantidad de años: {self.__cant_anios}"
    
    def get_cantidad_materias(self)->int:
        cantidad_materias = len(self.cursos)
        return cantidad_materias


