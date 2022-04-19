import math

if __name__ == "__main__":
    num = abs(int(input()))
    area_of_octahedron = 2 * math.sqrt(3) * math.pow(num, 2)
    volume_of_octahedron = (1 / 3) * math.sqrt(2) * math.pow(num, 3)
    print(round(area_of_octahedron, 2),
          round(volume_of_octahedron, 2),
          sep=" ")
