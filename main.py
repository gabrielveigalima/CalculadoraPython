s = 's'
soma = lambda x,y: x+y
sub = lambda x,y: x-y
div = lambda x,y: x/y
mul = lambda x,y: x*y


while s == 's':
    operacao = input('Digite a operação que você irá fazer: \n + -> soma \n - -> subtração \n * -> multiplicação \n / -> divição\n')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    verificaOperacao = False
    if operacao == '+':
        resul = soma(n1,n2)
        verificaOperacao = True
    elif operacao == '-':
        resul = sub(n1,n2)
        verificaOperacao = True
    elif operacao == '/':
        resul = div(n1,n2)
        verificaOperacao = True
    elif operacao == '*':
        resul = mul(n1,n2)
        verificaOperacao = True
    if verificaOperacao  == True:
        print('{0} {1} {2} = {3}'.format(n1,operacao,n2,resul))
    else:
        print('Opção de operação inválida!!!')
    s = str(input('Deseja fazer outra operação? [s/n]')).lower()
    