# Wriet a function to convert between 'mi', 'km', 'ft', and 'm'.

def convert_distance(dis, c_from, c_to):
    if c_from.lower() == 'mi':
        if c_to == 'km':
            return dis * 1.6
        elif c_to == 'ft':
            return dis * 5280
        elif c_to == 'm':
            return dis * 1609.344
    elif c_from.lower() == "mi":
        if c_to == 'km':
            return dis * 1.6
        elif c_to == 'ft':
            return dis * 5280
        elif c_to == 'm':
            return dis * 1609.344
    elif c_from.lower() == 'mi':
        if c_to == 'mi':
            pass
        elif c_to == 'ft':
            pass
        elif c_to == 'm':
            pass
    elif c_from.lower() == 'mi':
        if c_to == 'mi':
            pass
        elif c_to == 'ft':
            pass
        elif c_to == 'm':
            pass

distance = int(input("WWhat is the number you are trying to convert:\n: "))
convert_from = input("What are you convertin from?\n: ")
convert_to = input("What are you converting to?\n: ")

print(convert_distance(distance, convert_from, convert_to))
