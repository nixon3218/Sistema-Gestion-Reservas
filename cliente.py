from excepciones import ClienteError


class Cliente:
    def __init__(self, nombre, correo, telefono):
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):

        if len(self.__nombre.strip()) < 3:
            raise ClienteError("El nombre es inválido")

        if "@" not in self.__correo:
            raise ClienteError("Correo inválido")

        if not self.__telefono.isdigit():
            raise ClienteError("El teléfono debe contener números")

    @property
    def nombre(self):
        return self.__nombre

    def mostrar_info(self):
        return f"{self.__nombre} - {self.__correo}"