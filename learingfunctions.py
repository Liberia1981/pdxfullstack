# #NOTHING GOES IN, NOTHING COMES OUT
# def display_message():
#     print("****   PYTHON IS GREAT   ****")
#     print("=============================")
#
# # Main Program #
# radius = 5
# print("The radius of the circle is: ", radius)
# display_message()    # The function call
#
# circumference = 2*3.14*radius
# print("The circumference of the circle is:", circumference)
# display_message()    # The function call

#NOTHING GOES IN, SOMETHING COMES OUTS
# import random
#
# def report_random():
#     my_number = random.randint(20, 100)
#     return my_number
#
# # Main Program #
# a = report_random()    # return a random int and assign it to a
# print("a is equal to ", a)
# b = report_random()    # return a random int and assign it to b
# print("b is equal to ", b)
# c = report_random()    # return a random int and assign it to c
# print("c is equal to ", c)

#SOMETHING GOES IN, NOTHING COMES OUT
# def calculate_area(length, breadth):
#     area = length * breadth
#     perimeter = 2*length + 2*breadth
#     print("area is equal to", area)
#     print("perimeter is equal to", perimeter)
#
# # Main Program #
# calculate_area(10, 20)

# SOMETHING GOES IN, SOMETHING COMES OUT
#
# def calculate_area(length, breadth):
#     area = length * breadth
#     perimeter = 2*length + 2*breadth
#     my_result = [area, perimeter]    # put results in a list
#     return my_result                 # return the list
#
# # Main Program #
# my_list = calculate_area(10, 20) # two arguments are supplied
# print("The resulting list looks like:", my_list)

# This function calculates and returns the square root
# of the number which is given to it as input.
# def my_square_root(input_number):
#     square_root = input_number/2
#     accuracy=0.001
#     while abs(input_number-(square_root**2)) >accuracy:
#         square_root = (square_root +(input_number/square_root))/2
#     return(square_root)
#
# #This is the main program to check the my_square_root_function
#
# for x in range(1,21):
#     y= my_square_root(x)
#     print("Square root of ", x, "is", y)
# def sum_sample(sample_list):
#     my_sum = 0
#     print(len(sample_list))
#     for item in sample_list:
#         my_sum=my_sum+item
#     print (my_sum)
#
sample_l=[1,330,3,4,100]
# sum_sample(lst)

def _find_max_sample_(lst):
    # Initially set the first element
    # of the list as the maximum
    my_max = lst[0]     # this is the current maximum
    print(my_max)
    # Iterate through the list
    for item in lst:
        # Compare each item from the list
        # to the current maximum. If the item is larger
        # than your current maximum then set that item
        # to be your current maximum instead
        if item > my_max:
            my_max = item
            print(my_max)
    # finally return the maximum value
    return (my_max)


_find_max_sample_(sample_l)
