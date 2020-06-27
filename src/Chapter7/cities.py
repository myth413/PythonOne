prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you  are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break #跳出循环
    else:
        print("I'd love to go to " + city.title() + "!")

'''
Please enter the name of a city you have visited:
(Enter 'quit' when you  are finished.)New York
I'd love to go to New York!

Please enter the name of a city you have visited:
(Enter 'quit' when you  are finished.)San Francisco
I'd love to go to San Francisco!

Please enter the name of a city you have visited:
(Enter 'quit' when you  are finished.)quit
'''