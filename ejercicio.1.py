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
        

# Aquí le bajamos al escudo primero, como si fuera un chaleco
        if objetivo.escudo >= daño:
            objetivo.escudo -= daño
        else:
            restante = daño - objetivo.escudo
            objetivo.escudo = 0
            objetivo.bateria = max(0, objetivo.bateria - restante)
        
        self.bateria -= 10 # Atacar cansa mucho, mi pez

class RobotDefensa(Robot):
    def recargar(self):
        subida = 30
        self.escudo += subida
        self.bateria -= 5
        print(f"🛡️ {self.nombre} se puso las pilas y recuperó el chaleco. ¡Quedó melo!")

# --- Aquí es donde se arma el mierdero ---

# Creamos al mero mero: Elbergon
elbergon = RobotAtaque("Elbergon", 100, 50)
# Y el otro que va a recibir
victima = RobotDefensa("El-Zanahoria", 80, 20)

print("--- SE ARMÓ EL VISAJE ---")
print(elbergon)
print(victima)
print("-" * 30)

# Elbergon no se queda quieto
elbergon.atacar(victima)

print("\n¿Cómo quedó la vuelta?")
print(elbergon)
print(victima)

