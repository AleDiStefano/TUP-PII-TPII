from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia
    
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
        return self._email

    @email.setter
    def email(self, nuevo_email: str):
        self._email = nuevo_email
        
    @property
    def contrasenia(self) -> str:
        return self._contrasenia
            
    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia: str):
        self._contrasenia = nueva_contrasenia
    
    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def validar_credenciales(self, email, contrasenia) -> bool:
        return True if self.email == email and self.contrasenia == contrasenia else False
