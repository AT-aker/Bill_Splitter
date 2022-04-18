class LessThanFiveHundredError(Exception):
    def __init__(self, num):
        self.message = "The integer %s is below 500!" % str(num)
        super().__init__(self.message)


def example_exceptions_5(num):
    if num < 500:
        raise LessThanFiveHundredError(num)
    else:
        print(num)

if __name__ == "__main__":
    example_exceptions_5(int(input()))