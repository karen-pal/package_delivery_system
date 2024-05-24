from datetime import datetime
from main import Client, Company

def test_deliver_package():
    farmacia = Client("farmacia Lider")
    AA = Company("aerolineas argentinas")

    AA.deliver_package(farmacia, "cordoba", "baires", "sertal")
    assert len(AA.deliveries) == 1
    assert len(AA.clients) == 1
    assert AA.transactions_log == {'{}'.format(datetime.today().strftime('%Y-%m-%d')): 10}

    AA.deliver_package(farmacia, "cordoba", "baires", "actron")
    assert len(AA.deliveries) == 2
    assert AA.transactions_log == {'{}'.format(datetime.today().strftime('%Y-%m-%d')): 20}

def test_transaction_report_by_date():
    farmacia = Client("farmacia Lider")
    AA = Company("aerolineas argentinas")

    AA.deliver_package(farmacia, "cordoba", "baires", "sertales")
    AA.deliver_package(farmacia, "cordoba", "baires", "actron")

    report = AA.transaction_report_by_date()
    assert isinstance(report, dict)
    assert len(report) == 1
    assert '{}'.format(datetime.today().strftime('%Y-%m-%d')) in report
    assert report['{}'.format(datetime.today().strftime('%Y-%m-%d'))] == 20
