# Lab: Hammer

# Delivery Method: Doctests

# Goal

# Write a function that returns the meal for any given hour of the day or night in respect to the following schedule:
# what time is it
# what are our meal times
#find out if am or pm
#return what mealtime it is

"""
Breakfast: 7AM - 9AM
Lunch: 12PM - 2PM
Dinner: 7PM - 9PM
Hammer: 10PM - 4AM
"""


meal_time = input('what time is it?: ')
meridian = meal_time[-2:]
time = int(meal_time[:-2])
print(meal_time)
print(meridian)
print(time)
if meridian.lower()== 'am':
    if time >=7 and time <=9:
        print("{} is Breakfast TIME!!!".format(meal_time))
    elif time == 12 or time >=1 and time <=4:
        print('{} is Hammer Time!!!'.format(meal_time))
elif meridian.lower()=='pm':
    if time ==12 or time==1 or time ==2:
        print("{} is Lunch Time!!!".format(meal_time))
    elif time >=7 and time <=9:
        print("{} is Dinner Time!!!!".format(meal_time))
    elif time >= 10 and time <=11:
        print("{} is Hammer Time!!!!".format(meal_time))
else:
    print("This doesn't seem like a good time to eat duuuud",)
