prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

'''
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program.Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program.Hello again
Hello again

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program.quit
'''