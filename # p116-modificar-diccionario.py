# p116-modificar-diccionario

# Crea un diccionario llamado paises con los siguientes pares (llave: valor): Argentina: 100, Brasil: 200, Colombia: 300, Chile: 400, Ecuador: 500, Bolivia: 600, Jamaica: 700.
# Muestra el diccionario inicial.
# Modifica los valores de las siguientes llaves:
#  - Cambia el valor de Brasil a 250 (usando []).
#  - Cambia el valor de Chile a 450 (usando []).
#  - Cambia el valor de Bolivia a 650 (usando update()).
#  - Cambia el valor de Jamaica a 750 (usando update()).
# Finalmente muestra el diccionario modificado.

print('\033[H\033[J')
print("Modificar elementos de un diccionario\n")

paises = {
    "Argentina": 100,
    "Brasil": 200,
    "Colombia": 300,
    "Chile": 400,
    "Ecuador": 500,
    "Bolivia": 600,
    "Jamaica": 700
}

print("Diccionario inicial:")
print(paises)

paises["Brasil"] = 250
paises["Chile"] = 450
paises.update({"Bolivia": 650})
paises.update({"Jamaica": 750})

print("\nDiccionario modificado:")
print(paises)