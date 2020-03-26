from collections import Counter

def counterdict(sales,sizes):
    totsales = 0
    sizescnt = Counter(sizes) 
    for i in range(len(sales)):
       if sales [i][0] in sizescnt:
           if sizescnt[sales[i][0]] > 0:   
               totsales += sales[i][1]
               sizescnt[sales[i][0]] -= 1 
    print(totsales)

counterdict([[6,55],[6,45],[6,55],[4,40],[18,60],[10,50]],[2,3,4,5,6,7,6,5,18])
