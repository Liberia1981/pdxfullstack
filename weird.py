def numbers():
    length=2*5
    breadth=2*10
    print(length)
    print(breadth)
    return (length, breadth)
numbers()


def calculate_area(x,y):
    area = x * y
    perimeter = 2*x + 2*y
    my_result = [area, perimeter]    # put results in a list
    return my_result                 # return the list

# Main Program #
my_list = calculate_area(numbers) # two arguments are supplied
print("The resulting list looks like:", my_list)
