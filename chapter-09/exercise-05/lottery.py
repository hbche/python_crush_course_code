# 练习9.14：彩票　创建一个列表或元素，其中包含10个数和5个字母。
# 从这个列表或元组中随机选择4个数或字母，并打印一条消息，指出只要彩票上是这4个数或字母，就中大奖了。

# 练习9.15：彩票分析　可以使用一个循环来理解中前述彩票大奖有多难。
# 为此，创建一个名为my_ticket的列表或元组，再编写一个循环，不断地随机选择数或字母，直到中大奖为止。
# 请打印一条消息，报告执行多少次循环才中了大奖。

from random import choice

char_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

# 中奖码
winning_num = []
for i in range(0, 4):
    winning_num.append(choice(char_list))

print(f"Winning number is {winning_num}")

def draw_numbers(char_list):
    """模拟抽奖"""
    result = []
    for i in range(0, 4):
        result.append(choice(char_list))
    equal = True

    for i in range(0, 4):
        if result[i] != winning_num[i]:
            equal = False

    return equal

def total_draw():
    count = 0
    is_won = False
    while not is_won:
        is_won = draw_numbers(char_list)
        count += 1
        if is_won:
            print("Wow, congratulations on your big win!")
        else:
            print("We regret to announce that your numbers didn't match the winning combination.")

    return count

print(f"You have draw {total_draw()} count.")