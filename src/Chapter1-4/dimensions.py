dimensions = (200, 50) #元组，一系列不可修改的元素
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

'''
Original dimensions:
200
50

Modified dimensions:
400
100
'''
