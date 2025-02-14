#input
print("================================================================")
h=int(input("ingrese la altura: "))
print("================================================================")

#processing
q=h/5
n=0
while h>=q:
    h=0.9*h
    n=n+1
#output
print("================================================================")
print("los rebotes al alcanzar la quinta parte de la altura es: "+str(n))
print("================================================================")
