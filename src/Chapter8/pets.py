#位置实参 调用函数多次
def describe_pet(animal_type, pet_name):
    #显示宠物信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

def describe_pet2(pet_name, animal_type='dog'): #先列出没有默认值的形参
    #显示宠物信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#关键字实参
describe_pet(animal_type='cat', pet_name='mike')
describe_pet(pet_name='john', animal_type='bird')
describe_pet2(pet_name='CC', animal_type='hamster') #由于显示地给animal_type提供了实参，因此将忽略这个形参的默认值

'''
Result:
I have a hamster.
My hamster's name is Harry.

I have a dog.
My dog's name is Willie.

I have a cat.
My cat's name is Mike.

I have a bird.
My bird's name is John.

I have a hamster.
My hamster's name is Cc.
'''