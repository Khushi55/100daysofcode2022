#range in python
#range() function returns a range object that is a sequence of numbers.

i=range(5)

print(i)

#for loop

for i in range(10):
  i=i+1
  print(i)  #print 1 to 10

for i in range(5):
    print(i)
    i=i+1      #print 0 to 4

for i in range(4):

    i=i+1
    print(i * "*")

for i in range(4):

    i=i-1
    print(i)
for i in range(4):
    i=i-1
    print(i* "*")

#while loop

i=1
while(i<5):

  i=i+1
  print(i)

while(i<5):
  print(i)
  i=i+1
while(i<=5):
    print(i*"*")
    i=i+1

i=1
while(i<=5):
    print(i*"*")
    i=i+1

i=5
while(i>=1):
    print(i*"*")
    i=i-1
