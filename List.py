fname = raw_input('Enter File name')
fhandler = open(fname);
lst = list()
newlist = list()
for line in fhandler:
    line  = line.rstrip()
    lst = line.split()
    for i in range(len(lst)):
    
        if lst.count(lst[i]) == 1:
            if newlist.count(lst[i]) ==0: 
                newlist.append(lst[i])
newlist.sort()
print newlist            
            
             