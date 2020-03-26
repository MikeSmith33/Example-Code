def countSignals(frequencies, filterRanges):
    minval = 0
    maxval = 0
    cntr = 0
    for i in range(len(filterRanges)):
        for j in range(len(filterRanges[i])):
            if j == 0:
                if filterRanges [i] [j] > minval:
                    minval = filterRanges [i][j]
            else:
                if maxval == 0:
                    maxval = filterRanges [i][j]
                else:
                    if filterRanges[i][j] < maxval:
                        maxval = filterRanges[i][j]
    for k in range(len(frequencies)):
        if minval <= frequencies[k] <= maxval:
            cntr += 1
    return cntr