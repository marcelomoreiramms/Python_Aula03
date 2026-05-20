# Python - Aula 03 - Exercícios de Condicionais e Loops

### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

```python
quantidade = float(input("Digite a quantidade: "))
preco = float(input("Digite o preço: "))
if quantidade > 0 and preco > 0:
    print("Dados válidos!")
else:
    print("Dados inválidos!")
```

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

```python
sensores = [
    {'id 1': 1, 'temperatura': 15},
    {'id 2': 2, 'temperatura': 25},
    {'id 3': 3, 'temperatura': 35}
]
for sensor in sensores:
    if sensor['temperatura'] < 20:
        print("Sensor {sensor['id 1']}: Baixa")
    elif sensor['temperatura'] <= 30:
        print("Sensor {sensor['id 2']}: Normal")
    else:
        print("Sensor {sensor['id 3']}: Alta")
```

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

```python
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print(log['message'])
elif log['level'] == 'WARNING':
    print("Atenção: " + log['message'])
elif log['level'] == 'INFO':
    print("Informação: " + log['message'])
else:
    print("Não há mensagens de erro, warning ou info.")
```

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

```python
nome_usuario = input("Digite o nome do usuário: ")
idade_usuario = int(input("Digite a idade do usuário: "))
email_usuario = input("Digite o email do usuário: ")
if 18 <= idade_usuario <= 65:
    if "@" in email_usuario and "." in email_usuario:
        print("Dados de usuário válidos!")
    else:
        print("Erro: Email inválido.")
else:
    print("Erro: Idade inválida. O usuário deve ter entre 18 e 65 anos.")
```

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

```python
transacao = {'valor': 5000, 'hora': 10}
if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação suspeita!")
else:
    print("Transação normal.")
```

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

```python
texto = "Python é uma linguagem de programação. Python é fácil de aprender."
palavras = texto.split()
contador_palavras = {}
for palavra in palavras:
    palavra = palavra.lower().strip(".,")
    if palavra in contador_palavras:
        contador_palavras[palavra] += 1
    else:
        contador_palavras[palavra] = 1
print(contador_palavras)
```

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

```python
lista_numeros = [5, 15, 35, 50, 70, 80]
min_num = min(lista_numeros)
max_num = max(lista_numeros)
lista_normalizada = [(num - min_num) / (max_num - min_num) for num in lista_numeros]
print(lista_normalizada)
```

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, 
# filtrar aqueles que têm um campo específico faltando

```python
lista_usuarios = [
    {'nome': 'Alice', 'idade': '20', 'email': 'alice@example.com'},
    {'nome': 'Bob', 'idade': '25', 'email': ''},
    {'nome': 'Charlie', 'idade': '', 'email': 'charlie@example.com'}
    ]
while True:
    usuario = input("Digite o nome do usuário para verificar (ou 'sair' para encerrar): ")
    if usuario.lower() == 'sair':
        break
    encontrado = False
    for user in lista_usuarios:
        if user['nome'].lower() == usuario.lower():
            encontrado = True
            if user['idade'] and user['email']:
                print(f"Usuário {usuario} tem dados completos.")
            else:
                print(f"Usuário {usuario} tem dados faltantes.")
            break
    if not encontrado:
        print(f"Usuário {usuario} não encontrado na lista.")
```

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

```python
lista_numeros = [10,11,15,20,35,40,48,50,62,75,80,90]
numeros_pares = [num for num in lista_numeros if num % 2 == 0]
print("Os números pares da lista são:", numeros_pares)
```

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

```python
vendas = [
    {'categoria': 'roupas', 'valor': 150},
    {'categoria': 'eletrônicos', 'valor': 300},
    {'categoria': 'roupas', 'valor': 200},
    {'categoria': 'eletrônicos', 'valor': 450},
    {'categoria': 'alimentos', 'valor': 100},
    {'categoria': 'pet', 'valor': 50}
]
total_vendas = {}
for venda in vendas:
    categoria = venda['categoria']
    valor = venda['valor']
    if categoria in total_vendas:
        total_vendas[categoria] += valor
    else:
        total_vendas[categoria] = valor
print("Total de vendas por categoria:")
for categoria, total in total_vendas.items():
    print(f"{categoria}: R$ {total}")
```


### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

```python
dados = []
while True:
    entrada = input("Digite um dado qualquer (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    dados.append(entrada)
print("Dados coletados:", dados)
```

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

```python
numero = []
while numero == []:
    try:
        entrada = int(input("Digite um número entre 1 e 10: "))
        if 1 <= entrada <= 10:
            numero = [entrada]
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
print(f"Número válido digitado: {numero[0]}")
```

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, 
# onde cada "página" de dados é processada em loop até que não haja mais páginas.

```python
api_data = {
    'page1': ['dado1', 'dado2', 'dado3'],
    'page2': ['dado20', 'dado30', 'dado40'],
    'page3': ['dado300', 'dado400', 'dado500'],
    'page4': []
    }
while True:
    page = input("Digite a página que deseja acessar (page1, page2, page3,page4) ou 'sair' para encerrar: ")
    if page.lower() == 'sair':
        break
    elif page in api_data:
        if api_data[page]:
            print(f"Dados da {page}: {api_data[page]}")
        else:
            print(f"{page} não contém dados.")
    else:
        print("Página inválida. Tente novamente.")
```

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

```python
tentativas = 0
max_tentativas = 5
while tentativas < max_tentativas:
    print(f"Tentativa {tentativas + 1} de {max_tentativas}...") # Simulação de tentativa de conexão (substitua por lógica real de conexão)
    sucesso = False  # Simula falha na conexão
    if sucesso:
        print("Conexão bem-sucedida!")
        break
    else:
        print("Falha na conexão. Tentando novamente...")
        tentativas += 1
if tentativas == max_tentativas:
    print("Número máximo de tentativas atingido. Conexão falhou.")
```

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

```python
itens = ['item1', 'item2', 'item3', 'item4', 'parar', 'item5']
while itens:
    item = itens.pop(0)
    if item == 'parar':
        print("Valor de parada encontrado. Encerrando processamento.")
        break
    print(f"Processando {item}...")
```