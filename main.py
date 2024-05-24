"""
Una compañía Aérea se dedica al negocio de transporte de cargas aéreas entre diferentes orígenes y destinos.

La compañía solo puede transportar paquetes de Clientes.

Por cada paquete transportado la compañía aérea cobra 10$

Debe existir un método que genere un reporte con el total de paquetes transportados y el total recaudado para un día determinado.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Any

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
        self.deliveries_log = {}

    def deliver_package(self, client, source, destination, description):
        self.clients.append(client)
        new_delivery = Delivery(source, destination, description, self, client)
        self.deliveries.append(new_delivery)
        
        if new_delivery.creation_date_string in self.deliveries_log.keys():
            self.deliveries_log[new_delivery.creation_date_string]["total_revenue"] += new_delivery.fee
            self.deliveries_log[new_delivery.creation_date_string]["deliveries"].append(new_delivery)
        else:

            self.deliveries_log[new_delivery.creation_date_string] = {"total_revenue": new_delivery.fee, "deliveries": [new_delivery]}
        return new_delivery

    @staticmethod
    def validate_date_format(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def transaction_report_by_date(self, *, date):
        if not self.validate_date_format(date):
            print("the value given {} is not a valid date, please use the format %Y-%m-%d".format(date))
            # TODO: raise a custom exception so other devs can catch the mistake
            return ""
        if date not in self.deliveries_log.keys():
            print("There are no deliveries for date {} and company {} ".format(date,self.name))
            # TODO: Give better formatting
            return ""
        deliveries = self.deliveries_log[date]
        print("/--- Deliveries report for date : {} ---/".format(date))
        print("Total collected: {}".format(deliveries["total_revenue"]))
        print("Total amount of packages delivered: {}\n".format(len(deliveries["deliveries"])))
        print("Detailed description\n")
        for delivery in deliveries["deliveries"]:
            print(delivery)
        print("/---------------/\n\n")
        #print(self.deliveries_log[date])

        return self.deliveries_log


class Delivery:
    def __init__(self, source: str, destination: str, description: str, company: Any, client: Any, fee: int = 10, creation_date: datetime = None):
        self.source = source
        self.destination = destination
        self.description = description
        self.company = company
        self.client = client
        self.fee = fee
        self.creation_date = datetime.today()
        self.creation_date_string = self.creation_date.strftime('%Y-%m-%d')

    def __repr__(self) -> str:
        return (f"Delivery with "
                f"source: {self.source}, and "
                f"destination: {self.destination}.\n\n "
                f"Provided description:'{self.description}'\n "
                f"Delivered by company={self.company}, "
                f"For client={self.client}.\n\n "
                f"Associated delivery fee={self.fee}, "
                f"creation_date={self.creation_date}, "
                f"creation_date_string='{self.creation_date_string}')")
