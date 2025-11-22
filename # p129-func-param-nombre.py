# p129-func-param-nombre

def saluda(apaterno: str, amaterno: str, nombre: str, edad: int) -> None:
    print(f"Hola {nombre} {apaterno} {amaterno}, tienes {edad} años de edad.")
    print()

saluda("Castañeda", "Ramírez", "Carlos Héctor", "25")
saluda(edad=34, nombre= "Rocio", amaterno= "Bernal", apaterno= "Soto")
saluda(nombre= "Juan", apaterno= "Díaz", edad= 18, amaterno= "López")