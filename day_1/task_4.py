print("Input your name, height (in cm), weight (in kg) below")
print('Name? ')
name = input()
print('Height? (in cm)')
height = int(input())
print('Weight? (in kg)')
weight = float(input())


print(f"Your name - {name} and type is {type(name)}.\nYour height is {height} cm and type is {type(height)}. \nYour weight is {weight} kg and type is {type(weight)}.")


# Как проверять тут тип, если я его задаю явно? Если не задаю, то везде будет string