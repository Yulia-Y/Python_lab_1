f = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '], 'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
     'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   ']}
s = input()
for i in range(5):
    for k in s:
        print(f.get(k)[i], end='')
    print()