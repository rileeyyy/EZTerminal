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
