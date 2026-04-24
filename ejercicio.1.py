class Robot:
    def __init__(self, nombre, bateria, escudo):
        self.nombre = nombre
        self.bateria = bateria
        self.escudo = escudo

    def __str__(self):
        return f"[{self.nombre}] -> Energía: {self.bateria}% | Chaleco: {self.escudo}"

class RobotAtaque(Robot):
    def atacar(self, objetivo):
        if self.bateria <= 0:
            print(f"Papi, {self.nombre} está apagado, ¡no tiene ni pa'l bus!")
            return

        daño = 25
        print(f"🔥 ¡{self.nombre} le metió un viaje a {objetivo.nombre}! Lo dejó viendo chispas.")
        


