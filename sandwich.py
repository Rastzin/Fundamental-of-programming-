sandwich_orders = ['tuna', 'pastrami', 'cheese', 'pastrami', 'turkey', 'pastrami']
finished_sandwiches = []

print("Sorry, we don't have pastrami today.")

# Remove all pastrami from the list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Make the remaining sandwiches
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print("I made your", sandwich, "sandwich.")
    finished_sandwiches.append(sandwich)

print("\nSandwiches that are ready:")
for sandwich in finished_sandwiches:
    print("-", sandwich)