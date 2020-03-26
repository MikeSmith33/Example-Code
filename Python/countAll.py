def count_dict(mystring):
    d = {}
# count occurances of character
    for w in mystring: 
        d[w] = mystring.count(w)
# print the result
    for k in sorted(d):
        print (k + ': ' + str(d[k]))

mystring='qwertyqweryyyy'
count_dict(mystring)

# The output:

# e: 2
# q: 2
# r: 2
# t: 1
# w: 2
# y: 5


# at  :: 23
# this  :: 43
# test  :: 43
# hello  :: 56
 
# Sort dictionary by value desc
# Create a list of tuples sorted by index 1 i.e. value field     
listofTuples = sorted(wordsFreqDict.items() , reverse=True, key=lambda x: x[1])
 
# Iterate over the sorted sequence
for elem in listofTuples :
    print(elem[0] , " ::" , elem[1] )    

# hello  :: 56
# test  :: 43
# this  :: 43
# at  :: 23