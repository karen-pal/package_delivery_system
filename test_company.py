from datetime import datetime
from main import Client, Company

def test_deliver_package():
    # Create a test Client and Company
    farmacia = Client("farmacia Lider")
    AA = Company("aerolineas argentinas")

    # Deliver a package from A to B
    AA.deliver_package(farmacia, "cordoba", "baires", "sertal")
    assert len(AA.deliveries) == 1
    assert len(AA.clients) == 1
    assert AA.deliveries_log == {'{}'.format(datetime.today().strftime('%Y-%m-%d')): 10}

    # Deliver another package from A to B
    AA.deliver_package(farmacia, "cordoba", "baires", "actron")
    assert len(AA.deliveries) == 2
    assert AA.deliveries_log == {'{}'.format(datetime.today().strftime('%Y-%m-%d')): 20}

def test_transaction_report_by_date():
    # Create a test Client and Company
    farmacia = Client("farmacia Lider")
    AA = Company("aerolineas argentinas")

    # Deliver two packages
    AA.deliver_package(farmacia, "cordoba", "baires", "sertales")
    AA.deliver_package(farmacia, "cordoba", "baires", "actron")

    report = AA.transaction_report_by_date(date='2024-05-24')
    assert isinstance(report, dict)
    assert len(report) == 1
    assert '{}'.format(datetime.today().strftime('%Y-%m-%d')) in report
    assert report['{}'.format(datetime.today().strftime('%Y-%m-%d'))] == 20

def test_transaction_report_by_date_no_deliveries():
    # Date with no deliveries

    # Create a test Client and Company
    farmacia = Client("farmacia Lider")
    AA = Company("aerolineas argentinas")

    # Deliver two packages
    AA.deliver_package(farmacia, "cordoba", "baires", "sertales")
    AA.deliver_package(farmacia, "cordoba", "baires", "actron")

    report = AA.transaction_report_by_date(date='2024-05-24')
    report = AA.transaction_report_by_date(date='2023-05-24')
    assert report == ""

def test_transaction_report_by_invalid_dates():
    # Invalid date format

    # Create a test Client and Company
    farmacia = Client("farmacia Lider")
    AA = Company("aerolineas argentinas")

    # Deliver two packages
    AA.deliver_package(farmacia, "cordoba", "baires", "sertales")
    AA.deliver_package(farmacia, "cordoba", "baires", "actron")

    report = AA.transaction_report_by_date(date='2023/05/24')
    assert report == ""
