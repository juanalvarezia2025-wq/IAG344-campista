
# ============================= 
#  🤖 TEST PARA QUITAR CARACTERES DIFERENTES A NUMEROS
# ============================= 
from proccesor import clear_id # Importa la función clear_id desde el módulo proccesor
def test_clear_id():
    assert clear_id("cc-75.108.061") == "75108061" # Prueba que clear_id limpie correctamente el ID con puntos y letras

# ============================= 
#  🤖 TEST PARA UNIR PRIMER NOMBRE Y SEGUNDO NOMBRE
# ============================= 

from proccesor import merge_name # Importa la función merge_name desde el módulo proccesor
def test_merge_name():
    assert merge_name("juan", "perez") == "juan perez" # Prueba que merge_name une correctamente el nombre y el apellido