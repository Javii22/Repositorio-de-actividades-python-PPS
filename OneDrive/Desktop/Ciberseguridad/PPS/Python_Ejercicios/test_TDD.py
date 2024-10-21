from tdd import*
import pytest


def test_calculo_importe():
    importe = 2.95
    cantidad = 0.5

    assert importe_fruta(importe, cantidad)== importe*cantidad
