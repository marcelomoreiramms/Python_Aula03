# Desafio: Crie um programa que solicite ao usuário que digite seu nome,
# o valor do seu salário e o valor do bônus recebido.

# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

# Solicita ao usuário que digite seu nome

nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
    try:
        nome = input("Digite seu nome: ")
        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        # Verifica se há apenas espaços no nome
        elif nome.isspace():
            raise ValueError("O nome não pode conter apenas espaços.")
        elif len(nome.strip()) == 0:
            raise ValueError("O nome não pode estar vazio.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float
while salario_valido is not True:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        # Verifica se o salario é negativo
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        # Verifica se o salario está vazio
        if len(str(salario)) == 0:
            raise ValueError("O salário não pode estar vazio.")
        # Se o salário for válido, imprime a mensagem de sucesso e define a variável de controle para True
        else:
            print(f"Salário válido: R${salario:.2f}")
            salario_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
while bonus_valido is not True:
    try:
        bonus = float(input("Digite o valor do bônus recebido: "))
        # Verifica se o bônus é negativo
        if bonus < 0:
            raise ValueError("O bônus não pode ser negativo.")
        # Verifica se o bônus está vazio   
        if len(str(bonus)) == 0:
            raise ValueError("O bônus não pode estar vazio.")
        # Se o bônus for válido, imprime a mensagem de sucesso e define a variável de controle para True
        else:
            print(f"Bônus válido: {bonus}%")
        bonus_valido = True
    except ValueError as e:
        print(e)

# Exemplo simples de KPI para calcular o bônus final
bunus_recebido = salario * (bonus / 100)
bonus_recebido = 1000 + salario + bunus_recebido

# Imprime as informações para o usuário
print(f"{nome.title()}, seu salário é de R${salario:.2f} e seu salário com bônus final é R${bonus_recebido:.2f}.")
