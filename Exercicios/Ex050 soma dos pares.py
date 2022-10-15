print('Digite números inteiros.')
par = 0
contador = 0
for c in range (1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    contador = contador + 1
    calculo = num%2
    if calculo == 0:
        par = par + num
        print('{} é par, o valor somado até agora é de: {}'.format(num, par))
    else:
        print('{} é um número impar, não soma'.format(num))
    
print('Você informou {} numeros, dos valores informados a soma dos \
pares é de {}. '.format(contador, par))