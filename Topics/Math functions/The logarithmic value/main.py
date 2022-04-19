import math


def is_base_for_log(num):
    assert num > 1, "Not positive"
    return num


def logarithm(first_num, second_num):
    num = abs(first_num)
    try:
        is_base_for_log(second_num)
    except AssertionError:
        result = math.log(num)
    else:
        result = math.log(num, second_num)
    return round(result, 2)


if __name__ == "__main__":
    f_num = int(input())
    s_num = int(input())
    print(logarithm(f_num, s_num))
    # is_positive(int(input()))
