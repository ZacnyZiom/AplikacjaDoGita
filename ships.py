import numpy as np
print('====== Statki ======')
comp_ships = np.full((10, 10), ' ')
for row in range(10):
    for col in range(10):
        print(f'|{comp_ships[row][col]}', end='')
    print('|')

print('Podaj wspolrzedne strzalu (wiersz i kolumna): ')
row_col = input()
