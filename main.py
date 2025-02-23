from abc import ABC, abstractmethod

# Interfaz
class MetodoDePago(ABC):
    @abstractmethod
    def pagar(self, monto: float) -> bool:
        pass
class TarjetaDeCredito(MetodoDePago):
    def pagar(self, monto: float) -> bool:
        print(f"Pagar ${monto} con tarjeta de crédito.")

class PayPal(MetodoDePago):
    def pagar(self, monto: float) -> bool:
        print(f"Pagar ${monto} mediante PayPal.")

class TransferenciaBancaria(MetodoDePago):
    def pagar(self, monto: float) -> bool:
        print(f"Pagar ${monto} mediante transferencia bancaria.")

# srp - Single Responsibility Principle 
# Clase que se encarga de realizar el pago con el método de pago seleccionado para garantizar que la interfaz no sea modificada ni instanciada directamente
class SRP_MetodoDePago:
    def __init__(self, metodo_pago: MetodoDePago):
        self.metodo_pago = metodo_pago

    def realizar_pago(self, monto: float):
        return self.metodo_pago.pagar(monto)

# Uso
if __name__ == "__main__":
    # Crear instancias de los métodos de pago
    tarjeta = TarjetaDeCredito()
    paypal = PayPal()
    transferencia = TransferenciaBancaria()

    # Procesar pagos
    procesador = SRP_MetodoDePago(tarjeta)
    procesador.realizar_pago(100.0)

    procesador = SRP_MetodoDePago(paypal)
    procesador.realizar_pago(50.0)

    procesador = SRP_MetodoDePago(transferencia)
    procesador.realizar_pago(200.0)
