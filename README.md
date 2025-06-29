<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/pedroeuzebiodev/atvdd-pratica-03-curso-restart-ia-edn?color=3b82f6" />

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/pedroeuzebiodev/atvdd-pratica-03-curso-restart-ia-edn" />

  <a href="https://github.com/pedroeuzebiodev/atvdd-pratica-03-curso-restart-ia-edn/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/pedroeuzebiodev/atvdd-pratica-03-curso-restart-ia-edn" />
  </a>

   <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen" />

   <a href="https://github.com/pedroeuzebiodev/atvdd-pratica-03-curso-restart-ia-edn/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/pedroeuzebiodev/atvdd-pratica-03-curso-restart-ia-edn?style=social" />
  </a>

  <a href="https://pedroeuzebiodev.github.io/atvdd-pratica-03-curso-restart-ia-edn">
    <img alt="Feito pelo Pedro Euzebio" src="https://img.shields.io/badge/feito%20por-Pedro%20Euzebio-3b82f6" />
  </a>
</p>

<h4 align="center">
 🚧  Atividade Prática 03 do curso Restar + IA da Escola da Nuvem (EdN) 🔗 Concluído 🚀 🚧
</h4>

<p align="center">
 <a href="#-sobre-o-projeto">Questões</a> •
 <a href="#-tecnologias">Tecnologias</a> •
 <a href="#-autor">Autor</a> •
 <a href="#user-content--licença">Licença</a>
</p>

## Questões

### 1. Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:

- Criança (0-12 anos)
- Adolescente (13-17 anos)
- Adulto (18-59 anos)
- Idoso (60 anos ou mais)

**Resolução:**

```py
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
```

### 2. Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

- < 18.5: classificacao = "Abaixo do peso"
- < 25: classificacao = "Peso normal"
- < 30: classificacao = "Sobrepeso"
- Para os demais cenários: classificacao = "Obeso"

**Resolução:**

```py
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
```

### 3. Conversor de Temperatura

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

**Resolução:**

```py
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
```

### 4. Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

**Resolução:**

```py
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
```

---

## 🛠 Tecnologias

A seguinte ferramenta foi usada na construção da atividade:

- **[Python](https://www.python.org)**

---

## 🦸 Autor

<a href="https://www.linkedin.com/in/pedroeuzebio">
  <img style="border-radius: 50%;" src="https://i.imgur.com/uieVTmO.png" width="100px;" alt="" />

  <br />

  <sub>
    <b>Pedro Euzebio</b>
  </sub>
</a>

<br>

<a href="mailto:pedroeuzebio.contato@gmail.com" class="contato">
  <img src="https://img.shields.io/badge/Gmail-D14836?style=plastic&logo=gmail&logoColor=white" />
</a>

<a href="https://www.linkedin.com/in/pedroeuzebio" class="contato">
  <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=plastic&logo=linkedin&logoColor=white" />
</a>

---

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).

Feito com ❤️ por Pedro Euzebio 👋 [Entre em contato!](https://www.linkedin.com/in/pedroeuzebio)
