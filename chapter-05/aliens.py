# alien_0 = { 'color': 'green','points': 5 }
# alien_1 = { 'color': 'yellow', 'points': 10 }
# alien_2 = { 'color': 'red', 'points': 15 }
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

aliens = []
# 批量生成
for alien_num in range(30):
    if alien_num < 2:
        aliens.append({'color': 'yellow', 'points': 10, 'speed': 'medium'})
    else:
        aliens.append({'color': 'green', 'points': 5, 'speed': 'slow'})
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'mdeium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
# 显示前5个
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示外星人总数
print(f"Total number of aliens: {len(aliens)}")