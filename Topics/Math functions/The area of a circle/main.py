import math

def area_of_circle(radius):
    area_of = math.pi * math.pow(radius, 2)
    return round(area_of, 2)

if __name__ == "__main__":
    rad = int(input())
    print(area_of_circle(rad))