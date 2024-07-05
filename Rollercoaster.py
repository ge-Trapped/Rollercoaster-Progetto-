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
    
    def __repr__(self) -> str:
        return f'{self.nome}, {self.cognome}, {self.posizione}, {self.tipo}, {self.attrazioniDesiderate}'

# Definire la classe Bambino (ereditaria Umano)
class Bambino(Umano):
    def __init__(self, nome: str, cognome: str, posizione: PuntoCartesiano):
        attrazioni = ["Tazze", "Bruco", "Covo dei pirati"]
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
        self.clientiServiti = []
        self.clientiInAttesa = []

    def __str__(self):
        return f"{self.nome = }, self.posizione = {self.posizione},  {self.capienzaMassima = }, {self.capienzaAttuale = }, {self.perBambini = }, {self.tempoAttesa = }"
    
    def accettaUmano(self, u):
        if self.capienzaAttuale > 0:
            self.clientiServiti.append(u)
            self.capienzaAttuale -= 1
        else:
            self.clientiInAttesa.append(u)
        




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


# CREAZIONE DELLE CODE

pTazze = PuntoCartesiano(1, 1)
pBruco = PuntoCartesiano(2, 2)
pCovo = PuntoCartesiano(3, 3)
pRaptor = PuntoCartesiano(4, 4)
pTornado = PuntoCartesiano(5, 5)
pVertigo = PuntoCartesiano(6, 6)

totaleAttrazioni = {
    'Tazze': Attrazione("Tazze", pTazze, 10, 10, True, 5),
    'Bruco': Attrazione("Bruco", pBruco, 10, 10, True, 5),
    'Covo dei pirati': Attrazione("Covo dei pirati", pCovo, 10, 10, True, 5),
    'Raptor': Attrazione("Raptor", pRaptor, 10, 10, False, 5),
    'Blue Tornado': Attrazione("Blue Tornado", pTornado, 10, 10, False, 5), 
    'Space Vertigo': Attrazione("Space Vertigo", pVertigo, 10, 10, False, 5)
}

clientiServiti = []
clientiInAttesa = []

# print(clientiInAttesa)

listaBambini = [Bambino('Sergio', 'Rossi', p1) for x in range(100)]
listaRagazzi = [Ragazzo('Luca', 'Neri', p1) for x in range(100)]

clientiInSospeso = listaBambini.copy()
clientiInSospeso.extend(listaRagazzi)

maxRep = 10

for i in range(maxRep):
    for umano in clientiInSospeso:
        totaleAttrazioni[umano.attrazioniDesiderate[0]].accettaUmano(umano)
        umano.attrazioniDesiderate.pop(0)
        clientiInSospeso.remove(umano)
    for attrazione in totaleAttrazioni.values():
        if attrazione.capienzaAttuale == 0:
            attrazione.tempoAttesa = 5 
            while attrazione.tempoAttesa != 0:
                attrazione.tempoAttesa -= 1
                print(f"{attrazione.tempoAttesa = } minuti")
            attrazione.capienzaAttuale = attrazione.capienzaMassima
            



# Capire se l'attesa per l'attarzione è finita (se tempo attesa = 0), allora attrazine finita, dunque si svuota (capire come svuotare) Da clienti serviti a clienti in sospeso. 



# Riempirla di nuova: da clienti in attesa a clienti serviti. Tempo di attesa = 0, quindi resettare tempo di attesa (non è detto che possa ripartire, poiché potrebbero eseserci non abbastanza clienti in attesa
# richiede di settare una condizione per verificare se l'attrazione sia piena o meno: se piena riparte (tempo di attesa settato a 5); altrimenti sta lì ad aspettare, dunque aspettare i prossimi.


# Simula con un ciclo for le due code di ciascuna Attrazione, stampando a video per ogni iterazione il seguente messaggio:
#for attrazione in totaleAttrazioni:
    
 

# <Attrazione> ---> <Clienti Serviti>: <lunghezza della coda clientiServiti> | <Clienti in Attesa> : <lunghezza della coda clientiInAttesa>
# for umano in attrazione:
# listaClientiServiti.append(umano)
# capienzaAttuale -= 1
# if capienzaAttuale == 0 --> listaClientiInAttesa.append(umano)
# if capienzaAttuale == 0 --> "parte" il giro, tempoAttesa = 5
# while tempoAttesa != 0:
# for giro in range(5):
# tempoAttesa -= 1
# print(f"Giro {i+1} --- {tempoAttesa = } minuti)
# alla fine del ciclo while, capienzaAttuale = capienzaMassima_Attrazione

# Creo codaClientiInSospeso