from statistics import mean


int_list = []

while True:
    i = input()
    if i != ".":
        int_list.append(int(i))
    else:
        break

result = mean(int_list)
print(result)
