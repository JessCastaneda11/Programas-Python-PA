"""
Objetivo: [Un cine local necesita un programa para administrar la venta de boletos para una función especial en una de sus salas. El programa debe controlar la venta de boletos, gestionar el aforo y calcular los ingresos generados.Diseña un programa en Python, aplicando los conocimientos aprendidos en clase.]
Nombre del Alumno: [Jessica Esmeralda Castañeda Pérez]
Matrícula: [42405208]
Materia: Computación Aplicada
Examen: Primer Parcial
"""

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos

# --- Contadores de Asistentes ---
total_estudiantes = 0
total_adultos = 0
total_tercera_edad = 0
total_academicos = 0

# ... (agrega los demás contadores de tipo_comprador de comprador y de sexo)
total_asistentes = 0
total_rechazados = 0
suma_edades = 0
total_mujeres = 0
total_hombres = 0

# --- Acumuladores de Ingresos ---
ingresos_estudiantes = 0.0
# ... (agrega los demás acumuladores de ingresos)
ingresos_totales = 0.0
ingresos_adultos = 0.0
ingresos_tercera_edad = 0.0
ingresos_academicos = 0.0

# --- Precios de los Boletos (constantes) ---
PRECIO_ESTUDIANTE = 50.0
PRECIO_ADULTO = 90.0

# ... (agrega las demás constantes de precios)
PRECIO_TERCERA_EDAD = 60.0
PRECIO_ACADEMICO = 70.0

print('\033[2J\033[H')
print("--- Sistema de Venta de Boletos de Cine ---")

# --- Ciclo Principal para la Venta de Boletos ---
# Usaremos un ciclo while para registrar ventas hasta que el usuario decida parar.
continuar_venta = "s"
while continuar_venta == "s":

    print("\n--- Nueva Venta ---")
    # --- 1. Solicitud de Datos ---
    # Pide la edad, el tipo_comprador de comprador y el sexo.
    # ¡Recuerda convertir la edad a un número entero!

    edad = int(input("Introduce la edad del comprador: "))

    # ... (pide el tipo_comprador de comprador y el sexo)

    if edad > 13:
    
        tipo_comprador = input("Tipo de comprador (estudiante/adulto/tercera_edad/academico): ").lower()
        sexo = input("Sexo (hombre/mujer): ").lower()


    # --- 2. Validación de Edad (Clasificación B) ---
    # La película es para mayores de 13 años.
    
    
        # Si la edad es permitida, procede con la venta.
        # Muestra el mensaje de bienvenida con los datos registrados
        print(f"¡Bienvenido(a)! Venta registrada: Edad: {edad}, Sexo: {sexo}, Tipo: {tipo_comprador}")
        
        # --- 3. Actualización de Estadísticas Generales ---
        # Incrementa el contador de asistentes y suma la edad para el promedio.
        # Incrementa el contador de sexo correspondiente (hombre o mujer).

        total_asistentes += 1
        suma_edades += edad
        if sexo == 'hombre':
            total_hombres += 1
        elif sexo == 'mujer':
            total_mujeres += 1

        # --- 4. Cálculo de Costo y Actualización de Contadores Específicos ---
        # Usa una estructura if/elif/else para determinar el precio y actualizar
        # los contadores del tipo de comprador y sus ingresos.
        # Suma el costo del boleto a los ingresos totales.

        costo = 0.0
        if tipo_comprador == 'estudiante':
            total_estudiantes += 1
            costo = PRECIO_ESTUDIANTE
            ingresos_estudiantes += costo

        elif tipo_comprador == 'adulto':
            total_adultos += 1
            costo = PRECIO_ADULTO
            ingresos_adultos += costo

        elif tipo_comprador == 'tercera_edad':
            total_tercera_edad += 1
            costo = PRECIO_TERCERA_EDAD
            ingresos_tercera_edad += costo

        elif tipo_comprador == 'academico':
            total_academicos += 1
            costo = PRECIO_ACADEMICO
            ingresos_academicos += costo
            
        else:
            print("Tipo de comprador no válido. Venta anulada.")
            costo = 0.0

        ingresos_totales += costo


    else:
        # Si la edad no es permitida, muestra un mensaje y actualiza el contador ()
        print("ACCESO DENEGADO: El comprador es menor de 13 años.")

        # ... (incrementa el contador de personas rechazadas)

        total_rechazados += 1

    # Pregunta al usuario si desea registrar otra venta.
    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()

# --- FIN DEL CICLO ---

# --- 5. Cálculo de Promedio ---
# Calcula el promedio de edad. Cuidado con la división entre cero si no hubo asistentes.
promedio_edad = 0
# if total_asistentes > 0:
#     promedio_edad = ... # (calcula el promedio aquí)

if total_asistentes > 0:

    promedio_edad = suma_edades / total_asistentes


# --- 6. Impresión del Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")

print("\n--- Estadísticas del Público ---")
# Imprime todos los totales de asistentes por tipo_comprador y sexo.
print(f"Estudiantes: {total_estudiantes}")
print(f"Adultos: {total_adultos}")
print(f"Tercera Edad: {total_tercera_edad}")
print(f"Académicos: {total_academicos}")
print("-"*30)
print(f"Hombres: {total_hombres}")
print(f"Mujeres: {total_mujeres}")
print("-"*30)

print(f"Total de Asistentes: {total_asistentes}")
print(f"Promedio de edad de asistentes: {promedio_edad:.2f} años")
print(f"Personas rechazadas por edad: {total_rechazados}") 

print("\n--- Reporte de Ingresos ---")
# Imprime todos los ingresos por tipo_comprador de comprador y el total general.
# Utiliza formato para mostrar dos decimales en el dinero.
print(f"Ingresos Estudiantes: ${ingresos_estudiantes:,.2f}")
print(f"Ingresos Adultos:     ${ingresos_adultos:,.2f}")
print(f"Ingresos Tercera Edad:${ingresos_tercera_edad:,.2f}")
print(f"Ingresos Académicos:  ${ingresos_academicos:,.2f}")
print("-"*30)
print(f"Total Recaudado en General: ${ingresos_totales:,.2f}")

print("\n--- Rentabilidad ---")
# --- 7. Mensaje de Rentabilidad ---
# Usa una estructura if/elif/else para determinar si las ganancias
# fueron BAJAS, MODERADAS o BUENAS, basándote en los ingresos totales.
if ingresos_totales < 1500:
    print("La función generó BAJAS ganancias.")
elif ingresos_totales <= 3500:
    print("La función generó ganancias MODERADAS.")
else:
    print("La función generó BUENAS ganancias.")

"""
Preguntas: Explica con tus palabras

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento.  ¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

[Creo que lo más fácil sería preguntar al usuario que día de la semana es o tal vez solo asegurar que el día es MARTES, y en la parte donde vaya a calcular el precio del boleto para un adulto, revisaría si es_martes == "s". En caso de que esto sea verdadero, le aplicaría el descuento al precio normal del boleto que seria multiplicar el costo por el descuento en este caso 0.8]

2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, aunque los ingresos por cada tipo_comprador de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

[Si el "total recaudado" me arrojara un valor incorrecto aunque los ingresos por cada tipo estén correctos, yo lo primero que haría sería revisar que todos los acumuladores estén en 0.0 y que no se reasignen en otra parte del programa, después comprobaría que la variable costo se reinicie en cada venta y que no arrastre valores anteriores, y que en cada tipo de comprador (estudiante, adulto, tercera edad o académico) ese costo se sume una sola vez al ingreso específico correspondiente y también una sola vez al total general. También revisaría que en el bloque de rechazados no se sumen ingresos por error. Si aún no encuentro el problema, colocaría impresiones temporales justo después de cada suma para verificar cómo va cambiando el valor de ingresos_totales y al final compararía la suma de todos los ingresos por tipo contra el total, ya que si no coinciden, sabría que en alguna parte estoy duplicando o dejando de sumar, y así podría encontrar el posible el error en el código.]

"""