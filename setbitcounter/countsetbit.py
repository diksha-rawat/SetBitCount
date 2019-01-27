def countset(start,end=0):
    count=0
    if end==0:
        c=bin(start)
        binary=c[2:]
        if '1' in binary:
            count+=int(binary.count('1'))
    else:
        for i in range(start,end+1):
            c=bin(i)
            binary=c[2:]
            if '1' in binary:
                count+=int(binary.count('1'))       
    return(count)

