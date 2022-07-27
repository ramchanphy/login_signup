# q=int(input("enter:"))
# unit=100
# b=q*unit
# if b>1000:
#     a=10/100*b
#     print(b-a)
# quantity=int(input("enter the quantity"))
# unit=100
# a=quantity*unit
# if a>1000:
#     discount=10/100*a
#     print(a-discount)
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
if a>b and a>c:
    if b>c:
        print("a is young","\n","b is younger","\n","c is the youngest")
if a>b and a>c:
    if c>b:
        print("a is young","\n","c is younger","\n","b is the youngest")
if b>a and b>c:
    if c>a:
        print("b is young","\n","c is younger","\n","a is the youngest")
if b>a and b>c:
    if a>c:
        print("b is young","\n","a is younger","\n","c is the youngest")
if c>a and c>b:
    if a>b:
        print("c is young","\n","a is younger","\n","b is the youngest")
if c>a and c>b:
    if b>a:
        print("c is young","\n","b is younger","\n","a is the youngest")