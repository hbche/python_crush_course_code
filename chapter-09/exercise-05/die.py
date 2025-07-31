
# 练习 9.13：骰子　创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。
# 编写一个名为 roll_die()的方法，它打印位于 1 和骰子面数之间的随机数。
# 创建一个 6 面的骰子并掷 10 次。
# 创建一个 10 面的骰子和一个 20 面的骰子，再分别掷 10 次。
from random import randint

class Die:
    """模拟骰子"""


    def __init__(self, sides = 6):
        self.sides = sides


    def roll_die(self):
        """根据当前骰子的面数进行掷骰子"""
        print(f"Current side is {randint(1, self.sides)}.")

die_0 = Die(6)
die_1 = Die(10)
die_2 = Die(20)
def roll_dies(die):
    """掷指定轮数的骰子"""
    print(f"\nAre you ready? I'm going to roll an {die.sides}-sided die {10} times.")
    for i in range(0, 10):
        die.roll_die()

roll_dies(die_0)
roll_dies(die_1)
roll_dies(die_2)