from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.dizionarioParole = Dictionary()

    def printMenu(self):

        funzionalita = ["Aggiungi nuova parola","Cerca una traduzione","Cerca con wildcard","Exit"]
        i = 1
        for funz in funzionalita:
            print(str(i) + ". " + funz)
            i = i + 1

        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary

        with open(dict, "r") as file:
            for line in file:
                parti = line.split()
                parolaAliena = parti[0].strip()
                traduzione = parti[1].strip()
                self.dizionarioParole.addWord(parolaAliena,[traduzione])


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parti = entry.split()
        parolaAliena = parti[0]
        traduzioni = []
        for p in parti[1:]:
            traduzioni.append(p.strip())

        self.dizionarioParole.addWord(parolaAliena,traduzioni)



    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        parolaAlienaDaCercare = query.strip()
        self.dizionarioParole.translate(parolaAlienaDaCercare)


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        parolaAlienaDaCercare = query.strip()
        self.dizionarioParole.translateWordWildCard(parolaAlienaDaCercare)

