# write your code here
friend_dict = {}
print('Enter the number of friends joining (including you):')
join_people = int(input())

if join_people <= 0:
    print("No one is joining for the party")
else:
    print('Enter the name of every friend (including you),'
          'each on a new line:')
    for i in range(join_people):
        friend_name = input()
        friend_dict[friend_name] = 0

    print(friend_dict)
