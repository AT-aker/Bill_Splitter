# class NotInBoundsError(Exception):
#     def __str__(self):
#         return "There is an error!"

def check_integer(num):
    if 45 < int(num) < 67:
        return int(num)
    else:
        raise NotInBoundsError

def error_handling(num):
    try:
        check_integer(num)
    except NotInBoundsError as err:
        print(err)
    else:
        print(num)

# if __name__ == "__main__":
#     error_handling(int(input()))
