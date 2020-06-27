def get_formatted_name(first_name, last_name):
    #返回整洁的名字
    full_name = first_name + ' ' + last_name
    return full_name.title()

def get_formatted_name2(first_name, last_name, middle_name=''): #让实参变得可选
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    #返回整洁的名字
    return full_name.title()

musician = get_formatted_name('jimi', 'hendri')
print(musician)

musician = get_formatted_name2('jimi', 'hendri')
print(musician)

musician = get_formatted_name2('john', 'hooker', 'lee')
print(musician)
'''
Result:
Jimi Hendri
Jimi Hendri
John Lee Hooker
'''