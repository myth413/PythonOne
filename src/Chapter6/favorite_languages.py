favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

#遍历字典中所有键值对
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

friends = ['phil', 'sarah']

#遍历字典所有KEY，并判断输出
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

#遍历排序后的字典所有KEY
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#遍历字典的所有值，并去重复
for language in set(favorite_languages.values()):
    print(language.title())








[]