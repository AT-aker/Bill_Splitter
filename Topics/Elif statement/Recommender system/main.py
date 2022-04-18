# movies = {"Lion King": 16,
#           "Trainspotting": 25,
#           " Matrix": 40,
#           "Pulp Fiction": 60
#           }

age_user = int(input())

if age_user <= 16:
    print("Lion King")
elif 17 <= age_user <= 25:
    print("Trainspotting")
elif 26 <= age_user <= 40:
    print("Matrix")
elif 41 <= age_user <= 60:
    print("Pulp Fiction")
elif age_user > 60:
    print("Breakfast at Tiffany's")
# for i in movies.values():
#     if age_user < i:
#         print(movies.get(i))
