#Program to calculate person Salary
Hours = raw_input("Enter Hours:")
Rate  = raw_input("Enter Rate:")
if float(Hours) > 40.0:
    over = float(Hours) - 40.0
    Pay = 40.0 * float(Rate) + float(over) * 1.5 * float(Rate)
    print 'Pay:',Pay
else:
     Pay = 40.0 * float(Rate) + float(over)
     print 'Pay:',Pay