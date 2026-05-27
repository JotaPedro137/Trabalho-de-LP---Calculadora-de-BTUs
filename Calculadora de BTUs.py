# =========================================
# PROJETO: CALCULADORA DE BTUs
# =========================================


# Função para calcular os BTUs
def calcular_btus(area, pessoas, eletronicos, sol):

    # Cálculo base pela área
    btus = area * 600

    # Adiciona BTUs para pessoas extras
    if pessoas > 1:
        btus += (pessoas - 1) * 600

    # Adiciona BTUs para eletrônicos
    btus += eletronicos * 600

    # Adiciona BTUs se o ambiente recebe muito sol
    if sol == "S":
        btus += 800

    # Retorna o valor calculado
    return btus


# Função para recomendar o ar-condicionado
def recomendar_ar(btus):

    if btus <= 9000:
        return "9.000 BTUs"

    elif btus <= 12000:
        return "12.000 BTUs"

    elif btus <= 18000:
        return "18.000 BTUs"

    elif btus <= 24000:
        return "24.000 BTUs"

    else:
        return "Acima de 24.000 BTUs"


# =========================
# PROGRAMA PRINCIPAL
# =========================

print("=" * 40)
print("      CALCULADORA DE BTUs")
print("=" * 40)

continuar = "S"

while continuar == "S":

    print("\nPreencha as informações do ambiente:\n")

    # Entrada de dados
    area = float(input("Área do ambiente (m²): "))
    pessoas = int(input("Quantidade de pessoas: "))
    eletronicos = int(input("Quantidade de eletrônicos: "))
    sol = input("Recebe muito sol? (S/N): ").upper()

    # Chama a função para calcular os BTUs
    resultado = calcular_btus(area, pessoas, eletronicos, sol)

    # Exibe os resultados
    print( "=" * 40)
    print("RESULTADO")
    print("=" * 40)

    print(f"BTUs recomendados: {resultado:.0f}")
    print(f"Ar-condicionado indicado: {recomendar_ar(resultado)}")

    # Pergunta se deseja continuar
    continuar = input("\nDeseja fazer outro cálculo? (S/N): ").upper()

# Mensagem final
print("Programa encerrado.")