from archivo import *
from curso import *
# from data import *

cursos = [
    Curso("Programación I"),
    Curso("Programación II"),
    Curso("Laboratorio II"),
    Curso("Ingles I"),
    Curso("Ingles II")
]

#crear lista de cursos

fecha1 = datetime.strptime("08/04/2021", "%d/%m/%Y").date()
fecha2 = datetime.strptime("02/06/2020", "%d/%m/%Y").date()
fecha3 = datetime.strptime("05/09/2018", "%d/%m/%Y").date()
fecha4 = datetime.strptime("15/10/2015", "%d/%m/%Y").date()
fecha5 = datetime.strptime("23/01/2023", "%d/%m/%Y").date()

archivos = [
    Archivo("programacion.pdf","pdf",fecha4),
    Archivo("tpi.word","word",fecha3),
    Archivo("practica1.ex","excel",fecha2),
    Archivo("practica2.pdf","pdf",fecha1),
    Archivo("practica3.pdf","pdf",fecha5)
]


cursos[0].nuevo_archivo(archivos[3])
cursos[0].nuevo_archivo(archivos[0])
cursos[0].nuevo_archivo(archivos[2])

cursos[1].nuevo_archivo(archivos[4])

cursos[2].nuevo_archivo(archivos[1])
cursos[2].nuevo_archivo(archivos[4])

cursos[3].nuevo_archivo(archivos[1])
cursos[3].nuevo_archivo(archivos[0])
cursos[3].nuevo_archivo(archivos[4])

cursos[4].nuevo_archivo(archivos[1])



