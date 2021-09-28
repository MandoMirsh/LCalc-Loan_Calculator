MONDAY_BOUNDARY = -11
WEDNESDAY_BOUNDARY = 14
timezone = int(input())
if timezone <= MONDAY_BOUNDARY:
    print("Monday")
elif timezone >= WEDNESDAY_BOUNDARY:
    print("Wednesday")
else:
    print("Tuesday")
