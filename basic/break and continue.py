#break and continue

"""
this is multiline
comment
"""

students=['ram','shyam','ghanshyam','radheshyam']

for i in students:
    if i=='ghanshyam':
      break
    print(i)

for i in students:
    if i=='shyam':
        continue
    print(i)

students = ["ram", "shyam", "kishan", "radha", "radhika"]

for student in students:
   if(student == "radha"):
       break
   print(student)

for student in students:
   if(student == "kishan"):
       continue
   print(student)
#


#print the no when no is greater than 100
while(1):
  i=int(input("enter the number"))

  if i<100:
    continue
  else:
   print("congrutulation")
   break