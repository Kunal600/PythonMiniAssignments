def computepay(h,r):
    Hours = h
    Rate  = r
    if float(Hours) > 40.0:
        over = float(Hours) - 40.0
        Pay = 40.0 * float(Rate) + float(over) * 1.5 * float(Rate)
        return Pay
    else:
        Pay = 40.0 * float(Rate) + float(over)
        return Pay

hours = raw_input("Enter Hours:")
Rate  = raw_input("Enter Rate:")
p = computepay(hours,Rate)
print "Pay",p