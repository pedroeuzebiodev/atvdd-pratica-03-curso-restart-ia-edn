def verificador_ano_bissexto():
  try:
    ano = int(input("Digite o ano: "))
    
    if ano <= 0:
      print("Digite um ano válido (maior que 0)!")
      return

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
      resultado = "bissexto"
    else:
      resultado = "não bissexto"
    
    print(f"O ano {ano} é {resultado}.")
      
  except ValueError:
    print("Erro! Digite apenas números inteiros.")

verificador_ano_bissexto()
