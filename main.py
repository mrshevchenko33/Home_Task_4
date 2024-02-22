first_num = int(input('Please enter first number: '))
second_num = int(input('Please enter second number:  '))
action = input('Please enter action:  ')

if action == '*':
    print(first_num * second_num)
if action == '+':
    print(first_num + second_num)
if action == '-':
    print(first_num - second_num)
if action == '/':
    if second_num == 0:
        print("You can't divide by 0")
    else:
        print(first_num/second_num)
