state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}
#print(len(state_capitals))

print(state_capitals["Washington"])         #Olympia

state_capitals["Washington"] = "Aberdeen"
state_capitals["Texas"] = "Austin"
print(state_capitals)                       #{'Washington': 'Aberdeen', 'Oregon': 'Salem', 'California': 'Sacramento', 'Texas': 'Austin'}

del state_capitals["California"]
print(state_capitals)                       #{'Washington': 'Aberdeen', 'Oregon': 'Salem', 'Texas': 'Austin'}

removed_capital = state_capitals.pop("Oregon")
print(state_capitals)                       #{'Washington': 'Aberdeen', 'Texas': 'Austin'}
print(removed_capital)
