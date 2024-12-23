print()

state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}

print("Captials:")
for state in state_capitals:
    print(state)                                    #Washington...

print("\nCities:")
for city in state_capitals.values():
    print(city)                                     #Olympia

print()

for state in state_capitals:
    print(state_capitals[state], "is the capital of", state)

print()
for state, city in state_capitals.items():
    print(city, "is the capital of", state)         #same as the 3rd for loop