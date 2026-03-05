import translator as tr
import dictionary as dr

t = tr.Translator()
d = dr.Dictionary()
t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()

    txtIn = input("Scegli un'opzione: ")
    # Add input control here!

    if not txtIn.isdigit():
        print("Input non valido")
        txtIn = input("Riprova: ")
    if int(txtIn) == 1:
        parola = input("Ok, quale parola devo aggiungere? ")
        if parola.replace(" ", "").isalpha():
            #salvare parola e traduzione in  input.tolower e aggiungerle in dictionary (add Word)
            t.handleAdd(parola.lower())
        else:
            print("Input non valido")


    if int(txtIn) == 2:
        parola = input("Ok, quale parola devo cercare?")
        if parola.replace(" ", "").isalpha():
            #cercare la parola in input.toloower in dictionary e restituire traduzione (translate)
            t.handleTranslate(parola.lower())
        else:
            print("Input non valido")



    if int(txtIn) == 3:
        parola = input("Ok, quale parola devo cercare?")
        if parola.replace("?", "").isalpha():
            #cercare parola con wildcard
            if parola.count("?") == 1:
                t.handleWildCard(parola.lower())
            else:
                print("Errore: puoi usare solo un '?' per parola")

    if int(txtIn) == 4:
        print("Uscita dal programma.")
        break