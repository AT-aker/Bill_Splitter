word = input()

snake_word = ""

for char in word:
    if char == char.upper():

        char = "_" + char.lower()
        snake_word += char
    else:
        snake_word += char

print(snake_word)
