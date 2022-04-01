dict_card = {str(key): key for key in range(2, 11)}
dict_card.update(Jack=11)
dict_card.update(Queen=12)
dict_card.update(King=13)
dict_card.update(Ace=14)
# print(dict_card)
a = 0
for i in range(6):
    char = input()
    if char in dict_card.keys():
        a += dict_card.get(char, 0)

b = a / 6

print(b)