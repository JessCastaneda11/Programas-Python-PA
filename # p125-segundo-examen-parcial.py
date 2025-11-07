# p125-segundo-examen-parcial

# ------------------------------------------------------------
# TecnoTienda - Sistema de Inventario
# Capturar los productos y generar:
# 1) Lista cruda (diccionarios)
# 2) Tabla formateada
# 3) Resumen (totales, promedios, conteos, más caro y más barato)
# ------------------------------------------------------------

print("\033[H\033[J")
print("TecnoTienda - Sistema de Inventario\n")

productos = [] 

print("Captura de datos de los productos (* para terminar):\n")
while True:
    nombre = input("Nombre del producto: ").strip()
    if nombre == "" or nombre == "*":
        break

    precio = float(input("Precio: "))
    categoria = input("Categoría: ").strip()
    proveedor = input("Proveedor: ").strip()
    stock = int(input("Stock: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria,
        "proveedor": proveedor,
        "stock": stock
    }

    productos.append(producto)
    print()

if len(productos) == 0:
    print("\nNo se registraron productos. Proceso Terminado.")

else:
    print("\n3.1. DATOS (LISTA DE DICCIONARIOS):")
    print(productos)

    print("\n3.2. TABLA DE DATOS:")
   
    cab1, cab2, cab3, cab4, cab5 = "Nombre", "Precio", "Categoría", "Stock", "Proveedor"

    w1, w2, w3, w4, w5 = 20, 10, 14, 7, 12
    print(f"{cab1:<{w1}} {cab2:>{w2}} {cab3:>{w3}} {cab4:>{w4}} {cab5:>{w5}}")

    for p in productos:
        precio_txt = f"{p['precio']:,.2f}"
        print(f"{p['nombre']:<{w1}} {precio_txt:>{w2}} {p['categoria']:>{w3}} {p['stock']:>{w4}} {p['proveedor']:>{w5}}")

    print("\n3.3. RESUMEN:")

    total_prod = len(productos)
    print(f"Productos totales: {total_prod}")

    categorias = {}
    for p in productos:
        cat = p["categoria"]
        if cat not in categorias:
            categorias[cat] = 0
        categorias[cat] += 1

    print("\nCategorías:")
    for cat, cnt in categorias.items():
        print(f"• {cat}: {cnt}")

    proveedores = {}
    for p in productos:
        prov = p["proveedor"]
        if prov not in proveedores:
            proveedores[prov] = 0
        proveedores[prov] += 1

    print("\nProveedores:")
    for prov, cnt in proveedores.items():
        print(f"• {prov}: {cnt}")

    suma_stock = 0
    for p in productos:
        suma_stock += p["stock"]
    prom_stock = suma_stock / total_prod

    print(f"\nStock -> Suma: {suma_stock:,}, Promedio: {prom_stock:.1f}")

    suma_precios = 0.0
    for p in productos:
        suma_precios += p["precio"]
    prom_precios = suma_precios / total_prod

    print(f"\nPrecio -> Suma: {suma_precios:,.2f}, Promedio: {prom_precios:,.2f}")

    mas_caro = productos[0]
    mas_barato = productos[0]
    i = 1

    while i < len(productos):
        if productos[i]["precio"] > mas_caro["precio"]:
            mas_caro = productos[i]
        if productos[i]["precio"] < mas_barato["precio"]:
            mas_barato = productos[i]
        i += 1

    print(f"\n{mas_caro['nombre']} de {mas_caro['precio']:,.2f} es el más caro, "
          f"{mas_barato['nombre']} de {mas_barato['precio']:,.2f} es el más barato.")

    print("\nProceso Terminado.")