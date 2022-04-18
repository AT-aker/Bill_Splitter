# put your python code here
first_number = float(input())
second_number = float(input())
operation = input()
result = 0



if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "/":
    if second_number == 0:
        result = "Division by 0!"
    else:
        result = first_number / second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "mod":
    if second_number == 0:
        result = "Division by 0!"
    else:
        result = first_number % second_number
elif operation == "pow":
    result = first_number ** second_number
elif operation == "div":
    if second_number == 0:
        result = "Division by 0!"
    else:
        result = first_number // second_number
print(result)
