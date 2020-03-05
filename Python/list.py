# Adding and Appending

# append(): Used for appending and adding elements to List.It is used to add elements to the last position of List.
# Syntax: 

list.append (element)

# Adds List Element as value of List. 
List = ['Mathematics', 'chemistry', 1997, 2000] 
List.append(20544) 
print(List) 

# Output:
# ['Mathematics', 'chemistry', 1997, 2000, 20544]
 

# insert(): Inserts an elements at specified position.
# Syntax:
# list.insert(<position, element)
# Note: Position mentioned should be within the range of List, as in this case between 0 and 4, elsewise would throw IndexError.

List = ['Mathematics', 'chemistry', 1997, 2000] 
# Insert at index 2 value 10087 
List.insert(2,10087)      
print(List)    

# Output:
# ['Mathematics', 'chemistry', 10087, 1997, 2000, 20544]

# extend(): Adds contents to List2 to the end of List1.
# Syntax:
# List1.extend(List2)

List1 = [1, 2, 3] 
List2 = [2, 3, 4, 5] 
  
# Add List2 to List1 
List1.extend(List2)         
print(List1) 

# Output:
# [1, 2, 3, 2, 3, 4, 5] 
#  
#Add List1 to List2 now 
List2.extend(List1)  
print(List2) 

# Output:
# [2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]

# sum(), count(), index(), min() and max() functions of List

# sum() : Calculates sum of all the elements of List.
# Syntax:
# sum(List)

List = [1, 2, 3, 4, 5] 
print(sum(List)) 

# Output:
# 15

# What happens if numeric value is not used a parameter?
# Sum is calculated only for Numeric values, elsewise throws TypeError.
# See example:

List = ['gfg', 'abc', 3] 

# print(sum(List)) 
# Output:

# Traceback (most recent call last):
#   File "", line 1, in 
#     sum(List)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# count():Calculates total occurrence of given element of List.
# Syntax:
# List.count(element)

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.count(1)) 

# Output:
# 4

# length:Calculates total length of List.
# Syntax:
# len(list_name)

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(len(List)) 

# Output:
# 10

# index(): Returns the index of first occurrence. Start and End index are not necessary parameters.
# Syntax:
# List.index(element[,start[,end]])

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.index(2)) 

# Output:
# 1

# Another example:

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.index(2,2)) 

# Output:
# 4

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
  
# will check from index 2 to 3. 
print(List.index(2,2,4)) 

# Output:
# Traceback (most recent call last):
#   File "", line 1, in 
#     List.index(2,2,4)
# ValueError: tuple.index(x): x not in tuple

# min() : Calculates minimum of all the elements of List.
# Syntax:
# min(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(min(List))

# Output:
# 1.054

# max(): Calculates maximum of all the elements of List.
# Syntax:
# max(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(max(List)) 

# Output:
# 5.33

# sort() and reverse() functions

# reverse(): Sort the given data structure (both tuple and list) in ascending order. Key and reverse_flag are not necessary parameter and reverse_flag is set to False, if nothing is passed through sorted().
# Syntax:
# sorted([list[,key[,Reverse_Flag]]])
# list.sort([key,[Reverse_flag]])

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
  
#Reverse flag is set True 
List.sort(reverse=True)  
  
#List.sort().reverse(), reverses the sorted list   
print(List) 

# Output:
# [5.33, 4.445, 3, 2.5, 2.3, 1.054]


List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
sorted(List) 
print(List) 

# Output:
# [1.054, 2.3, 2.5, 3, 4.445, 5.33]

# Deletion of List Elements
# To Delete one or more elements, i.e. remove an element, many built in functions can be used, such as pop() & remove() and keywords such as del.

# pop(): Index is not a necessary parameter, if not mentioned takes the last index.
# Syntax:
#  list.pop([index])
# Note: Index must be in range of the List, elsewise IndexErrors occurs.

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(List.pop()) 

# Output:
# 2.5

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(List.pop(0)) 

# Output:
# 2.3

# del() : Element to be deleted is mentioned using list name and index.
# Syntax:
# del list.[index]

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
del List[0] 
print(List) 

# Output:
# [4.445, 3, 5.33, 1.054, 2.5]

# remove(): Element to be deleted is mentioned using list name and element.
# Syntax:
#  list.remove(element)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
List.remove(3) 
print(List) 

# Output:
# [2.3, 4.445, 5.33, 1.054, 2.5]