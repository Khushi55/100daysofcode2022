#lets build a calculator

num1=input("Enter 1st number:")
num2=input("Enter 2nd number:")

num1=int(num1)
num2=int(num2)

operator=input("Enter operator:")  #(input from keyboard symbol of operator)


if operator=='+':
  print("sum=" ,num1+num2)

elif operator=='-':
    print("sub=" ,num1-num2)

elif operator=='*':
    print("mul=" ,num1*num2)

elif operator=='/':
    print("div=" ,num1/num2)

elif operator=='%':
    print("mod=" ,num1%num2)

else:
    print("wrong operation")
    print("Sorry!")

