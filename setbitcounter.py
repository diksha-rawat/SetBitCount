def countsetbit(start,end):
    count=0
    for i in range(initial,end+1):
        c=bin(i)
        binary=c[2:]
        if '1' in binary:
            count+=int(binary.count('1'))       
    return(count)
