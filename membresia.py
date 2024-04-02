from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int):
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

class Gratis(Membresia):
    @property
    def costo(self):
        return 0

    @property
    def max_dispositivos(self):
        return 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        if 1 <= nueva_membresia <= 4:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return None

    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

class Basica(Membresia):
    @property
    def costo(self):
        return 3000

    @property
    def max_dispositivos(self):
        return 2

    def cambiar_suscripcion(self, nueva_membresia: int):
        if 2 <= nueva_membresia <= 4:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return None

    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

class Familiar(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.__dias_regalo = 7

    @property
    def costo(self):
        return 5000

    @property
    def max_dispositivos(self):
        return 5

    @property
    def dias_regalo(self):
        return self.__dias_regalo

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia in [1, 3, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return None

    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

class SinConexion(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.__dias_regalo = 7

    @property
    def costo(self):
        return 3500

    @property
    def max_dispositivos(self):
        return 2

    @property
    def dias_regalo(self):
        return self.__dias_regalo

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia in [1, 2, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return None

    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

class Pro(Membresia):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.__dias_regalo = 15

    @property
    def costo(self):
        return 7000

    @property
    def max_dispositivos(self):
        return 6

    @property
    def dias_regalo(self):
        return self.__dias_regalo

    def cambiar_suscripcion(self, nueva_membresia: int):
        if 1 <= nueva_membresia <= 3:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return None

    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)
