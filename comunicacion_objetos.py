from abc import ABC, abstractmethod

class individuo(ABC):

    def __init__(self):
        self.nombre = None

    @abstractmethod
    def saludar(self):
        pass


class Doctor(individuo):

    def __init__(self):
        super().__init__()
        self.nombre = "Juan perez"
        self.profesion = "médico cirujano"

    def saludar(self, individuo):
        print("Hola, soy el doctor ", self.nombre, "y soy ", self.profesion)
        print("Hola, ",self.nombre," yo me llamo ", individuo.nombre, "y soy ", individuo.profesion)


class Profesor(individuo):

    def __init__(self):
        super().__init__()
        self.nombre = "Roberto Gomez"
        self.profesion = "Profesor de matemáticas"

    def saludar(self, individuo):
        print("Hola, soy el profesor ", self.nombre, "y soy ", self.profesion)
        print("Hola, ",self.nombre," yo me llamo ", individuo.nombre, "y soy ", individuo.profesion)


if __name__ == "__main__":
    doctor = Doctor()
    profesor = Profesor()

    # doctor.saludar(profesor)

    # objeto llamando a un metodo de otro objeto
    profesor.saludar(doctor)


