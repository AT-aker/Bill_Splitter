# class NotWordError(Exception):
#     def __init__(self, word):
#         self.message = word + " is not a word, sorry!"
#         super().__init__(self.message)


def check_word(word):
    for i in word:
        if i == "0":
            raise NotWordError(word)
        else:
            result = word
    return result



def error_handling(word):
    try:
        check_word(word)
    except NotWordError as err:
        print(err)
    else:
        print(word)

# if __name__ == "__main__":
#     error_handling(input())
