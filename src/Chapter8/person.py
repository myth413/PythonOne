def build_person(first_name, last_name):
    #返回一个字典，包含有关一个人的信息
    person = {'first':first_name, 'last':last_name}
    return person

musician = build_person('jimi', 'handrix')
print(musician)

'''
Result:
{'first': 'jimi', 'last': 'handrix'}
'''