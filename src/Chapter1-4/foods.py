my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]#复制列表，独立副本

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

'''
My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli']

My friends favorite foods are:
['pizza', 'falafel', 'carrot cake', 'ice cream']
'''