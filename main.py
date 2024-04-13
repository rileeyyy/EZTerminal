from basic import BasicInterpreter
import os

def execute_basic_file(file_path):
    with open(file_path, 'r') as file:
        basic_code = file.read()
        interpreter = BasicInterpreter()
        interpreter.interpret(basic_code)

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
        elif command.lower().endswith('.bas'):
            if os.path.isfile(command):
                execute_basic_file(command)
            else:
                print("File not found.")
        else:
            print("Command not recognized.")

if __name__ == "__main__":
    main()
