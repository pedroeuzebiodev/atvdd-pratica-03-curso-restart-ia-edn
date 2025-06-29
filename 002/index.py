def calculadora_imc():
  try:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    if peso <= 0 or altura <= 0:
      print("Peso e altura devem ser valores positivos!")
      return
    
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
      classificacao = "Abaixo do peso"
    elif imc < 25:
      classificacao = "Peso normal"
    elif imc < 30:
      classificacao = "Sobrepeso"
    else:
      classificacao = "Obeso"
    
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")
    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")
      
  except ValueError:
    print("Erro! Digite apenas números válidos.")

calculadora_imc()
