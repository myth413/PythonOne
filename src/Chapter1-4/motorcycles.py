
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati2')
print(motorcycles)

motorcycles.insert(2, 'yaoguang')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + '.')

print(motorcycles)

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + '.')

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove("ducati") #不知道要删除的列表值在那个位置用
print(motorcycles)