#Program to calculate person Salary
try:
	Hours = raw_input("Enter Hours:")
	Hours = float(Hours)
	Rate  = raw_input("Enter Rate:")
	Rate  = float(Rate)	
	
except:
	print "Please enter a numeric value"
	quit()

if float(Hours) > 40.0:
		over = float(Hours) - 40
		print 'Over Tracked:',over 
		print 'Calculating Pay1...'
		Pay = 40.0 * float(Rate) + over * 1.5 * float(Rate)
		print "Over Pay:",Pay
elif float(Hours) <= 40.0:
		print 'Entered Hours:', Hours
		print 'Calculating Pay2...'
		Pay = float(Hours) * float(Rate)
		print "Regular Pay:",Pay	