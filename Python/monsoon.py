def monsoon (people,umbrellas):
    umbrellas.sort(reverse=True)
    rtnval = 0
    remainppl = people
    for i in range(len(umbrellas)):
         umbcount = divmod(remainppl,umbrellas[i])
         rtnval = rtnval + umbcount[0]
         if umbcount[1] > 0:
            remainppl = umbcount[1]
    if umbcount[1] > 0:
        rtnval = -1
    print ("rtnval is ",rtnval)

monsoon(7,[1,6,4])
    
     
    