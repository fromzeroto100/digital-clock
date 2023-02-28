prompt = '\nTell me something and I will repeat it to you: '
prompt += '\nPress "quit" to finish the program'

message = ''
while message != "quit":
    message = input(prompt)
    print(message)