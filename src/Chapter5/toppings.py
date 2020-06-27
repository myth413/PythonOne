requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_topping = ['mushrooms', 'etra cheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
elif 'etra cheese' in requested_topping:
    print("Adding etra cheese.")

print("\nFinished making your pizza")

'''
Adding mushrooms.

Finished making your pizza
'''

requested_topping = []
if requested_topping:
    print("Empty")
else:
    print("Full")
