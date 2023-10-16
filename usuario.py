from abc import ABC, abstractmethod

class Usuario(ABC):

    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia
        
    def __str__(self) -> str:
        return f"{self._nombre} {self._apellido}"
    
    @property
    def nombre(self) -> str:
        return self._nombre.title()

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre

    @property
    def apellido(self) -> str:
        return self._apellido.title()

    @apellido.setter
    def apellido(self, nuevo_apellido: str):
        self._apellido = nuevo_apellido
        
    @property
    def email(self) -> str:
        return self._email.title()

    @email.setter
    def email(self, nuevo_email: str):
        self._email = nuevo_email
            
        @contrasenia.setter
        def contrasenia(self, nueva_contrasenia: str):
            self._contrasenia = nueva_contrasenia
    
