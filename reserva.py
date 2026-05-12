from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, horas):

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

        if horas <= 0:
            raise ReservaError("Horas inválidas")

    def confirmar(self):

        try:
            self.estado = "Confirmada"
            print("Reserva confirmada")

        except Exception as error:
            raise ReservaError("Error al confirmar") from error

    def cancelar(self):

        self.estado = "Cancelada"

    def procesar_pago(self, descuento=0):

        try:

            costo = self.servicio.calcular_costo(
                self.horas,
                descuento
            )

            print(f"Pago realizado: ${costo}")

        except Exception as error:

            raise ReservaError(
                "Error en el pago"
            ) from error

    def mostrar_reserva(self):

        return (
            f"{self.cliente.nombre} | "
            f"{self.servicio.nombre} | "
            f"{self.estado}"
        )