from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    #En el archivo foto.py entregado, modificar los métodos setter de alto y ancho, de forma tal que se lance una excepción de tipo DimensionError en caso de que el nuevo valor ingresado no cumpla con las condiciones descritas. En caso contrario, asignar el nuevo valor al atributo de instancia correspondiente.
    @ancho.setter
    def ancho(self, ancho) -> None:
        if 1 <= ancho <= self.MAX:
            self.ancho = ancho
        else:
            raise DimensionError(f"Valor ingresado está fuera de rango. Por favor ingresar un valor entre 1 y {self.MAX}",ancho, self.MAX)

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if 1 <= alto <= self.MAX:
            self.alto = alto
        else:
            raise DimensionError(f"Valor ingresado está fuera de rango. Por favor ingresar un valor entre 1 y {self.MAX}",alto, self.MAX)


fotito = Foto()
fotito.ancho = 3000