def read_list():
    sir = input('Dati lista de floaturi separata prin spatiu: ')
    lista = sir.split(' ')
    res = []
    for element in lista:
        res.append(float(element))

    return res


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
    assert get_integers_part([-1, 32.56, 0, -0.5, 23]) == [-1, 32, 0, 0, 23]
    assert get_integers_part([1, 2, 3, 4, 5, 78, 89]) == [1, 2, 3, 4, 5, 78, 89]
    assert get_integers_part([]) == []
    assert get_integers_part([1.2, 4.65, 56.99, 67.8, 90.34, 12.32]) == [1, 4, 56, 67, 90, 12]
    assert get_integers_part([1.5, 3.4]) == [1, 3]


def get_all_numbers_in_open_interval(lst, s, d):
    '''
    Functie care are ca paramtrii o lista si capetele intervalului si care returneaza toate numerele din interval
    :param lst: lista de float-uri
    :param s: capatul din stanga
    :param d: capatul din dreapta
    :return: toate elementele care fac parte din interval
    '''
    result = []
    for element in lst:
        if element > s and element < d:
            result.append(element)
    return result


def test_get_all_numbers_in_open_interval():
    assert get_all_numbers_in_open_interval([1, 2, 3, 4, 5], 2, 5) == [3, 4]
    assert get_all_numbers_in_open_interval([], 12, 34) == []
    assert get_all_numbers_in_open_interval([-1.4, -56, 34.5, 65, 23.54, 45.01], 700, 800) == []
    assert get_all_numbers_in_open_interval([1.5, -3.3, 8, 9.8, 3.2], -4, 5) ==  [1.5, -3.3, 3.2]
    assert get_all_numbers_in_open_interval([1.4, 6, 7, 9], 5, 10) == [6, 7, 9]


def get_all_elements_with_integer_part_being_a_divisor_of_fractional_part(lst):
    '''
    Functie ce are ca parametrii lista de float-uri si returneaza elementele care au partea intreaga divizor al partii fractionale
    :param lst: lista de floaturi
    :return: o lista cu elementele ce au partea intreaga divizor al partii fractionale
    '''
    result = []
    for element in lst:
        string_element = str(element)
        decimale = string_element.split('.')[1]
        intreg = string_element.split('.')[0]
        fract = int(decimale)
        it = int(intreg)
        if fract % it == 0 and fract != 0:
            result.append(element)
    return result


def test_get_all_elements_with_integer_part_being_a_divisor_of_fractional_part():
    assert get_all_elements_with_integer_part_being_a_divisor_of_fractional_part([1.5, 2.6]) == [1.5, 2.6]
    assert get_all_elements_with_integer_part_being_a_divisor_of_fractional_part([]) == []


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
            stanga = float(input('Dati capatul din stanga al intervalului: '))
            dreapta = float(input('Dati capatul din dreapta al intervalului: '))
            interval = get_all_numbers_in_open_interval(lst, stanga, dreapta)
            print(interval)
        elif opt == '4':
            divizorul = get_all_elements_with_integer_part_being_a_divisor_of_fractional_part(lst)
            print(divizorul)
        elif opt == '5':
            pass
        elif opt == 'x':
            break
        else:
            print('Optiune invalida, alege altceva!')


if __name__ == '__main__':
    test_get_integers_part()
    test_get_all_numbers_in_open_interval()
    test_get_all_elements_with_integer_part_being_a_divisor_of_fractional_part()
    main()
