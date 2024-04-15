import os
import re

class BasicInterpreter:
  def __init__(self):
      self.symbol_table = {}

  def interpret(self, code):
      lines = code.split("\n")
      for line in lines:
          line = line.strip()
          if line:
              self.execute_line(line)

  def execute_line(self, line):
      parts = line.split(" ")
      line_number = int(parts[0])
      statement = " ".join(parts[1:])
      if statement.startswith("PRINT"):
          self.print_statement(statement)
      elif statement.startswith("LET"):
          self.assign_variable(statement)
      elif statement == "END":
          return
      else:
          print(f"Syntax error: {statement}")

  def print_statement(self, statement):
      value = statement[6:].strip()
      if value.startswith('"') and value.endswith('"'):
          print(value[1:-1])
      elif value.isdigit():
          print(value)
      elif value in self.symbol_table:
          print(self.symbol_table[value])
      else:
          print("Undefined variable:", value)

  def assign_variable(self, statement):
      parts = statement.split("=")
      var_name = parts[0][4:].strip()
      value = parts[1].strip()
      if value.isdigit():
          self.symbol_table[var_name] = int(value)
      elif value in self.symbol_table:
          self.symbol_table[var_name] = self.symbol_table[value]
      else:
          print("Syntax error in LET statement.")

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

def print_welcome_message():
    print("Welcome to EZTerminal Version 1.2!")

def main():
    print_welcome_message()
    while True:
        current_path = os.getcwd()
        command = input(f"{current_path}> ")
        if command.lower() == 'clr':
            os.system('cls' if os.name == 'nt' else 'clear')
            print_welcome_message()
        elif command.lower() == 'hlp':
            print('\n cd [folder] - change directory\n cd .. - put the directory to the parent folder\n dir - shows the files\n md [name] - makes a folder\n mf [filename] - makes a file\n [any math equation] - does math\n clr - clears the screen\n echo [string] - "echos" your text\n win [command] - executes your command via windows cmd (eg. title blahblah)\n hlp - displays this message\n if - ????\n [filename.bas] - executes a basic file\n exit or quit - quits\n')
          
        elif command.lower() == 'if':
            print("if youd like to make a call, please hang up and try again, if you need help hang up and dial your ooperatorrrrr")
        elif command.lower() in ['exit', 'quit']:
            break
        elif command.lower().startswith('win '):
            os.system(command[4:])
        elif command.lower().startswith('echo '):
            print(command[5:])
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
