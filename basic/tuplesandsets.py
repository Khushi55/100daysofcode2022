#tuples
#They are like lists (sequence of objects) but they are immutable i.e. once they have been defined we cannot change them.
#Parenthesis in tuples are optional.


marks=21,37,38,49,26,59
marks=(21,37,38,49,26,59)
print(marks[0]==34)
print(marks.count(26))
print(marks.index(26))



#Sets
#Sets are a collection of all unique elements.
#Indexing is not supported in sets.

marks={45,43,65,74,34,67}  # random sequence of output
print(marks)

for score in marks:
    print(score)
