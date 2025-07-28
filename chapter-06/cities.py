prompt = "Please input the name of city you have visited:"
prompt += "\nEnter 'quit' when you are finished."
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I would love to go to {city}")