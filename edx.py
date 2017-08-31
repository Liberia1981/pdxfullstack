# radius_value=int(input("What is radius "))
# area=(radius_value*radius_value) * 3.14
# perimeter =(radius_value *2) * 3.14
# print(area)
# print(perimeter)
# my_list=['hello', 5, True, 'yellow', 7]
# print(my_list)
# # print(my_list[1] and [2])
# user=int(input('what is the value of x '))
# x = user
# y = x**2 - 12 * x + 11
# print(y)
# print(my_list[1] and [2])
# user=int(input('Pick a number from 1 to 7 '))
# if user == 1:
#     print('monday')
# elif user == 2:
#     print('tuesday')
# elif user == 3:
#     print('wednesday')
# elif user == 4:
#     print('thursday')
# elif user == 5:
#     print('friday')
# elif user == 6:
#     print('saturday')
# elif user == 7:
#     print('sunday')
# else:
#     pass
# user_response = int(input("Enter first integer:"))
# index=(user_response)
# if user_response > 7:
#     print("There's only 7 days in a week")
# else:
#     days = ["MONDAY", "TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY", "SUNDAY"]
#     print(days[user_response-1])

x=0
count=0
while x <= 101:
    if x%5==0:
        count = count+x
    x=x+1
print(count)
