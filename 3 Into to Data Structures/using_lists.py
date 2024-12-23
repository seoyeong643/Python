states = ["Washington", "Oregon", "California"]

print(states[0])
print(states[1])
print(states[2])

print("\nprint backwards:")
print(states[-1])
print(states[-2])
print(states[-3])
print()

states[2] = "Arizona"
print(states)

print(f"\nlength of the list is: {len(states)}\n")

print("Append New York:")
states.append("New York")
print(states)

print("\npop:")
states.pop()
print(states)

states.pop(1)
print(states)