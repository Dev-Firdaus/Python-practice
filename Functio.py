#Factorial of a number...
def facto():
    num=int(input("Enetr a number:"))
    f=1
    for i in range(1,num+1):
        f=f*i
        print("Factorial=",f)
facto()


#Power of a number...
def power(base,exponent):
    f=base**exponent
    return f
base=int(input("Enetr a number:"))
exponent=int(input("Enetr the power:"))
f=power(base,exponent)
print("Power is :",f)
power(base,exponent)

#swap of two number...
def SwapNum(a,b):
    s=a
    a=b
    b=s
    print(a,b)

a=int(input("Enetr 1st number:"))
b=int(input("Enetr 2nd number:"))
SwapNum(a,b)
