class NegativeSumError(Exception):
    def __init__(self, num):
        self.message = f'{num} is negative'
        super().__init__(self.message)
    def __str__(self):
        return self.message


def sum_with_exceptions(a, b):
    sum_ = a + b
    num_err = 0
    if sum_ < num_err:
        raise NegativeSumError(sum_)
    return sum_

