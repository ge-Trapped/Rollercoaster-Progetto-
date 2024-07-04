import random

## DEFINIRE TUTTE LE CLASSI:

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
        attrazioni = ["tazze", "bruco", "covo dei pirati"]
        random.shuffle(attrazioni)
        super().__init__(nome, cognome, posizione, "Bambino", attrazioni)

# Definire la classe Ragazzo (ereditaria Umano)
class Ragazzo(Umano):
    def __init__(self, nome: str, cognome: str, posizione: PuntoCartesiano):
        attrazioni = ["Raptor", "Blue Tornado", "Space Vertigo"]
        random.shuffle(attrazioni)
        super().__init__(nome, cognome, posizione, "Ragazzo", attrazioni)

# Definire la classe Adulto (ereditaria Umano)
class Adulto(Umano):
    def __init__(self, nome: str, cognome: str, posizione: PuntoCartesiano):
        super().__init__(nome, cognome, posizione, "Adulto", [""])

# Definire la classe Location
class Location():
    def __init__(self, nome: str, posizione: PuntoCartesiano):
        self.nome = nome
        self.posizione = posizione

    def __str__(self):
        return f"{self.nome}, {self.posizione}"

# Definire la classe Ristoro
class Ristoro(Location): 
    def __init__(self, nome: str, posizione: PuntoCartesiano, capienzaMassima: int, capienzaAttuale: int):
        super().__init__(
            nome = nome, 
            posizione = posizione, 
            )
        self.capienzaMassima = capienzaMassima
        self.capienzaAttuale = capienzaAttuale

    def __str__(self):
        return f"{self.nome = }, self.posizione = {self.posizione},  {self.capienzaMassima = }, {self.capienzaAttuale = }"

# Definire la classe Attrazione
class Attrazione(Location): 
    def __init__(self, nome: str, posizione: PuntoCartesiano, capienzaMassima: int, capienzaAttuale: int, perBambini: bool, tempoAttesa: int):
        super().__init__(
            nome = nome, 
            posizione = posizione
            )
        self.capienzaAttuale = capienzaAttuale
        self.capienzaMassima = capienzaMassima
        self.tempoAttesa = tempoAttesa
        self.perBambini = perBambini

    def __str__(self):
        return f"{self.nome = }, self.posizione = {self.posizione},  {self.capienzaMassima = }, {self.capienzaAttuale = }, {self.perBambini = }, {self.tempoAttesa = }"

"""
OPZIONE 1

Creare una funzione che:

- Definire una lista con: 1 adulto, 1 bambino, 1 o + ragazzi;
- Confronti i cognomi;
- In caso di congomi uguali, aggiunga il ragazzo alla famiglia.

OPZIONE 2

Creare 4 liste con al suo interno oggetti delle classi Adulto, Ragazzo, Bambino

Definire una funzione che crea una famiglia
def creaFamiglia(cognome: str, posizione: PuntoCartesiano):
#     famiglia = [
#         Adulto("Adulto", cognome, posizione),
#         Bambino("Bambino", cognome, posizione),
#         Ragazzo("Ragazzo", cognome, posizione)
#     ]

# famiglie = [
#     creaFamiglia("Rossi", PuntoCartesiano(0, 0)),
#     creaFamiglia("Bianchi", PuntoCartesiano(0, 0)),
#     creaFamiglia("Verdi", PuntoCartesiano(0, 0)),
#     creaFamiglia("Neri", PuntoCartesiano(0, 0))
# ]
"""

# CREAZIONE DELLE FAMIGLIE MEDIANTE QUATTRI SEPARATE LISTE

famigliaRossi = [Adulto('Claudio', 'Rossi', p1), Ragazzo('Alice', 'Rossi', p1), Bambino('Sergio', 'Rossi', p1)]

famigliaVerdi = [Adulto('Klaus', 'Verdi', p1), Ragazzo('Francesco', 'Verdi', p1), Bambino('Giulia', 'Verdi', p1)]

famigliaBianchi = [Adulto('Tito', 'Bianchi', p1), Ragazzo('Paolo', 'Bianchi', p1), Bambino('Claudia', 'Bianchi', p1)]

famigliaNeri = [Adulto('Sempronia', 'Neri', p1), Ragazzo('Luca', 'Neri', p1), Bambino('Alex', 'Neri', p1)]


print(famigliaBianchi[2])
print(famigliaVerdi[2])