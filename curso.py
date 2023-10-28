import random
import string
from archivo import *

class Curso():
    __prox_codigo = int(0)
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__contrasenia_matricula = self.generar_contrasenia  # Genera la matricula del curso
        self.__archivo = []
        self.__codigo = Curso.__generar_codigo()
    def __str__(self) -> str:
        return f"Nombre:{self.__nombre}\nCodigo:{self.codigo} \nContraseña:{self.__contrasenia_matricula}\nCantidad de archivos: {len(self.__archivo)}"
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevo_nombre:str) -> None:
        self.__nombre = nuevo_nombre
    
    @property
    def contrasenia_matricula(self) -> str:
        return self.__contrasenia_matricula
    @property
    def archivo(self) -> list:
        return self.__archivo
    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @property
    def generar_contrasenia(cls) -> str:
        characters = string.ascii_letters + string.digits
        matricula = ''.join(random.choice(characters) for i in range(8))
        cls.__contrasenia_matricula = matricula
        return cls.__contrasenia_matricula

    @classmethod
    def __generar_codigo(cls)-> int:
        cls.__prox_codigo = cls.__prox_codigo + 1
        return cls.__prox_codigo
    
    def nuevo_archivo(self,archivo:Archivo)-> None:
        self.__archivo.append(archivo)