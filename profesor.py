from usuario import *
from curso import *
from data_cursos import *

class Profesor(Usuario):
    def __init__(self,nombre:str,apellido:str,email:str,contrasenia:str,titulo:str,anio_egreso:int) -> None:
        super().__init__(nombre,apellido,email,contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []
    @property
    def titulo(self) -> str:
        return self.__titulo.title()

    @titulo.setter
    def titulo(self, nuevo_titulo: str) -> None:
        self.__titulo = nuevo_titulo
    
    @property
    def anio_egreso(self) -> str:
        return self.__anio_egreso.title()

    @anio_egreso.setter
    def anio_egreso(self, nuevo_anio_egreso: str) -> None:
        self.__anio_egreso = nuevo_anio_egreso
    
    @property
    def mis_cursos(self) -> str:
        if self.__mis_cursos:
            while True:
                indice = 0
                print("Ingrese que curso desea ver")
                for indice,curso in enumerate(self.__mis_cursos):
                    print(f"{indice + 1} - {curso.nombre}")
                opcion = int(input())
                if opcion >= 1 and opcion <= indice + 1:
                    return f"{self.__mis_cursos[opcion - 1]}",(opcion-1),self.__mis_cursos
                else:
                    print("Debe ingresar un numero de indice valido")
        else:
            return "Usted no a dictado ningun curso"
        
    def __str__(self) -> str:
        return f"El profesor se llama: {self.nombre} {self.apellido} con titulo {self.__titulo}"
    
    def validar_credenciales(self, email:str, contrasenia:str) -> bool:
        return self.email.upper() == email.upper() and self.contrasenia == contrasenia

    def dictar_cursos(self,nombre_curso:str) -> str:
        curso = Curso(nombre_curso) 
        for cur in cursos:
            if cur.nombre.upper() == nombre_curso.upper():
                return print(f"El curso {nombre_curso} ya se encuentra cargado")
        else:
            self.__mis_cursos.append(curso)
            cursos.append(curso)
            print(f"Curso dado de alta exitosamente:\nNombre: {nombre_curso}\nCódigo:{curso.codigo} \nContraseña: {curso.contrasenia_matricula}")
            return curso