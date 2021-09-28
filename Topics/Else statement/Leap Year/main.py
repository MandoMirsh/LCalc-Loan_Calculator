year = int(input())
Result = "Ordinary"
if year % 400 == 0:
    Result = "Leap"
if year % 100 != 0:
    if year % 4 == 0:
        Result = "Leap"
print(Result)
