current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue #跳出单次循环
    print(current_number)

'''
1
3
5
7
9
'''