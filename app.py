from modules.model import Model

model = Model()

while True:
    command = input("Enter your command: ")
    respond = model.process(command)
    if respond[0]:
        print(respond[1])
