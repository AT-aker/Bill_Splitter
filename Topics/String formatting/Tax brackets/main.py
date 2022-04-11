income: int = int(input())
percent = 0
calculated_tax = 0

if 0 <= income <= 15527:
    percent = 0
    # calculated_tax = int(income * (percent / 100))
elif 15528 <= income <= 42707:
    percent = 15
    # calculated_tax = int(income * (percent / 100))
elif 42708 <= income <= 132406:
    percent = 25
    # calculated_tax = int(income * (percent / 100))
elif income >= 132407:
    percent = 28

else:
    print("Wrong input")

calculated_tax = income * (percent / 100)
print(f"The tax for {income} is {percent}%." +
      f" That is {round(calculated_tax)} dollars!"
      )
