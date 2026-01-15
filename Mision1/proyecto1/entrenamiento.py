# Libreria de expresiones regulares
import re # Importa el módulo de expresiones regulares

"""
Expresiones Regulares en Python
Las expresiones regulares son secuencias de caracteres que forman un patrón de búsqueda.
"""
# Codigo
print("Libreria importada correctamente") # Mensaje de confirmación
# Ejemplo 1
texto = "Mi numero es 12345"
resultado = re.search(r'\d+', texto) # Busca una secuencia de dígitos, la \d representa cualquier dígito y el + indica una o más ocurrencias
print(resultado.group()) # Imprime el número encontrado
texto = "Mi numero es 12345-985"
resultado = re.search(r'\d+', texto) # Busca una secuencia de dígitos, la \d representa cualquier dígito y el + indica una o más ocurrencias
print(f"{texto}, Resultado {resultado.group()}") # Imprime el número encontrado con formato de cadena 