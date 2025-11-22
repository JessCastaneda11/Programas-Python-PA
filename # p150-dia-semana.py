# p150-dia-semana

# Programa que recibe un numero del 1 al 7 y devuelve el dia de la semana

def dia_semana(num: int) -> str:
    if num == 1:
        return "Lunes"
    elif num == 2:
        return "Martes"
    elif num == 3:
        return "Miércoles"
    elif num == 4:
        return "Jueves"
    elif num == 5:
        return "Viernes"
    elif num == 6:
        return "Sábado"
    elif num == 7:
        return "Domingo"
    else:
        return ""   # señal de error


def main() -> None:
    print('\033[H\033[J')
    num = int(input("Introduce un número del 1 al 7: "))
    dia = dia_semana(num)

    if dia == "":
        print("Error: El número debe estar entre 1 y 7.")
    else:
        print(f"El día es: {dia}")


if __name__ == "__main__":
    main()