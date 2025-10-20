# p091-iterar-lista

# Mostrar las diferentes formas de iterar (pasar) por cada elemento de una lista

print('\033[2J\033[H')
print("Iterar por los elementos de una lista")

nums = [2, 4, 6, 8, 10, 12, 14, 16]

print(f"Todos los números: {nums} - {len(nums)}")

print("\n\n1. Iteración por elemento: ")
for n in nums:
    print(n, end=' ')

print("\n\n2. Iteración por el índice de cada elemento: ")
for i in range(len(nums)):
    print(nums[i], end=' ')

print("\n\n3. Iteración por cada elemento y sumar 2: ")
for n in nums:
    print(n + 2, end=' ')

print("\n\n4. Iteración por índice y sumar 10: ")
for i in range(len(nums)):
    print(nums[i] + 10, end=' ')


print("\n\n5. Iteración con enumerate: ")
print("Pos\tValor")
for i, n in enumerate(nums):
    print(i,'\t', n,)

print(f"\nResultado: {nums} - {len(nums)}")    

print("\n\n6. Modificar la lista al iterar: ")
for i in range(len(nums)):
    nums[i] = nums[i] ** 2

print(f"\nResultado: {nums} - {len(nums)}")     