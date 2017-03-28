score = raw_input("Please Enter Score between 0.0 and 0.9: ")

if float(score) > 0.0 and float(score) < 1.0:
    if float(score)>= 0.9:
        print 'A'
    elif float(score)>= 0.8:
        print 'B' 
    elif float(score)>= 0.7:
        print 'C' 
    elif float(score)>= 0.6:
        print 'D' 
    elif float(score) < 0.6:
        print 'E'    
else:
    print('Please enter value within range')



