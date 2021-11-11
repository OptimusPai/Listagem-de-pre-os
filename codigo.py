listagem= ('Arroz',25.00,
           'Feijão',8.00,
           'Açucar',4.60,
           'Bolacha',3.00,
           'Sal',2.30,
           'Salgadinho',2.50,
           'Leite',4.99)
print ('#'*42)
print( f'{"LISTGEM DE PREÇOS":^40}')
print('#'*42)
for pos in range (0, len(listagem)):
    if pos % 2==0:
        print ( f'R${listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
print('-'*42)
