def addition_operation(num_1, num_2):
    """计算两个数字相加"""
    try:
        sum = int(num_1) + int(num_2)
        print(f"The sum of {num_1} and {num_2} is {sum}.")
    except ValueError:
        print("You enter is not number.")

def input_two_number():
    """获取用户输入两个数字"""

    active = True
    while active:
        first_number = input("Enter first number:")
        if first_number == 'q':
            break
        second_number = input("Enter second number:")
        if second_number == 'q':
            break
        addition_operation(first_number, second_number)

input_two_number()
