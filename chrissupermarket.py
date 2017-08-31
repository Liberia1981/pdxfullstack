change_due = int(input("How much change is owed?: "))
q=0
d=0
n=0
p=0
while change_due > 0:
    if change_due >= 25:
        change_due -= 25
        q+=1
    elif change_due >=10:
        change_due -= 10
        d +=1
    elif change_due >=5:
        change_due -=5
        n += 1
    else:
        p += change_due
        break
else:
    p += change_due
print("Your change is {} q, {} d, {} n, {} p.".format(q, d, n, p))
