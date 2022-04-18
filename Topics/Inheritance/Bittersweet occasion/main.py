# finish the function
def find_the_parent(child):
    trolley = (Drinks, Pastry, Sweets)
    for i in trolley:
        if issubclass(child, i):
            print(i.__name__)
