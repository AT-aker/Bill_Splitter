# write your code here
import random


class InvalidInputError(Exception):
    def __init__(self, num):
        self.message = f"{num} is not valid number"
        super(InvalidInputError, self).__init__(self.message)


friend_dict = {}  # Empty dictionary of party friends


def valid_input(value_of_people):
    """Validation input and exception wrong input"""
    try:
        value = int(value_of_people)
        if value <= 0:
            raise InvalidInputError(value)
    except ValueError:
        print("No one is joining for the party")
        quit()
    except InvalidInputError:
        print("No one is joining for the party")
        quit()
    else:
        return value


def total_bill_value(value: float, num_of_friends: int):
    """Return value, what need to pay for one people from the party """
    return round(value / num_of_friends, 2)


def join_for_party(peoples):
    """This definition add peoples to dict,
     friend_dict with zero bill value"""

    print('Enter the name of every friend (including you),'
          'each on a new line:')
    for i in range(peoples):
        friend_name = input()
        friend_dict[friend_name] = 0
    return friend_dict


def update_bill(dict_of_bill: dict, total_value: float):
    """Update dictionary and return with new value of part
     in total prise"""
    if len(dict_of_bill) != 0:

        num_of = len(dict_of_bill)
        value_ = total_bill_value(total_value, num_of)
        for i in dict_of_bill.keys():
            dict_of_bill[i] = value_
        return dict_of_bill
    else:
        return dict_of_bill


def lucky_one(dict_of_bill: dict):
    """One lucky , who don`t need  to pey"""

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    choise = input()
    if choise == "Yes":
        key_list = list(item for item in dict_of_bill.keys())
        lucky = random.choice(key_list)
        lucky_bill = dict_of_bill[lucky]
        num_of = len(dict_of_bill) - 1
        value_ = total_bill_value(lucky_bill, num_of)
        for i in dict_of_bill.keys():
            dict_of_bill[i] = round(dict_of_bill.get(i) + value_, 2)
        dict_of_bill[lucky] = 0
        print(f"{lucky} is the lucky one!")
    elif choise == "No":
        print("No one is going to be lucky")
    else:
        print('Wrong input')
    return dict_of_bill


if __name__ == "__main__":
    print('Enter the number of friends joining (including you):')
    join_people = valid_input(input())
    result = join_for_party(join_people)
    print("Enter the total bill value:")
    total_bill = float(input())
    result_1 = update_bill(result, total_bill)
    resulr_2 = lucky_one(result_1)
    print(resulr_2)
