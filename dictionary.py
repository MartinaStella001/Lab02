class Dictionary:
    def __init__(self):
        self.dizionarioParole = {}

    def addWord(self, parolaAliena, traduzioni):
        if parolaAliena in self.dizionarioParole:
            self.dizionarioParole[parolaAliena].extend(traduzioni)
        else:
            self.dizionarioParole[parolaAliena] = traduzioni
        print(f"Dizionario aggiornato: {self.dizionarioParole}")

    def translate(self, parolaAlienaDaCercare):
        if parolaAlienaDaCercare in self.dizionarioParole:
            print(self.dizionarioParole[parolaAlienaDaCercare])

    def translateWordWildCard(self,parolaAlienaDaCercareWildCard):
        paroleTrovate = []
        for key in self.dizionarioParole:
            trovatoMatch = True
            if len(key) == len(parolaAlienaDaCercareWildCard):
                for i in range(len(parolaAlienaDaCercareWildCard)):
                    if parolaAlienaDaCercareWildCard[i] != "?" and parolaAlienaDaCercareWildCard[i] != key[i] :
                        trovatoMatch = False
                        break #interrompe ciclo su caratteri, va a parola successiva del dizionario

                if trovatoMatch:
                    paroleTrovate.append(self.dizionarioParole[key])
        for parola in paroleTrovate:
            print(parola)