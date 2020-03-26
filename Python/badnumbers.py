def badnumbers(lower,upper,inlist):
    inlist.append(lower)
    inlist.append(upper)
    inlist.sort()
    diffval = 0
    for i in range(len(inlist) -1):
        if (inlist [i] >= lower) and (inlist [i+1]) <= upper:
            if (inlist [i +1]) - (inlist [i]) > diffval:
                diffval = (inlist [i+1]) - (inlist [i])
    print (diffval)

badnumbers(10,30,[3,9,12,17, 22, 31])
