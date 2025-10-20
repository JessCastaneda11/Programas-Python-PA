# p090-eliminar-lista

# Mostrar las diferentes formas de eliminar elementos de una lista

print('\033[2J\033[H')
print("Eliminar elementos de una lista")

nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]
print(f"\nDatos originales con anomalías: {nums} - {len(nums)}")

print("\nEliminar el valor 99: ")
nums.remove(99)
print(f"Resultado : {nums} - {len(nums)}")

print("\nEliminar el elemento en la posición 8: ")
num_removido = nums.pop(8)
print(f"Resultado : {nums} - {len(nums)} - Se removió {num_removido}")

print("\nEliminar el último elemento: ")
num_removido = nums.pop()
print(f"Resultado : {nums} - {len(nums)} - Se removió {num_removido}")


print("\nEliminar todas las mediciones: ")
nums.clear()
print(f"Resultado : {nums} - {len(nums)}")