# Assignment1
def myAdd(n1,n2):
    print(n1+n2)
def mySub(n1,n2):
    print(n1-n2)
def myMul(n1,n2):
    print(n1*n2)
def myDiv(n1,n2):
    print(n1/n2)
n1=int(input("Please enter your first integer:"))
op1=input("Choose your first operator from the following(+,-,*,/):")
n2=int(input("Please enter your second integer:"))
op2=input("Choose your second operator from the following(+,-,*,/):")
n3=int(input("Please enter your third integer:"))
print("Entered expression",n1,op1,n2,op2,n3)

if op1=='+':
    myAdd(n1,n2)  #Introduce r1=n1+2
if op2=='+':
    myAdd(n2,n3)    #r1,n3
if op1=='-':
    mySub(n1,n2)
if op2=='-':
    mySub(n2,n3)
if op1=='*':
    myMul(n1,n2)    
if op2=='*':
    myMul(n2,n3)    
if op1=='/':
    myDiv(n1,n2)
if op2=='/':
    myDiv(n2,n3)    