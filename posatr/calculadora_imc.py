# Calculadora de IMC - Índice de Massa Corporal
# Este programa calcula o IMC e classifica o resultado

try:
    # Solicita entrada do usuário
    peso = float(input("Digite seu peso corporal (kg): "))
    altura = float(input("Informe sua altura (m): "))
    
    # Validação de entrada
    if peso <= 0 or altura <= 0:
        print("❌ Erro: Peso e altura devem ser maiores que zero!")
    else:
        # Calcula o IMC (Peso / altura²)
        imc = peso / (altura ** 2)
        
        # Classifica o IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        elif imc < 35:
            classificacao = "Obesidade grau I"
        elif imc < 40:
            classificacao = "Obesidade grau II"
        else:
            classificacao = "Obesidade grau III"
        
        # Exibe os resultados
        print("\n" + "="*40)
        print(f"Peso: {peso} kg")
        print(f"Altura: {altura} m")
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        print("="*40 + "\n")

except ValueError:
    print("❌ Erro: Digite apenas números válidos!")
