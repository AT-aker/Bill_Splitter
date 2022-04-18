value_in = float(input())

if value_in < 2:
    print("Analytic")
elif 2 <= value_in <= 3:
    print("Synthetic")
elif value_in > 3:
    print("Polysynthetic")
