from curso import *
from data_cursos import *
from usuario import *




class Estudiante(Usuario):
    def __init__(self,nombre:str,apellido:str,email:str,contrasenia:str,legajo:int,anio_inscripcion_carrera:int,carrera) -> None:
        super().__init__(nombre,apellido,email,contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos = []
        self.__carrera = carrera
        
    def __str__(self) -> str:
        return f"El estudiante se llama: {self.nombre} {self.apellido} con legajo {str(self.__legajo)}"
    
    @property
    def carrera(self) -> int:
        return self.__carrera
    @property
    def get_carrera(self) -> int:
        return self.__carrera.nombre
    
    @property
    def legajo(self) -> int:
        return self.__legajo.title()
    @legajo.setter
    def legajo(self, nuevo_legajo: int) -> None:
        self.__legajo = nuevo_legajo
    
    @property
    def anio_inscripcion_carrera(self) -> int:
        return self.__anio_inscripcion_carrera
    
    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, nuevo_anio_inscripcion_carrera: int) -> None:
        self.__anio_inscripcion_carrera = nuevo_anio_inscripcion_carrera
    
    @property
    def mis_cursos(self)-> str:
        if self.__mis_cursos: 
            while True:
                indice = 0
                print("Ingrese la opcion ")
                for indice,curso in enumerate(self.__mis_cursos):
                    print(f"{indice + 1} - {curso}")
                opcion = int(input())
                if opcion >= 1 and opcion <= indice + 1:
                    # Para desmatricularme necesito solo el nombre, para realizar el remove
                    return self.__mis_cursos[opcion - 1]
                else:
                    print("Debe ingresar un numero de indice valido")
        else:
            return "Usted no se encuentra anotado a ningun curso"
    
    def matricular_en_curso(self,curso:str,contrasenia:str)  -> None:
        if curso in self.__mis_cursos:
            print(f"Usted ya se encuentra inscripto en {curso}")
        else:
            for i in cursos:
                if i.nombre == curso and i.contrasenia_matricula == contrasenia:
                    self.__mis_cursos.append(curso)
                    return "Curso agregado con exito"
        return "La contraseña es invalida"
       
        
        
        # curso_valido = False
        # if curso in self.__mis_cursos:
        #     print(f"Usted ya se encuentra inscripto en {curso}")
        # else:
        #     for i in cursos:
        #         if i.nombre == curso and i.contrasenia_matricula == contrasenia:
        #             self.__mis_cursos.append(curso)
        #             curso_valido = True
        #             break
        
        # Arreglar que filtre si el curso que queremos agregar esta en la misma carrera que el estudiante
        # Tuve quilombo con el import de carreras (ojo que rompe el data_carreras)
        
        # else:
        #     for i in cursos:
        #         if i.nombre == curso and i.contrasenia_matricula == contrasenia:
        #             for carrera in carreras:
        #                 if i.nombre in carrera.curso and self.legajo in carrera.estudiantes:
        #                     self.__mis_cursos.append(curso)
        #                     curso_valido = True
        #                     break
            # if (curso_valido):
            #     print("Curso agregado con exito") 
            # else:
            #     print("La contraseña es invalida")
    
    def desmatricular_curso(self,curso:str)  -> str:
        self.__mis_cursos.remove(curso)
        return "Curso elimnado exitosamente"


    def validar_credenciales(self, email:str, contrasenia:str) -> bool:
        return self.email.upper() == email.upper() and self.contrasenia == contrasenia