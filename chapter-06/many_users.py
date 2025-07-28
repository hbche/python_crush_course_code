users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': "curie",
        'location': "paris"
    }
}
for username, info in users.items():
    print(f"\nUsername: {username.title()}")
    full_name = f"{info['last']} {info['first']}"
    location = info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")