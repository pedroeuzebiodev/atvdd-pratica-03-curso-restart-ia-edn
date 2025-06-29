def conversor_temperatura():
  try:
    temperatura = float(input("Digite a temperatura: "))
    print("Unidades disponíveis: C (Celsius), F (Fahrenheit), K (Kelvin)")
    origem = input("Digite a unidade de origem (C/F/K): ").upper()
    destino = input("Digite a unidade de destino (C/F/K): ").upper()
    
    unidades_validas = ['C', 'F', 'K']
    if origem not in unidades_validas or destino not in unidades_validas:
      print("Unidades inválidas! Use C, F ou K.")
      return
      
    if origem == destino:
      resultado = temperatura
    else:
        if origem == 'F':
          celsius = (temperatura - 32) * 5/9
        elif origem == 'K':
          celsius = temperatura - 273.15
        else:
          celsius = temperatura
      
        if destino == 'F':
          resultado = (celsius * 9/5) + 32
        elif destino == 'K':
          resultado = celsius + 273.15
        else:
          resultado = celsius
      
    print(f"Temperatura original: {temperatura}°{origem}")
    print(f"Temperatura convertida: {resultado:.2f}°{destino}")
      
  except ValueError:
    print("Erro! Digite apenas números válidos.")

conversor_temperatura()
