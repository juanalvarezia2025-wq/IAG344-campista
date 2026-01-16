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

texto = "Mi numero es 12345-985"
resultado = re.findall(r'\d+', texto) # busca todas las secuencias de dígitos en el texto
print(f"{texto}, Resultado {resultado}") # imprime el número encontrado con formato de cadena

# Funcion para limpiar un ID de documento
documento1 = "cc.75.108.061"
def clean_id(documento): # Función para limpiar un ID de documento, recibe un parámetro documento
    return re.sub(r'\D', '', documento) # Reemplaza todos los caracteres no numéricos con una cadena vacía, sub es una función de re que realiza esta operación
print(clean_id(documento1))

# Funcion para limpiar un ID de documento
documento2 = "75,108,061"
def clean_id(documento): # Función para limpiar un ID de documento, recibe un parámetro documento
    return re.sub(r'\D', '.', documento) # Reemplaza todos los caracteres no numéricos con una cadena vacía, sub es una función de re que realiza esta operación
print(clean_id(documento2))