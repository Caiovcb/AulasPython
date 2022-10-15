print('='*30)
print('    10 TERMOS DE UMA PA')
print('='*30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = razao+termo
print(termo, '-> ','{}'.format(contador), ' -> ', end="")
for c in range (1, 9):
    contador = contador + razao
    print('{} -> '.format(contador), end="")
