all_summa = 0
history = [ ]

def buy(all_summa):
    summa = int(input('Введите сумму покупки: '))
    if summa > all_summa:
        print('Недостаточно средств')
    else:
        all_summa -= summa
        pokupka = input('Введите название покупки: ')
        history.append((pokupka, summa))
    return all_summa



while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Ваш счёт {all_summa}')

    menu = input('Выберите пункт меню: ')
    if menu == '1':
        summa = int(input('Введите сумму пополнения: '))
        all_summa += summa
    elif menu == '2':
        all_summa = buy(all_summa)
    elif menu == '3':
        print(history)
    elif menu == '4':
        break
    else:
        print('Неверный пункт меню')