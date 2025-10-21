# p098-producto-punto

# Cálculo del producto punto de dos vectores

vector_a = [1, 3, -5]
vector_b = [4, -2, -1]
producto_punto = 0

print('\033[H\033[J')
print("--- Cálculo del Producto Punto ---\n")

print(f"Vector A: {vector_a}")
print(f"Vector B: {vector_b}\n")

if len(vector_a) == len(vector_b):
    for i in range(len(vector_a)):
        producto = vector_a[i] * vector_b[i]
        producto_punto += producto

    print(f"El producto punto de los vectores es: {producto_punto}")

else:
    print("Error: Los vectores deben tener la misma longitud para calcular el producto punto.")
