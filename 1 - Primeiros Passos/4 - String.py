# Definição da variável com a frase
resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprimir a variável inteira
print(resumo)  # Exibe a frase completa

# Imprimir a segunda letra da variável
print(resumo[1])  # Exibe a segunda letra da frase (índice 1)

# Imprimir a idade de Paloma (resposta esperada: "46")
idade = resumo.split()[6]  # Divide a frase em palavras e pega a 7ª palavra (a idade)
print(idade)  # Exibe a idade de Paloma

# Imprimir o trecho final da variável
print(resumo[-15:])  # Exibe os últimos 15 caracteres da frase

# Converter todas as letras para minúsculo e imprimir
print(resumo.lower())  # Exibe a frase toda em minúsculas

# Converter todas as letras para maiúscula e imprimir
print(resumo.upper())  # Exibe a frase toda em maiúsculas

# Formatar a frase para que a primeira letra de cada palavra seja maiúscula
print(resumo.title())  # Exibe a frase com a primeira letra de cada palavra em maiúscula

# Formatar a frase para que apenas a primeira letra da frase seja maiúscula
print(resumo.capitalize())  # Exibe a frase com a primeira letra maiúscula e o restante em minúscula

# Imprimir uma string utilizando uma variável, com o recurso string format
nome = "Paloma"  # Define o nome de Paloma
idade = 46  # Define a idade de Paloma
print("Nome: {}, Idade: {}".format(nome, idade))  # Formata a string para incluir nome e idade
