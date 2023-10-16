from usuario import *

class profesor(Usuario):
    
    def __init__(self,nombre,apellido,email,contrasenia,titulo,anio_egreso) -> None:
        super().__init__(nombre,apellido,email,contrasenia)
        self._titulo = titulo
        self._anio_egreso = anio_egreso

    def __str__(self) -> str:
        return f"El profesor se llama: {super()._nombre} {super()._apellido} con titulo {self._titulo}"

    @property
    def titulo(self) -> str:
        return self._titulo.title()

    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        self._titulo = nuevo_titulo
    
    @property
    def anio_egreso(self) -> str:
        return self._anio_egreso.title()

    @anio_egreso.setter
    def anio_egreso(self, nuevo_anio_egreso: str):
        self._anio_egreso = nuevo_anio_egreso
        