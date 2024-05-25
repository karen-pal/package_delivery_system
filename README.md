# Description
Code to implement the system described as follows:


> Una compañía Aérea se dedica al negocio de transporte de cargas aéreas entre diferentes orígenes y destinos.
> 
> La compañía solo puede transportar paquetes de Clientes.
> 
> Por cada paquete transportado la compañía aérea cobra 10$
> 
> Debe existir un método que genere un reporte con el total de paquetes transportados y el total recaudado para un día determinado.


Using python and pytest.

<img src="diag.png">

# Dependencies
`pip install pytest`


## Run tests

`pytest test_main.py`

or, to see logs in terminal:

`pytest test_main.py --capture=no`

> In both cases the report created can be seen in reports subfolder
