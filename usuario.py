from abc import ABC, abstractmethod

class Usuario(ABC):
    # De esta manera nos aseguramos que el mail es unique
    __mail_disponibles = set()
    
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str) -> None:
        self._nombre = nombre
        self._apellido = apellido
        if email in Usuario.__mail_disponibles:
            raise ValueError("Ya existe un usuario con ese email")
        self._email = email
        self._contrasenia = contrasenia
        Usuario.__mail_disponibles.add(email)
    
    @property
    def nombre(self) -> str:
        return self._nombre.title()

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self._nombre = nuevo_nombre

    @property
    def apellido(self) -> str:
        return self._apellido.title()

    @apellido.setter
    def apellido(self, nuevo_apellido: str) -> None:
        self._apellido = nuevo_apellido
        
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, nuevo_email: str) -> None:
        self._email = nuevo_email
        
    @property
    def contrasenia(self) -> str:
        return self._contrasenia
            
    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia: str) -> None:
        self._contrasenia = nueva_contrasenia
    
    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def validar_credenciales(self, email, contrasenia) -> bool:
        return True if self.email == email and self.contrasenia == contrasenia else False