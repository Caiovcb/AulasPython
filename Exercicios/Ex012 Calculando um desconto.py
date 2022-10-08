produto = float(input('Qual o valor do produto desejado R$: '))
desc = produto*5/100
print ('O produto no valor de R${:.2f}, Sairá com desconto de 5%, você devera pagar R${:.2f}'.format(produto, produto - desc))
