
def counterlist(sales,sizes):
    totsales = 0
    for i in range(len(sales)):
        try:
            if sizes.index(sales [i][0]) > 0: 
                totsales += sales[i][1]
                sizes.remove(sales [i][0])
        except ValueError:
            totsales += 0
    print(totsales)

counterlist([[6,55],[6,45],[6,55],[4,40],[18,60],[10,50]],[2,3,4,5,6,7,6,5,18])