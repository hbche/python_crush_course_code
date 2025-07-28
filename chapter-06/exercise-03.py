# 练习6.7：人们　在为练习6.1编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people的列表中。遍历这个列表，将其中每个人的所有信息都打印出来。
# 练习6.8：宠物　创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets的列表中，再遍历该列表，并将有关每个宠物的所有信息打印出来。
# # 多个宠物字典
# pet_1 = {'type': 'dog',   'owner': 'Alice'}
# pet_2 = {'type': 'cat',   'owner': 'Bob'}
# pet_3 = {'type': 'parrot','owner': 'Carol'}
# pet_4 = {'type': 'hamster','owner': 'David'}

# # 统一放入列表
# pets = [pet_1, pet_2, pet_3, pet_4]
# for pet in pets:
#     print(f"{pet['owner']} has a {pet['type']}")

# 练习6.9：喜欢的地方　创建一个名为favorite_places的字典。在这个字典中，将三个人的名字用作键，并存储每个人喜欢的1～3个地方。为让这个练习更有趣些，让一些朋友说出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
# favorite_places = {
#     'Alice': ['Kyoto', 'Santorini'],
#     'Bob':   ['New York'],
#     'Carol': ['Paris', 'Rome', 'Bali']
# }
# for name, cities in favorite_places.items():
#     print(f"{name.title()}, your favorite places are:")
#     for city in cities:
#         print(f"\t{city}")

# 练习6.10：喜欢的数2　修改为练习6.2编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数打印出来。
# favorite_nums = {
#     'Jack': [9, 8],
#     'Tom': [5],
#     "Alice": [8, 3],
#     'Lucy': [1],
#     'Bob': [6]
# }

# for name, numbers in favorite_nums.items():
#     print(f"{name}'s favorite numbers are:")
#     for num in numbers:
#         print(f"\t{num}")

# 练习6.11：城市　创建一个名为cities的字典，将三个城市名用作键。对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。表示每座城市的字典都应包含country、population和fact等键。将每座城市的名字以及相关信息都打印出来。
cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 37_400_000,        # Greater Tokyo Area, 2023 est.
        'fact': 'The Greater Tokyo Area is the most populous metropolitan region in the world.'
    },
    'New York': {
        'country': 'United States',
        'population': 8_300_000,         # NYC proper, 2023 est.
        'fact': 'New York City is home to the United Nations Headquarters.'
    },
    'Paris': {
        'country': 'France',
        'population': 2_100_000,         # Paris proper, 2023 est.
        'fact': 'Paris is known as the "City of Light" and was one of the first European cities to adopt street lighting.'
    }
}
for city, info in cities.items():
    print(f"{city} is the city of {info['country']}, and the population of {city} is {info['population']}, {info['fact']}")
