# p014-funciones-trigonometricas
# Demostrar el uso de funciones trigonométricas básicas

import math as mt

angulo = 45
radianes = mt.radians(angulo)

#CALCULAR LAS FUNCIONES TRIGONOMETRICAS

seno = mt.sin(radianes)
coseno = mt.cos(radianes)
tangente = mt.tan(radianes)

grados = mt.degrees(radianes)

# FORMATEAR SALIDA CON F-STRING PREVIO A LA IMPRESION

salida = ("Resumen de funciones\n"
f"El seno es: {seno:.4f} \n"
f"El coseno es: {coseno:.4f} \n"
f"La tangente es: {tangente:.4f} \n"
f"El angulo {angulo} grados, equivale a {radianes:.4f} radianes\n"
f"Los {radianes:.4f} radianes, equivalen a {grados:.4f} grados\n"
)

#MOSTRAR SALIDA FORMATEADA
print(salida)