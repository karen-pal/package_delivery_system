from datetime import datetime
from main import Client, DeliveryCompany, Location

def test_deliver_package():
    # Create a test Client and Company
    farmacia = Client("farmacia Lider")
    AA = DeliveryCompany("aerolineas argentinas")
    cordoba = Location(name="Cordoba, ARG", lat=-31.4201, long=-64.1888)
    baires = Location(name="Buenos Aires, ARG", lat=-34.6037, long=-58.3816)

    # Deliver a package from A to B
    delivery_a = AA.deliver_package(farmacia, cordoba, baires, "sertal")
    assert len(AA.deliveries) == 1
    assert len(AA.clients) == 1
    assert AA.deliveries_log[datetime.today().strftime('%Y-%m-%d')]["total_revenue"] == 10
    assert AA.deliveries_log[datetime.today().strftime('%Y-%m-%d')]["deliveries"] == [delivery_a]

    # Deliver another package from A to B
    delivery_b = AA.deliver_package(farmacia, cordoba, baires, "actron")
    assert len(AA.deliveries) == 2
    assert AA.deliveries_log[datetime.today().strftime('%Y-%m-%d')]["total_revenue"] == 20
    assert AA.deliveries_log[datetime.today().strftime('%Y-%m-%d')]["deliveries"] == [delivery_a, delivery_b]

def test_transaction_report_by_date():
    # Create a test Client and Company
    farmacia = Client("farmacia Lider")
    AA = DeliveryCompany("aerolineas argentinas")

    cordoba = Location(name="Cordoba, ARG", lat=-31.4201, long=-64.1888)
    baires = Location(name="Buenos Aires, ARG", lat=-34.6037, long=-58.3816)
    # Deliver two packages
    AA.deliver_package(farmacia, cordoba, baires, "sertales")
    AA.deliver_package(farmacia, cordoba, baires, "actron")

    report = AA.report_by_date(date= datetime.today().strftime('%Y-%m-%d'))
    assert isinstance(report, dict)
    assert len(report) == 1
    assert '{}'.format(datetime.today().strftime('%Y-%m-%d')) in report
    assert report['{}'.format(datetime.today().strftime('%Y-%m-%d'))]["total_revenue"] == 20

def test_transaction_report_by_date_no_deliveries():

    # Create a test Client and Company
    farmacia = Client("farmacia Lider")
    AA = DeliveryCompany("aerolineas argentinas")

    cordoba = Location(name="Cordoba, ARG", lat=-31.4201, long=-64.1888)
    baires = Location(name="Buenos Aires, ARG", lat=-34.6037, long=-58.3816)
    # Deliver two packages
    AA.deliver_package(farmacia, cordoba, baires, "sertales")
    AA.deliver_package(farmacia, cordoba, baires, "actron")

    # Date with no deliveries
    report = AA.report_by_date(date='2023-05-24')
    assert report == ""

def test_transaction_report_by_invalid_date_format():
    # Create a test Client and Company
    farmacia = Client("farmacia Lider")
    AA = DeliveryCompany("aerolineas argentinas")

    cordoba = Location(name="Cordoba, ARG", lat=-31.4201, long=-64.1888)
    baires = Location(name="Buenos Aires, ARG", lat=-34.6037, long=-58.3816)
    # Deliver two packages
    AA.deliver_package(farmacia, cordoba, baires, "sertales")
    AA.deliver_package(farmacia, cordoba, baires, "actron")

    # Invalid date format
    report = AA.report_by_date(date='2023/05/24')
    assert report == ""
