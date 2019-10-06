# Inicialmente, pedimos os dois números para o usuário
# Vamos transformar ele em float
var1 = float( input("Digite um numero: ") )
var2 = float( input("Digite outro numero: ") )

# Calculando a soma e armazenando na variável 'soma'
soma = var1 + var2

# Calculando a subtração e armazenando na variável 'subtracao'
subtracao = var1 - var2

# Calculando a multiplicação e armazenando na variável 'mult'
mult = var1 * var2

# Calculando a divisão e armazenando na variável 'div'
div = var1 / var2

# Calculando a exponenciação e armazenando na variável 'expo'
expo = var1 ** var2

# Calculando o resto da divisão e armazenando na variável 'resto'
resto = var1 % var2

# Imprimindo tudo
print('Soma:             ', var1,'+',var2,' = ' , soma)
print('Subtração:        ', var1,'-',var2,' = ' , subtracao)
print('Multiplicação:    ', var1,'*',var2,' = ' , mult)
print('Divisão:          ', var1,'/',var2,' = ' , div)
print('Exponenciação:    ', var1,'**',var2,' = ', expo)
print('Resto da divisão: ', var1,'%',var2,' = ' , resto)