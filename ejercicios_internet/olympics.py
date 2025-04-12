import random

class Participant:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Participant):
            return self.name == other.name and self.country == other.country
        return False

    def __hash__(self) -> int:
        return hash(self.name, self.country)
class Olympics:
    def __init__(self):
        self.events = []
        self.participants = {}
        self.results = {}
        self.country_results = {}
    def register_event(self):
        event = input("Introduce el nombre del evento deportivo: ").strip()

        if event in self.events:
            print("El evento ya esta registrado")
        else:
            self.events.append(event)
            print("El evento se ha registrado correctamente")
    def register_participant(self):
        if not self.events:
            print("No hay eventos para que los participantes puedan competir. Por favor introduce un evento")
            return
        name = input("Introduce el nombre del participante ").strip()
        country = input("Introduce el pais del participante ").strip()
        participant = Participant(name, country)
        print("Eventos deportivos disponibles")
        for index,event in enumerate(self.events):
            print(f"{index + 1}.{event}")
        event_choice =int(input("Selecciona el numero del evento deportivo para asignar al participante ")) - 1
        if event_choice >= 0 and event_choice < len(self.events):
            event = self.events[event_choice]
            if event in self.participants and participant in self.participants[event]:
                print(f"El participante {name} de {country} ya esta registrado en el evento deportivo {event}")
            else:
                if event not in self.participants:
                    self.participants[event] = []

                self.participants[event].append(participant)
                print(
                    f"El participante {name} de {country} se ha registrado en el evento deportivo {event}.")
        else:
            print("El evento deportivo introducido no es valido, el participante no será registrado")
    def simulate_events(self):
        if not self.events:
            print("No hay eventos registrados. Por favor registre al menos un evento deportivo.")
        for event in self.events:
            if len(self.participants.get(event, [])) < 3:
                print(f"El evento {event} no tiene suficientes participantes.")
                continue
            medalist = random.sample(self.participants[event], 3)
            random.shuffle(medalist)
            gold, silver, bronze = medalist
            self.results[event] = [gold, silver, bronze]

            self.update_country_results(gold.country, "gold")
            self.update_country_results(silver.country, "silver")
            self.update_country_results(bronze.country, "bronze")

            print(f"Resultados simulación del evento: {event}")
            print(f"Oro: {gold.name} ({gold.country})")
            print(f"Plata: {silver.name} ({silver.country})")
            print(f"Bronce: {bronze.name} ({bronze.country})")

    def update_country_results(self, country, medal):
        if country not in self.country_results:
            self.country_results[country] = {
                "gold": 0, "silver": 0, "bronze": 0}
        self.country_results[country][medal] += 1

    def show_report(self):

        print("Informe Juegos Olímpicos:")

        if self.results:

            print("Informe por evento:")

            for event, winners in self.results.items():
                print(f"Evento: {event}")
                print(f"Oro: {winners[0].name} ({winners[0].country})")
                print(f"Plata: {winners[1].name} ({winners[1].country})")
                print(f"Bronce: {winners[2].name} ({winners[2].country})")
        else:
            print("No hay resultados registrados.")

        print()

        if self.country_results:

            print("Informe por país:")

            for country, medals in sorted(self.country_results.items(), key=lambda x: (
                    x[1]["gold"], x[1]["silver"], x[1]["bronze"]), reverse=True):

                print(
                    f"{country}: Oro {medals['gold']}, Plata {medals['silver']}, Bronce {medals['bronze']}")

        else:
            print("No hay medallas por país registradas.")

olympics = Olympics()
print("Simulador juegos olimpicos")
while True:
    print()
    print("1.Registro de eventos")
    print("2.Registro de participantes")
    print("3.Simulaicon de eventos")
    print("4.Creacion de informes")
    print("5.Salir")
    
    option = input("Selecciona una accion:")
    match option:
        case "1":
            olympics.register_event()
        case "2":
            olympics.register_participant()
        case "3":
            olympics.simulate_events()
        case "4":
            olympics.show_report()
        case "5":
            print("Saliendo del simulador")
            break
    