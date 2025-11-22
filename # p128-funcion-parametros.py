# p128-funcion-parametros
# Función con multiples parametros
# Al llamarla debo hacerlo con el mismo número de parametros y en el mismo orden

def saluda2(apaterno: str, nombre: str) -> None:
    print(f"Hola {nombre}, {apaterno}")
    print()


saluda2("Pérez", "Juan")
#saluda2("Castañeda")
#saluda2("Castañeda", "Ramírez", "Carlos")