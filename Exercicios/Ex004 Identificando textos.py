id = input('Digite algo: ')
print('Detalhes sobre "{}" abaixo: '.format(id))
print('Só tem espaços ? ', id.isspace())
print('Só tem numeros ?', id.isnumeric())
print('Só tem letras ? ', id.isalpha())
print('Tem letras e numeros ? ', id.isalnum())
print('Esta escrito todo em letra maiuscula? ', id.isupper())
print('Esta escrito todo em letra minucscula?', id.islower())
print('Esta captalizada? ', id.istitle())