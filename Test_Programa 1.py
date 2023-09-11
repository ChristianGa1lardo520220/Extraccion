"""
Gallardo del Rosario Christian Pablo
Grupo 951
19 de Agosto de 2023
"""

from Funciones_Programa_1 import Duplicados, Busqueda_Suma, encripta, desencripta


def test_duplicados():
    assert Duplicados([1, 2, 3, 4, 5, 6, 1, 2, 2, 2, 2]) == True
    assert Duplicados([1, 2, 3, 4, 5, 6, 7, 8, 9]) == False

def test_busqueda():
    assert Busqueda_Suma([2, 7, 11, 15], 9) == (0,1)

def test_encripta():
    assert encripta("cafe", 'ixmrklstnuzbowfaqejdcpvhyg') == "milk"
    assert encripta('dame 1 chocolate', 'ixmrklstnuzbowfaqejdcpvhyg') == 'riok 1 mtfmfbidk'

def test_desencriptar():
    assert desencripta("milk", 'ixmrklstnuzbowfaqejdcpvhyg') == "cafe"
    assert desencripta("riok 1 mtfmfbidk", 'ixmrklstnuzbowfaqejdcpvhyg') == "dame 1 chocolate"

