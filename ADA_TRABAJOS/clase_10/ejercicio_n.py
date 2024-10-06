# Programar una cuenta bancaria y hacer un depósito
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo_actual = saldo
        # Atributo privado

    def depositar(self, dinero):
        if dinero > 0:
            saldo_anterior = self.__saldo_actual
            self.__saldo_actual += dinero
            return f'Deposito de ${dinero}\nTu cuenta tenía ${saldo_anterior}'
        return 'Cantidad no válida'
    
    def obtener_saldo(self):
        return f'Saldo final es de ${self.__saldo_actual}'

cuenta = CuentaBancaria(1000)
print(cuenta.depositar(500)) # Imprime el print del método depósito
print(cuenta.obtener_saldo()) # Imprime el saldo actual