from profesor import *
from estudiante import *
from matricula_curso import *

class Curso():
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__contrasenia_matricula = generar()  # Genera la matricula del curso
        
    def __str__(self) -> str:
        return f"Nombre del curso: {self.__nombre}"
    
    def generar_contrasenia(self) -> str:
        pass
    
    @property
    def nombre(self):
        return self.__nombre