players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #['charles', 'martina', 'michael'] 切片

print(players[1:4]) #['martina', 'michael', 'florence']

print(players[:4]) #['charles', 'martina', 'michael', 'florence'] 没有指定第一个索引，Python将自动从列表开头开始

print(players[2:]) #['michael', 'florence', 'eli'] 从索引2开始到列表末尾

print(players[-3:]) #['michael', 'florence', 'eli']负数索引返回离列表末尾相应距离的元素

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
'''
Here are the first three players on my team:
Charles
Martina
Michael
'''