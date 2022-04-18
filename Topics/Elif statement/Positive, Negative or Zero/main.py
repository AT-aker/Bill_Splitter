number_of_int = int(input())

if number_of_int == 0:
    print('zero')
else:
    if number_of_int < 0:
        print('negative')
    elif number_of_int > 0:
        print('positive')