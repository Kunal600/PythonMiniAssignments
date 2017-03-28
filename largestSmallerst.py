smallest = None
largestsofar = -1
sum = 0
while True:
    try:
        num = raw_input("Enter a number: ")
       
        if num == "done" :
            print 'Maximum is',largestsofar
            print 'Minimum is',smallest 
            break
        else:
            num = int(num)
    except:
        print('Invalid input')
        continue
        
    
        
    sum = sum + num
    if num > largestsofar:
        largestsofar =  num
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

