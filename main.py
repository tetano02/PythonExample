class Persona:

    #Attributo di classe, non dell'istanza=cambia il dato, cambia per tutti
    quante=0

    #metodo definito a livello di classe=static , puoi richiamarlo solo tramite Persona.<nome metodo>()
    @staticmethod
    def stringa_classe():
        return 'Ciao sono una persona'

    def __init__(self, nome:str): #costruttore
        self.__nome=nome
        Persona.quante+=1 #Non c'è il self! viene modificato l'attributo di classe

    # senza @staticmethod sono metodi definiti a livello di oggetto
    def get_nome(self):
        return self.__nome

    def set_nome(self, nuovo_nome: str):
        self.__nome=nuovo_nome

#Alternativa più bella rispetto agli attributi di classe, una nuova classe!
class Mondo:
    def __init__(self):
        self.__popolazione=[]

    def aggiungi_persona(self,nome: str):
        self.__popolazione.append(Persona(nome))

    def quante_persone(self):
        return len(self.__popolazione)

#ste è un oggetto(o istanza) di Persona
ste=Persona('Stefano')

#Stampo il nome, che è un attributo
print(ste.get_nome())

#Utilizzo un metodo static
print(Persona.stringa_classe())

#modifico il nome
print('Che nome vuoi dare?')
name=input()
ste.set_nome(name)
print('Congratulazioni, nome cambiato!\nDavvero un bel nome '+ste.get_nome())
print('Ci sono ben '+str(Persona.quante)+' persone')


#Alternativa Mondo
terra=Mondo()
terra.aggiungi_persona(ste)
print(terra.quante_persone())
