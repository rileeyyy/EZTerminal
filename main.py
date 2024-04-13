from basic import BasicInterpreter
import os
import re

def execute_basic_file(file_path):
    with open(file_path, 'r') as file:
        basic_code = file.read()
        interpreter = BasicInterpreter()
        interpreter.interpret(basic_code)

def evaluate_equation(expression):
    try:
        result = eval(expression)
        print(result)
    except Exception as e:
        print(e)

print("Welcome to EZTerminal Version 1.1!")
def main():
    while True:
        current_path = os.getcwd()
        command = input(f"{current_path}> ")
        if command.lower() in ['exit', 'quit']:
            break
        elif command.lower().startswith('cd '):
            try:
                os.chdir(command[3:])
                print("\n".join(os.listdir()))
            except FileNotFoundError:
                print("Directory not found.")
        elif command.lower() == 'dir':
            print("\n".join(os.listdir()))
        elif command.lower().startswith('md '):
            folder_name = command[3:]
            try:
                os.mkdir(folder_name)
                print(f"Folder '{folder_name}' created.")
            except FileExistsError:
                print(f"Folder '{folder_name}' already exists.")
        elif command.lower().startswith('mf '):
            file_name = command[3:]
            try:
                with open(file_name, 'x'):
                    print(f"File '{file_name}' created.")
            except FileExistsError:
                print(f"File '{file_name}' already exists.")
        elif re.match(r'^[\d+\-*/(). ]+$', command):
            evaluate_equation(command)
        elif command.lower().endswith('.bas'):
            if os.path.isfile(command):
                execute_basic_file(command)
            else:
                print("File not found.")
        else:
            print("Command not recognized.")

if __name__ == "__main__":
    main()
