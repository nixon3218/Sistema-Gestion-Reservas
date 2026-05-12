from cliente import Cliente
from reserva import Reserva

from excepciones import ClienteError
from excepciones import ReservaError

from datetime import datetime


class SistemaGestion:

    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_log(self, mensaje):

        with open("logs.txt", "a", encoding="utf-8") as archivo:

            archivo.write(
                f"{datetime.now()} - {mensaje}\n"
            )

    def agregar_cliente(
        self,
        nombre,
        correo,
        telefono
    ):

        try:

            cliente = Cliente(
                nombre,
                correo,
                telefono
            )

            self.clientes.append(cliente)

            print("Cliente agregado")

        except ClienteError as error:

            self.registrar_log(error)

            print(error)

    def agregar_servicio(self, servicio):

        self.servicios.append(servicio)

    def crear_reserva(
        self,
        cliente,
        servicio,
        horas
    ):

        try:

            reserva = Reserva(
                cliente,
                servicio,
                horas
            )

            self.reservas.append(reserva)

            return reserva

        except ReservaError as error:

            self.registrar_log(error)

            print(error)

    def mostrar_reservas(self):

        for reserva in self.reservas:

            print(
                reserva.mostrar_reserva()
            )