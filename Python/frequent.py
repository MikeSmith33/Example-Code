def frequent(arr):
    newdict = {}
    cntr = 0
    element = ''
    for indval  in arr:
        newdict[indval] = newdict.get(indval,0) + 1
        if newdict[indval] >= cntr:
            cntr = newdict[indval]
            element = indval
    print('Element is ', element)
    print('Cntr is', cntr)

frequent([2, 1, 2, 2, 1, 3])