from datetime import *

class Archivo:
    def __init__(self,nombre:str,formato:str,fecha:date = datetime.today().strftime('%d/%m/%Y')) -> None:
        self.__nombre = nombre
        self.__fecha = fecha
        self.__formato = formato

    def __str__(self) -> str:
        return f"{self.__nombre}"
    
    @property
    def nombre(self ) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre:str) -> None:
        self.__nombre = nombre
    
    @property
    def fecha(self) -> date: 
        return self.__fecha
    
    @fecha.setter
    def fecha(self,fecha:date)-> None:
        self.__nombre = fecha
    
    @property
    def formato(self) -> str:
        return self.__formato
    @formato.setter
    def formato(self,formato:str) -> None:
        self.__formato = formato