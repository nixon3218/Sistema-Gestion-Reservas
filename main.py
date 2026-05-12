from sistema import SistemaGestion

from servicio import ReservaSala
from servicio import AlquilerEquipo
from servicio import AsesoriaEspecializada


sistema = SistemaGestion()


# CLIENTES

sistema.agregar_cliente(
    "Nixon Alvarez",
    "nixon@gmail.com",
    "3201234567"
)

sistema.agregar_cliente(
    "Jo",
    "correo",
    "abc"
)


# SERVICIOS

sala = ReservaSala(
    "Sala Premium",
    100,
    20
)

equipo = AlquilerEquipo(
    "Laptop Gamer",
    80,
    "Computador"
)

asesoria = AsesoriaEspecializada(
    "Asesoria IA",
    120,
    "Ingeniero"
)

sistema.agregar_servicio(sala)
sistema.agregar_servicio(equipo)
sistema.agregar_servicio(asesoria)


# RESERVAS

cliente = sistema.clientes[0]

reserva1 = sistema.crear_reserva(
    cliente,
    sala,
    3
)

reserva1.confirmar()

reserva1.procesar_pago(0.10)

sistema.mostrar_reservas()

print("\nSistema funcionando correctamente")