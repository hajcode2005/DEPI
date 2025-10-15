def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def divide(x,y):
   if y!=0:
    return x/y
   else :
      return "error :can't divide by zero"
print (''' select operation:
            1- addition
            2- subtraction
            3- multiplication
            4- division
         ''') 
print("enter choice (1.2,3,4) or 'exit' to quite: ")
choice=input(" ")    
if choice == '1':
   num1=float(input("enter numbee1:"))
   num2=float(input("enter numbee2:"))
   print("reslult= ",add(num1,num2))
elif choice ==' 2':
   num1=float(input("enter numbee1:"))
   num2=float(input("enter numbee2:"))
   print("reslult= ",sub(num1,num2))
elif choice == '3':
   num1=float(input("enter numbee1:"))
   num2=float(input("enter numbee2:"))
   print("reslult= ",multi(num1,num2))
elif choice == '4':
   num1=float(input("enter numbee1:"))
   num2=float(input("enter numbee2:"))
   input("reslult= ",divide(num1,num2))
elif choice == 'exit':
   print("exiting the calculater .",end='')
   print("goodbye!")