
float_list = []

while True:
    i = input()
    if i == "." and len(i) == 1:
        break
    else:
        float_list.append(float(i))

print(min(float_list))
