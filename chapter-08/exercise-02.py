# 练习8.3: T恤　编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
# 这个函数应该打印一个句子，简要地说明T恤的尺码和字样。
# 先使用位置实参调用这个函数来制作一件T恤，再使用关键字实参来调用这个函数。
# def make_shirt(size, text):
#     """指定T恤的尺码及字样"""
#     print(f"这是一件{size}码T恤，上面印有\"{text}\"字样。")
# make_shirt(34, 'Have a good time!')
# make_shirt(text='Build your dream.', size=30)

# 练习8.4：大号T恤　修改make_shirt()函数，使其在默认情况下制作一件印有“I love Python”字样的大号T恤。
# 调用这个函数分别制作一件印有默认字样的大号T恤，一件印有默认字样的中号T恤，以及一件印有其他字样的T恤（尺码无关紧要）​。
# def make_shirt(text, size='big'):
#     print(f"I have a {size} size T-Shirt.It's wrote '{text}'")
# # 默认参数调用
# make_shirt('I love python.')
# # 位置参数调用
# make_shirt('I love python', 'medium')
# # 关键字参数调用
# make_shirt(text='I love python', size='medium')

# 练习8.5：城市　编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
# 这个函数应该打印一个像下面这样简单的句子。　　
# Reykjavik is in Iceland.给用于存储国家的形参指定默认值。
# 为三座不同的城市调用这个函数，其中至少有一座城市不属于默认的国家。
def describe_city(city, country='Iceland'):
    """描述一个城市位于哪个国家"""
    print(f"{city.title()} in {country.title()}.")
describe_city('Reykjavik')
describe_city('Wuhan', 'China')
describe_city(country = 'Japan', city = 'Tokyo')