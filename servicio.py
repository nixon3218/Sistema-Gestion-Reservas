from abc import ABC, abstractmethod
from excepciones import ServicioError


class Servicio(ABC):

    def __init__(self, nombre, costo_base):

        self.nombre = nombre
        self.costo_base = costo_base

        if costo_base <= 0:
            raise ServicioError("Costo inválido")

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, nombre, costo_base, capacidad):

        super().__init__(nombre, costo_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas=1, descuento=0):

        total = self.costo_base * horas
        total -= total * descuento

        return total

    def descripcion(self):

        return f"Sala para {self.capacidad} personas"


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base, tipo):

        super().__init__(nombre, costo_base)
        self.tipo = tipo

    def calcular_costo(self, horas=1, descuento=0):

        total = (self.costo_base * horas) + 20
        total -= total * descuento

        return total

    def descripcion(self):

        return f"Equipo tipo {self.tipo}"


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, costo_base, experto):

        super().__init__(nombre, costo_base)
        self.experto = experto

    def calcular_costo(self, horas=1, descuento=0):

        total = (self.costo_base * horas) + 50
        total -= total * descuento

        return total

    def descripcion(self):

        return f"Asesoría con {self.experto}"