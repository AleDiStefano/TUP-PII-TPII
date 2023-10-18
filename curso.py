# from profesor import * Esto esta asi por que sino en profesor - dictar_curso el curso me figuraba como undefined
from estudiante import *
from matricula_curso import *

class Curso():
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__contrasenia_matricula = generar()  # Genera la matricula del curso
        
    def __str__(self) -> str:
        return f"Nombre:{self.__nombre} \nContraseña:{self.__contrasenia_matricula}"
    
    def generar_contrasenia(self) -> str:
        # Por que no se llama el generar() aca. Cual es la funcionalidad de esta funcion
        pass
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def contrasenia_matricula(self):
        return self.__contrasenia_matricula

