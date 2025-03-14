# Definição das variáveis
data_nascimento = '05-10-1976'
idade_numerica = 46
altura = 1.74

# Descobrir o tipo de dado de cada variável
print("Tipo de 'data_nascimento':", type(data_nascimento))  # <class 'str'>
print("Tipo de 'idade_numerica':", type(idade_numerica))   # <class 'int'>
print("Tipo de 'altura':", type(altura))                    # <class 'float'>

# Operação entre dados do tipo string e inteiro
# Exemplo: repetindo a string 'data_nascimento' 3 vezes
resultado_string_inteiro = data_nascimento * 3
print("Operação entre string e inteiro:", resultado_string_inteiro)  # '05-10-197605-10-197605-10-1976'

# Operação entre dados do tipo inteiro e float
# Exemplo: somando 'idade_numerica' e 'altura'
resultado_inteiro_float = idade_numerica + altura
print("Operação entre inteiro e float:", resultado_inteiro_float)  # 47.74

