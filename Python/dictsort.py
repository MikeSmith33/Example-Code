def dictsort(arr):
    newdict = {}
    tuples = []
    for indval  in arr:
        newdict[indval] = newdict.get(indval,0) + 1
    tuples = sorted(newdict.items(), key=lambda x: (-x[1], x[0]))    
    print(tuples [0][0])
    
dictsort([2, 1, 2, 2, 1, 3, 1])