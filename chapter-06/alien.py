# alien_0 = {
#     "color": 'red',
#     'points': 5
# }
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}
# alien_0['color'] = 'red'
# alien_0['points'] = 5
# print(alien_0)

# alien_0 = {
#     'color': 'red'
# }
# print(f"The alien is {alien_0['color']}")
# alien_0['color'] = 'yellow'
# print(f"The alien is {alien_0['color']}")

# alien_0 = {
#     "x_position": 0,
#     'y_position': 25,
#     "speed": 'medium'
# }
# alien_0['speed'] = 'slow'
# print(f"Original position: {alien_0['x_position']}")
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] += x_increment
# print(f"New position: {alien_0['x_position']}")

alien_0 = {
    'color': 'red',
    'points': 5
}
print(alien_0)
del alien_0['points']
print(alien_0)