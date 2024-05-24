"""
Una compañía Aérea se dedica al negocio de transporte de cargas aéreas entre diferentes orígenes y destinos.

La compañía solo puede transportar paquetes de Clientes.

Por cada paquete transportado la compañía aérea cobra 10$

Debe existir un método que genere un reporte con el total de paquetes transportados y el total recaudado para un día determinado.
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Client:
    name:str

@dataclass
class Location:
    name: str
    geo_coordinates: str

class Company:
    def __init__(self, name):
        self.name = name
        self.deliveries = []
        self.clients = []
        self.transactions_log = {}

    def deliver_package(self, client, source, destination, description):
        self.clients.append(client)
        new_delivery = Delivery(source, destination, description, self, client)
        self.deliveries.append(new_delivery)
        
        if new_delivery.creation_date_string in self.transactions_log.keys():
            self.transactions_log[new_delivery.creation_date_string] += new_delivery.fee
        else:
            self.transactions_log[new_delivery.creation_date_string] = new_delivery.fee

    def transaction_report_by_date(self):
        print(self.transactions_log)
        return self.transactions_log

@dataclass
class Delivery:
    source: Location
    destination: Location
    description: str
    company: Company
    client: Client
    fee: int = 10
    creation_date: datetime = datetime.today()
    creation_date_string: str = creation_date.strftime('%Y-%m-%d')


farmacia = Client("farmacia Lider")
AA = Company("aerolineas argentinas")

AA.deliver_package(farmacia, "cordoba", "baires", "sertales")
AA.deliver_package(farmacia, "cordoba", "baires", "actron")
AA.deliver_package(farmacia, "cordoba", "corrientes", "actron")
AA.transaction_report_by_date()


