def read_list():
    sir = input('Dati lista,  fiecare element fiind separat printr-un spatiu: ')
    lista = sir.split(' ')
    result = []
    for element in lista:
        result.append(float(element))
    return result


def get_integers_part(lst):
    '''
    Cu aceasta functie vom returna partea intreaga a tuturor numerelor din lista
    :param lst: lista de float-uri
    :return: lista de intregi
    '''
    result = []
    for element in lst:
        result.append(int(element))
    return result


def test_get_integers_part():
    '''
    functie test pentru get_integers_part(lst)
    '''
    assert get_integers_part([-1, 32.56, 0, -0.5, 23]) == [-1, 32, 0, 0, 23]
    assert get_integers_part([1, 2, 3, 4, 5, 78, 89]) == [1, 2, 3, 4, 5, 78, 89]
    assert get_integers_part([]) == []
    assert get_integers_part([1.2, 4.65, 56.99, 67.8, 90.34, 12.32]) == [1, 4, 56, 67, 90, 12]
    assert get_integers_part([1.5, 3.4]) == [1, 3]


def main():
    lst = []
    while True:
        print('1. Citirea listei de floaturi fiecare numar fiind separat prin spatiu: ')
        print('2. Afisarea partii intregi a tuturor numerelor din lista')
        print('3. Afisarea tuturor numerelor din lista care apartin unui interval deschis, citit de la tastatura ')
        print('4. Afisarea tuturor numerelor a caror parte intreaga este divizor al partii fractionare ')
        print('5. Afisarea listei dupa inlocuirea fiecarui caracter din lista este inlocuit de numele acestuia  ')
        print('x. Inchidere program')
        opt = input('Alegeti optiunea pe care o doriti: ')
        if opt == '1':
            lst = read_list()
        elif opt == '2':
            intreg = get_integers_part(lst)
            print(intreg)
        elif opt == '3':
            pass
        elif opt == '4':
            pass
        elif opt == '5':
            pass
        elif opt == 'x':
            break
        else:
            print('Optiune invalida, alege altceva!')


if __name__ == '__main__':
    test_get_integers_part()
    main()
