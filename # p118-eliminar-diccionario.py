# p118-eliminar-diccionario

# Crea un diccionario municipios con los datos: Apozol: 1863, Calera: 1868, Fresnillo: 1554, Guadalupe: 1821, Jalpa: 1824, Jerez: 1824, Loreto: 1931, Mazapil: 1824, Momax: 1857.
# Muestra el diccionario inicial.
# Realiza las siguientes eliminaciones mostrando el resultado después de cada una:
#   - Elimina Apozol (usando del)
#   - Elimina Fresnillo (usando pop())
#   - Elimina el último elemento insertado (usando popitem())
# Vacía el diccionario (usando clear()).
# Finalmente muestra el diccionario vacío.

print('\033[H\033[J')
print("Eliminar elementos de un diccionario\n")

municipios = {
    'Apozol': 1863,
    'Calera': 1868,
    'Fresnillo': 1554,
    'Guadalupe': 1821,
    'Jalpa': 1824,
    'Jerez': 1824,
    'Loreto': 1931,
    'Mazapil': 1824,
    'Momax': 1857
}

print("Diccionario inicial:")
print(municipios)

del municipios['Apozol']
print("\nDespués de 'del Apozol':")
print(municipios)

municipios.pop('Fresnillo')
print("\nDespués de 'pop(Fresnillo)':")
print(municipios)

municipios.popitem()
print("\nDespués de 'popitem()' (eliminando último elemento):")
print(municipios)

municipios.clear()
print("\nDespués de 'clear()':")
print(municipios)