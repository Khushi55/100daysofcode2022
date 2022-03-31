#list

friends=['amar','akabar','anthony']
print(friends[0])
print(friends[1])
print(friends[-1])
print(friends[-2])
print(friends[-3])
print(friends[2])


friends[0]='aman'
print(friends)

print(friends[0:2])

for i in friends:
    print(i)

#list methods

marks=['english', 87, 'maths', 98]
print(marks)
marks.append('physics')
marks.append(89)
print(marks)

marks.insert(0,'chemistry')
marks.insert(1,99)
print(marks)

print('maths' in marks)
print(len(marks))
print(len(marks)/2)



i=0
while i<len(marks):
    print((marks[i]))
    print((marks[i+1]))
    i=i+2




