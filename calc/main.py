from art import logo

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2



operation = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div,
}


def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  stop = False
  
  while not stop:
    
    num2 = float(input("What's the next number?: "))
    for i in operation:
      print(i)
    
    operation_symbol  = input("Pick an operation from the line above: ")
  
    calculation_function = operation[operation_symbol]
    answer = calculation_function(num1, num2)
    print(answer)
    option = input("Type 'y' to continue calculating with 16, or type 'n' to exit: ")
    if option == "y":
      num1 = answer
    else:
      stop = True
      calculator()

calculator()
