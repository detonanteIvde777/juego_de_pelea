# juego_de_pelea

### 🤖 Proyecto: Robots de Mecha (Edición Medallo City)
¡Qué dice, mi fai! Bienvenid@ a este repositorio. Aquí lo que hay es puro código de alto voltaje para simular unos robocitos dándose en la torre. Es pura Programación Orientada a Objetos, pero sin tanto visaje técnico aburridor, sino con toda la esencia de la calle.

### 🚀 ¿De qué trata esta vuelta?
El código es un simulador de combate. Tenemos unos robots que se creen muy leones y se dan madera entre ellos. La lógica es clara: el que se descuide, ¡paila!, lo dejan viendo chispas.

- La Jerarquía: Tenemos un patrón (la clase Robot) y de ahí salen los que reparten y los que aguantan.

- El Chaleco: Antes de que les toquen el motor (la batería), tienen que acabarles el escudo. ¡Como en la vida real, el que tiene el chaleco puesto aguanta más el voltaje!

- El Cansancio: Atacar cansa, mi pez. Si el robot se pone a tirar mucho viaje, se queda sin energía para el bus.

### 🛠️ Los Personajes del Barrio
1. El Molde (Robot)
Es la base de todo. Todos los robots traen su nombre, su batería para estar activos y su escudo para que no los quiebren tan rápido.

2. El que Reparte (RobotAtaque)
Este es el que no se queda con nada.

- Ataque: Le mete un viaje al objetivo de una.

- Gasto: Tirar mano no es gratis, se le bajan 10 puntos de energía por cada golpe.

3. El que se Cubre (RobotDefensa)
Este es más calmado, pero no se deja montar.

- Recarga: Se pone las pilas, sube el escudo 30 puntos y queda listo para otra ronda de visaje.

### 🎮 Cómo se arma el mierdero
Pa' poner a pelear a esos locos, solo tenés que darle "Run" al script. Mirá cómo es la jugada:

 ```Python 
# Creamos al mero mero y al que va a cobrar
elbergon = RobotAtaque("Elbergon", 100, 50)
victima = RobotDefensa("El-Zanahoria", 80, 20)

# ¡Se prendió el visaje!
elbergon.atacar(victima)
📺 Lo que sale en la pantalla:
Plaintext
--- SE ARMÓ EL VISAJE ---
[Elbergon] -> Energía: 100% | Chaleco: 50
[El-Zanahoria] -> Energía: 80% | Chaleco: 20
------------------------------
🔥 ¡Elbergon le metió un viaje a El-Zanahoria! Lo dejó viendo chispas.

¿Cómo quedó la vuelta?
[Elbergon] -> Energía: 90% | Chaleco: 50
[El-Zanahoria] -> Energía: 75% | Chaleco: 0
⚠️ Pilas con esto (Reglas de la calle)
```
- Si está apagado, paila: Un robot sin batería no sirve ni pa' tranca de puerta.

- Cero es el límite: Si le quitan el escudo, el daño que sobre va derechito a la batería. ¡No se regale!

## representacion grafica

![alt text](69b13153-a93e-48b9-bde8-2eb01e291a5a.jpg)