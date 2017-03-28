def Operation(args):
    a = 3
    b = 5
    if args == '+':
     print a + b
    if args == '-':
     print a - b
    
opr =  raw_input('Enter the operation you want to perform:')   
Operation(opr)


