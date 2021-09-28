DIVISION = "/ div mod"
first_num = float(input())
second_num = float(input())
operation = input()
if operation in DIVISION:
    if second_num == 0:
        print("Division by 0!")
    elif operation == '/':
        print(first_num / second_num)
    elif operation == 'mod':
        print(first_num % second_num)
    else:
        print(first_num // second_num)
else:
    if operation == '+':
        print(first_num + second_num)
    elif operation == '-':
        print(first_num - second_num)
    elif operation == '*':
        print(first_num * second_num)
    else:
        print(pow(first_num, second_num))
