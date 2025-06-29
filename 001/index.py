def classificador_idade():
  try:
    idade = int(input("Digite sua idade: "))
    
    if idade < 0:
      print("Idade inválida! Digite um valor positivo.")
    elif idade <= 12:
      classificacao = "Criança"
    elif idade <= 17:
      classificacao = "Adolescente"
    elif idade <= 59:
      classificacao = "Adulto"
    else:
      classificacao = "Idoso"
    
    if idade >= 0:
      print(f"Idade: {idade} anos")
      print(f"Classificação: {classificacao}")
          
  except ValueError:
    print("Erro! Digite apenas números inteiros.")

classificador_idade()
