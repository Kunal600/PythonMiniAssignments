fname = raw_input('Enter File name')
fhandler = open(fname);
lst = list()
newlist = list()
count = 0
for line in fhandler:
    line  = line.rstrip()
    if not line.startswith('From:'):continue
    lst = line.split()
        #if newlist.count(lst[1]) == 0:
    newlist.append(lst[1])
    count = count + 1 
print  '\n'.join(newlist)    
print "There were",count,"lines in the file with From as the first word"        