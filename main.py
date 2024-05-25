from dataclasses import dataclass
from datetime import datetime
import os


@dataclass
class Location:
    name: str
    lat: float
    long: float


@dataclass
class Client:
    name: str


class DeliveryCompany:
    def __init__(self, name: str):
        self.name = name
        self.deliveries = []
        self.clients = []
        self.deliveries_log = {}

    def deliver_package(
        self, client: Client, source: Location, destination: Location, description: str
    ):
        self.clients.append(client)
        new_delivery = Delivery(
            source=source,
            destination=destination,
            description=description,
            company=self,
            client=client,
        )
        self.deliveries.append(new_delivery)

        if new_delivery.creation_date_string in self.deliveries_log.keys():
            self.deliveries_log[new_delivery.creation_date_string][
                "total_revenue"
            ] += new_delivery.fee
            self.deliveries_log[new_delivery.creation_date_string]["deliveries"].append(
                new_delivery
            )
        else:
            self.deliveries_log[new_delivery.creation_date_string] = {
                "total_revenue": new_delivery.fee,
                "deliveries": [new_delivery],
            }
        return new_delivery

    @staticmethod
    def validate_date_format(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def report_by_date(self, *, date):
        if not self.validate_date_format(date):
            print(
                "ERROR: The value given {} is not a valid date, please use the format %Y-%m-%d".format(
                    date
                )
            )
            return ""

        if date not in self.deliveries_log.keys():
            print(
                "There are no deliveries for date {} and delivery company {} ".format(
                    date, self.name
                )
            )
            return ""
        deliveries = self.deliveries_log[date]

        report = "/--- Deliveries report for date : {} ---/\n".format(date)
        report += "Total collected: {}\n".format(deliveries["total_revenue"])
        report += "Total amount of packages delivered: {}\n".format(
            len(deliveries["deliveries"])
        )
        report += "Detailed description\n"
        for delivery in deliveries["deliveries"]:
            report += str(delivery)
        report += "/---------------/\n\n"

        # display in terminal
        print(report)

        # write to disk
        directory = "./reports"
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = directory + "/" + date + ".txt"
        try:
            with open(file_path, "w") as file:
                file.write(report)
        except IOError as e:
            print(f"Failed to write report to {file_path}: {e}")

        return self.deliveries_log


class Delivery:
    def __init__(
        self,
        *,
        source: Location,
        destination: Location,
        description: str,
        company: DeliveryCompany,
        client: Client,
        fee: int = 10,
        creation_date: datetime = None,
    ):
        self.source = source
        self.destination = destination
        self.package_description = description
        self.company = company
        self.client = client
        self.fee = fee
        self.creation_date = creation_date or datetime.today()
        self.creation_date_string = self.creation_date.strftime("%Y-%m-%d")

    def __repr__(self) -> str:
        return (
            f"● Delivery with "
            f"source: {self.source}, and "
            f"destination: {self.destination}.\n\n "
            f"Provided description:'{self.package_description}'\n "
            f"Delivered by company: {self.company.name}, "
            f"For client: {self.client.name}.\n\n "
            f"Associated delivery fee={self.fee}, "
            f"creation_date={self.creation_date}, "
            f"creation_date_string='{self.creation_date_string}')"
        )
