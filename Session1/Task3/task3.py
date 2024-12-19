print('Введите порядковый номер вагона')
vag = int(input())
print('Введите номер вагона')
numvag = int(input())

if vag - numvag == 0:
    print(-1)
else:
    print('Количество вагонов',vag+numvag-1)