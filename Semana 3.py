# Programación Tradicional: Promedio semanal del clima

def ingresar_temperaturas():
    """
    Función para ingresar las temperaturas de 7 días
    """
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función para calcular el promedio semanal
    """
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio


# Programa principal
def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA (PROGRAMACIÓN TRADICIONAL) ===")
    temperaturas = ingresar_temperaturas()
    promedio_semanal = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio_semanal:.2f} °C")


# Ejecución del programa
main()
# Programación Orientada a Objetos: Promedio semanal del clima

class Clima:
    def __init__(self):
        # Encapsulamiento: atributo protegido
        self._temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self._temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal
        """
        return sum(self._temperaturas) / len(self._temperaturas)


# Herencia
class ClimaSemanal(Clima):
    def mostrar_promedio(self):
        """
        Polimorfismo: método que usa el cálculo heredado
        """
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Programa principal
def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA (POO) ===")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()


# Ejecución del programa
main()
