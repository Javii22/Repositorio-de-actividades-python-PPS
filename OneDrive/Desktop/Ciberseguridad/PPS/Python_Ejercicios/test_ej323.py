import ej3_2_3 as e

def test_precio_fruta():
    fruta_prueba = "Manzana"
    precio: float = e.precios["Manzana"]
    cantidad: float = 5.5


    assert e.precio_total(cantidad, fruta_prueba) == precio*cantidad

    assert e.precio_total(cantidad, fruta_prueba.lower()) == precio*cantidad

    assert e.precio_total(cantidad, fruta_prueba.upper()) == precio*cantidad
    