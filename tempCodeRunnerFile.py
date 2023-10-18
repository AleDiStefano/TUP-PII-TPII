# from profesor import * Esto esta asi por que sino en profesor - dictar_curso el curso me figuraba como undefined
from estudiante import *
from matricula_curso import *

class Curso():
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__contrasenia_matricula = self.generar_contrasenia  # Genera la matricula del curso
        
    def __str__(self) -> str:
        return f"Nombre:{self.__nombre} \nContraseña:{self.__contrasenia_matricula}"
    
    @property
    def generar_contrasenia(cls) -> str:
        # Por que no se llama el generar() aca. Cual es la funcionalidad de esta funcion
        characters = string.ascii_letters + string.digits
        matricula = ''.join(random.choice(characters) for i in range(8))
        cls.__contrasenia_matricula = matricula
        return cls.__contrasenia_matricula

    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def contrasenia_matricula(self):
        return self.__contrasenia_matricula


cursito = Curso("cursotest")

print(cursito)