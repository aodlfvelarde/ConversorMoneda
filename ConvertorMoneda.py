# Conversor de moneda simple en Python
# Autor: (Tu nombre)
# Descripción: Conversión entre USD, EUR, PYG y ARS usando tasas fijas

def mostrar_menu():
    print("\n=== Conversor de Moneda ===")
    print("1. USD → PYG")
    print("2. PYG → USD")
    print("3. EUR → PYG")
    print("4. PYG → EUR")
    print("5. ARS → PYG")
    print("6. PYG → ARS")
    print("0. Salir")

def convertir(monto, tasa):
    return monto * tasa

def main():
    # Tasas de ejemplo (podés actualizarlas cuando quieras)
    USD_A_PYG = 7700
    EUR_A_PYG = 8500
    ARS_A_PYG = 9

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == "0":
            print("Saliendo del programa...")
            break

        monto = float(input("Ingresa el monto a convertir: "))

        if opcion == "1":
            print(f"{monto} USD = {convertir(monto, USD_A_PYG)} PYG")
        elif opcion == "2":
            print(f"{monto} PYG = {convertir(monto, 1/USD_A_PYG):.4f} USD")
        elif opcion == "3":
            print(f"{monto} EUR = {convertir(monto, EUR_A_PYG)} PYG")
        elif opcion == "4":
            print(f"{monto} PYG = {convertir(monto, 1/EUR_A_PYG):.4f} EUR")
        elif opcion == "5":
            print(f"{monto} ARS = {convertir(monto, ARS_A_PYG)} PYG")
        elif opcion == "6":
            print(f"{monto} PYG = {convertir(monto, 1/ARS_A_PYG):.4f} ARS")
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
