fname = raw_input("Enter file name: ")
count = 0 
value = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
   # print line
    pos = int(line.find(':') + 1)
    newLine = line[pos:]
    newLine =  newLine.strip()
    print newLine
    value = value + float(newLine)
    count = count + 1  
print "Done"
print "Average spam confidence: ",value/count