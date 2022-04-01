# squares = {1: 1, 3: 9, 5: 25, 6: 36, 8: 64, 10: 100, 11: 121, 15: 225}

n = int(input())

# for i in squares.key:
#     a = squares.pop(i)
#     print(a)
#

if n in squares.keys():
    a = squares.pop(n)
    print(a)
else:
    print('There is no such key')

print(squares)