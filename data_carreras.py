from carrera import * 
from data_cursos import *
from data import *


carreras = [
    Carrera("Tecnicatura en Programacion",2),
    Carrera("Ingenieria en Sistemas",5),
    Carrera("Analista en Sistemas",3),
]

carreras[0].set_nuevo_curso(cursos[0])

carreras[1].set_nuevo_curso(cursos[2])

carreras[2].set_nuevo_curso(cursos[3])
carreras[2].set_nuevo_curso(cursos[4])


carreras[0].set_nuevo_estudiante(estudiantes[0])
carreras[0].set_nuevo_estudiante(estudiantes[1])
carreras[0].set_nuevo_estudiante(estudiantes[2])

carreras[1].set_nuevo_estudiante(estudiantes[3])

carreras[2].set_nuevo_estudiante(estudiantes[4])
carreras[2].set_nuevo_estudiante(estudiantes[5])

