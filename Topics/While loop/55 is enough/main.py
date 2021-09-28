# put your code here
STOP_NUMBER = 55
summed = 0
count = 0
x = int(input())
while x != STOP_NUMBER:
    count += 1
    summed += x
    x = int(input())
print(count)
print(summed)
if count != 0:
    print(round(summed / count))
