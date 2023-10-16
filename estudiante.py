from usuario import *

class estudiante(Usuario):
    
    def __init__(self,nombre,apellido,email,contrasenia,legajo,anio_inscripcion_carrera) -> None:
        super().__init__(nombre,apellido,email,contrasenia)
        self._legajo = legajo
        self._anio_inscripcion_carrera = anio_inscripcion_carrera

    def __str__(self) -> str:
        return f"El estudiante se llama: {super()._nombre} {super()._apellido} con legajo {self._legajo}"
    
    @property
    def legajo(self) -> str:
        return self._legajo.title()

    @legajo.setter
    def legajo(self, nuevo_legajo: str):
        self._legajo = nuevo_legajo
    
    @property
    def anio_inscripcion_carrera(self) -> str:
        return self._anio_inscripcion_carrera.title()

    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, nuevo_anio_inscripcion_carrera: str):
        self._anio_inscripcion_carrera = nuevo_anio_inscripcion_carrera