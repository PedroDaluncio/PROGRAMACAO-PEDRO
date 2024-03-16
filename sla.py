def organiza_nums(array):
    array2 = []
    maior_num = array[0]
    while len(array2) < len(array):
        menor_num = array[0]
        for number in array:
            if menor_num > number and number not in array2:
                menor_num = number
            elif menor_num < number and number not in array2:
                maior_num = number
        if menor_num not in array2:
            array2.append(menor_num)
        elif maior_num not in array2:
            array2.append(maior_num)
    return array2


print(organiza_nums([9,20,  0, 5, 12, 2 ,10]))
