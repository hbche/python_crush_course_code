# alien_0 = {'color': 'green','points': 5}
# alien_1 = {'color': 'yellow','points': 10}
# alien_2 = {'color': 'red','points': 15}
# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# 创建一个用于存储外星人的列表
aliens = []

# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 修改前三个外星人的颜色、速度、得分
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")