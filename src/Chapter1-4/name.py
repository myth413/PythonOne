name = "ada lovelace"
#title() 以首字母大写的方式显示每个单词
print(name.title())

#title() 以字母大写的方式显示每个单词
print(name.upper())

#title() 以字母小写的方式显示每个单词
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hellow, " + full_name.title() + "!"
print(message)

# \t代表制表符 tab
print("\tPython")
# \n代表换行
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = ' Python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()
