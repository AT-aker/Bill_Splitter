# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here

group_dict = dict.fromkeys(groups)
n = int(input())
children = []
for i in range(n):
    a = int(input())
    children.append(a)
    group_dict[groups[i]] = a

# for k in groups:
#     if c <= n:
#         group_dict[k] =
#         c += 1


print(group_dict)
