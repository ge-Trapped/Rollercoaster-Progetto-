# DEFINIRE TUTTE LE CLASSI:
# Definire la classe PuntoCartesiano
class PuntoCartesiano:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})" 

p1 = PuntoCartesiano(5,9)

# Definire la classe Umano
class Umano:
    def __init__(self, nome: str, cognome: str, posizione: PuntoCartesiano, tipo: str, attrazioniDesiderate: list[str]):
        self.nome = nome
        self.cognome = cognome
        self.posizione = posizione
        self.tipo = tipo
        self.attrazioniDesiderate = attrazioniDesiderate
    
    def __str__(self):
        return f'{self.nome}, {self.cognome}, {self.posizione}, {self.tipo}, {self.attrazioniDesiderate}'


# Definire la classe Bambino (ereditaria Umano)
class Bambino(Umano):
    def __init__(self, nome: str, cognome: str, posizione: PuntoCartesiano):
        super().__init__(nome, cognome, posizione, "Bambino", ["tazze", "bruco", "covo dei pirati"])

# Definire la classe Ragazzo (ereditaria Umano)

class Ragazzo(Umano):
    def __init__(self, nome: str, cognome: str, posizione: PuntoCartesiano):
        super().__init__(nome, cognome, posizione, "Ragazzo", ["Raptor", "Blue Tornado", "Space Vertigo"])

# Definire la classe Adulto (ereditaria Umano)

class Adulto(Umano):
    def __init__(self, nome: str, cognome: str, posizione: PuntoCartesiano):
        super().__init__(nome, cognome, posizione, "Adulto", [""])

# Definire la classe Location

# Definire la classe Ristoro

# Definire la classe Attrazione