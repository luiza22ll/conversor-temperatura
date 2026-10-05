# ============================================
#       CONVERSOR DE TEMPERATURAS
#             TEMA VERDE
# ============================================

# ---------- CORES ----------

VERDE = "\033[92m"
VERDE_ESCURO = "\033[32m"
VERDE_CLARO = "\033[1;92m"
BRANCO = "\033[97m"
VERMELHO = "\033[91m"
RESET = "\033[0m"


# ---------- FUNÇÕES DE CONVERSÃO ----------

def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_para_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_para_celsius(kelvin):
    return kelvin - 273.15


def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


# ---------- MENU ----------

def mostrar_menu():
    print(VERDE_CLARO + "\n╔══════════════════════════════════════╗")
    print("║       CONVERSOR DE TEMPERATURA      ║")
    print("╠══════════════════════════════════════╣")
    print("║  1 - Celsius → Fahrenheit           ║")
    print("║  2 - Celsius → Kelvin               ║")
    print("║  3 - Fahrenheit → Celsius           ║")
    print("║  4 - Fahrenheit → Kelvin            ║")
    print("║  5 - Kelvin → Celsius               ║")
    print("║  6 - Kelvin → Fahrenheit            ║")
    print("║  0 - Sair                            ║")
    print("╚══════════════════════════════════════╝" + RESET)


# ---------- PROGRAMA PRINCIPAL ----------

while True:

    mostrar_menu()

    opcao = input(VERDE + "Escolha uma opção: " + RESET)

    # ---------- SAIR ----------

    if opcao == "0":
        print(VERDE_CLARO + "\nPrograma encerrado. Até mais!" + RESET)
        break

    # ---------- VALIDAR OPÇÃO ----------

    if opcao not in ["1", "2", "3", "4", "5", "6"]:
        print(VERMELHO + "\nOpção inválida! Tente novamente." + RESET)
        continue

    # ---------- ENTRADA DA TEMPERATURA ----------

    try:
        temperatura = float(
            input(VERDE + "Digite a temperatura: " + RESET)
        )

    except ValueError:
        print(VERMELHO + "\nDigite apenas números!" + RESET)
        continue

    # ---------- CONVERSÕES ----------

    if opcao == "1":
        resultado = celsius_para_fahrenheit(temperatura)
        print(
            VERDE_CLARO +
            f"\n✓ {temperatura:.2f} °C = {resultado:.2f} °F" +
            RESET
        )

    elif opcao == "2":
        resultado = celsius_para_kelvin(temperatura)
        print(
            VERDE_CLARO +
            f"\n✓ {temperatura:.2f} °C = {resultado:.2f} K" +
            RESET
        )

    elif opcao == "3":
        resultado = fahrenheit_para_celsius(temperatura)
        print(
            VERDE_CLARO +
            f"\n✓ {temperatura:.2f} °F = {resultado:.2f} °C" +
            RESET
        )

    elif opcao == "4":
        resultado = fahrenheit_para_kelvin(temperatura)
        print(
            VERDE_CLARO +
            f"\n✓ {temperatura:.2f} °F = {resultado:.2f} K" +
            RESET
        )

    elif opcao == "5":
        resultado = kelvin_para_celsius(temperatura)
        print(
            VERDE_CLARO +
            f"\n✓ {temperatura:.2f} K = {resultado:.2f} °C" +
            RESET
        )

    elif opcao == "6":
        resultado = kelvin_para_fahrenheit(temperatura)
        print(
            VERDE_CLARO +
            f"\n✓ {temperatura:.2f} K = {resultado:.2f} °F" +
            RESET
        )