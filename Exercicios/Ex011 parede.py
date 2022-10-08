largura = float(input('Qual a Largura da sua parede: '))
altura = float(input('Qual a altura da sua parede: '))
area = altura*largura
litro = area / 2
print('Sua parede tem {:.2f}x{:.2f} de LxA contabiliazndo {:.2f}m² '.format(largura, altura, area))
print('Para pintar {}m² você ira precisar de  {}L de tintas.'.format(area, litro))
