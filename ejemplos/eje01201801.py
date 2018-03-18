#Hallar el número más alto de 5 números y ordenarlos de mayor a menor sin hacer uso de arreglos

n1=int(input("Ingrese un número"))
n2=int(input("Ingrese un número"))
n3=int(input("Ingrese un número"))
n4=int(input("Ingrese un número"))
n5=int(input("Ingrese un número"))

mayor=n1

if(mayor<n2):
    mayor=n2
if(mayor<n3):
    mayor=n3
if(mayor<n4):
    mayor=n4
if(mayor<n5):
    mayor=n5

menor=n1

if(menor>n2):
    menor=n2
if(menor>n3):
    menor=n3
if(menor>n4):
    menor=n4
if(menor>n5):
    menor=n5

p=s=t=c=q=0

#todo con n1
if n1==menor and n2==mayor:
    p=n1
    q=n2
    if n3>n4 and n3>n5:
        c=n3 #n1,____n3,n2
        if n4>n5:
            s=n5
            t=n4 #n1,n5,n4,n3,n2
        if n4<n5:
            s=n4
            t=n5 #n1,n4,n5,n3,n2
    if n3>n4 and n3<n5:
            s=n4
            t=n3
            c=n5 #n1,n4,n3,n5,n2
    if n3<n4 and n3>n5:
            s=n5
            t=n3
            c=n4 #n1,n5,n3,n4,n2
    if n3<n4 and n3<n5:
        s=n3
        if n4>n5:
            t=n5
            c=n4 #n1,n3,n5,n4,n2
        if n4<n5:
            t=n4
            c=n5 #n1,n3,n4,n5,n2

if n1 == menor and n3 == mayor:
    p=n1
    q=n3
    if n2>n4 and n2>n5:
        c=n2 #n1,____n3,n2
        if n4>n5:
            s=n5
            t=n4 #n1,n5,n4,n2,n3
        if n4<n5:
            s=n4
            t=n5 #n1,n4,n5,n2,n3
    if n2>n4 and n2<n5:
            s=n4
            t=n2
            c=n5 #n1,n4,n2,n5,n3
    if n2<n4 and n2>n5:
            s=n5
            t=n2
            c=n4 #n1,n5,n2,n4,n3
    if n2<n4 and n2<n5:
        s=n2
        if n4>n5:
            t=n5
            c=n4 #n1,n2,n5,n4,n3
        if n4<n5:
            t=n4
            c=n5 #n1,n2,n4,n5,n3

if n1 == menor and n4 == mayor:
    p = n1
    q = n4
    if n2 > n3 and n2 > n5:
        c = n2  # n1,____n3,n2
        if n3 > n5:
            s = n5
            t = n3  # n1,n5,n3,n2,n4
        if n3 < n5:
            s = n3
            t = n5  # n1,n3,n5,n2,n4
    if n2 > n3 and n2 < n5:
        s = n3
        t = n2
        c = n5  # n1,n3,n2,n5,n4
    if n2 < n3 and n2 > n5:
        s = n5
        t = n2
        c = n3  # n1,n5,n2,n3,n4
    if n2 < n3 and n2 < n5:
        s = n2
        if n3 > n5:
            t = n5
            c = n3  # n1,n2,n5,n3,n4
        if n3 < n5:
            t = n3
            c = n5  # n1,n2,n3,n5,n4

if n1 == menor and n5 == mayor:
    p = n1
    q = n5
    if n2 > n3 and n2 > n4:
        c = n2  # n1,____n3,n2
        if n3 > n4:
            s = n4
            t = n3  # n1,n4,n3,n2,n5
        if n3 < n4:
            s = n3
            t = n4  # n1,n3,n4,n2,n5
    if n2 > n3 and n2 < n4:
        s = n3
        t = n2
        c = n4  # n1,n3,n2,n4,n5
    if n2 < n3 and n2 > n4:
        s = n4
        t = n2
        c = n3  # n1,n4,n2,n3,n5
    if n2 < n3 and n2 < n4:
        s = n2
        if n3 > n4:
            t = n4
            c = n3  # n1,n2,n4,n3,n5
        if n3 < n4:
            t = n3
            c = n4  # n1,n2,n3,n4,n5

#todo con n2
if n2==menor and n1==mayor:
    p=n2
    q=n1
    if n3>n4 and n3>n5:
        c=n3 #n1,____n3,n2
        if n4>n5:
            s=n5
            t=n4 #n2,n5,n4,n3,n1
        if n4<n5:
            s=n4
            t=n5 #n2,n4,n5,n3,n1
    if n3>n4 and n3<n5:
            s=n4
            t=n3
            c=n5 #n2,n4,n3,n5,n1
    if n3<n4 and n3>n5:
            s=n5
            t=n3
            c=n4 #n2,n5,n3,n4,n1
    if n3<n4 and n3<n5:
        s=n3
        if n4>n5:
            t=n5
            c=n4 #n2,n3,n5,n4,n1
        if n4<n5:
            t=n4
            c=n5 #n2,n3,n4,n5,n1

if n2 == menor and n3 == mayor:
    p=n2
    q=n3
    if n1>n4 and n1>n5:
        c=n1 #n1,____n1,n3
        if n4>n5:
            s=n5
            t=n4 #n2,n5,n4,n1,n3
        if n4<n5:
            s=n4
            t=n5 #n2,n4,n5,n1,n3
    if n1>n4 and n1<n5:
            s=n4
            t=n1
            c=n5 #n2,n4,n1,n5,n3
    if n1<n4 and n1>n5:
            s=n5
            t=n1
            c=n4 #n2,n5,n2,n4,n3
    if n1<n4 and n1<n5:
        s=n1
        if n4>n5:
            t=n5
            c=n4 #n2,n2,n5,n4,n3
        if n4<n5:
            t=n4
            c=n5 #n2,n2,n4,n5,n3

if n2 == menor and n4 == mayor:
    p = n2
    q = n4
    if n1 > n3 and n1 > n5:
        c = n1  # n1,____n3,n2
        if n3 > n5:
            s = n5
            t = n3  # n1,n5,n3,n2,n4
        if n3 < n5:
            s = n3
            t = n5  # n1,n3,n5,n2,n4
    if n1 > n3 and n1 < n5:
        s = n3
        t = n1
        c = n5  # n1,n3,n2,n5,n4
    if n1 < n3 and n1 > n5:
        s = n5
        t = n1
        c = n3  # n1,n5,n2,n3,n4
    if n1 < n3 and n1 < n5:
        s = n1
        if n3 > n5:
            t = n5
            c = n3  # n1,n2,n5,n3,n4
        if n3 < n5:
            t = n3
            c = n5  # n1,n2,n3,n5,n4

if n2 == menor and n5 == mayor:
    p = n2
    q = n5
    if n1 > n3 and n1 > n4:
        c = n1  # n1,____n3,n2
        if n3 > n4:
            s = n4
            t = n3  # n1,n4,n3,n2,n5
        if n3 < n4:
            s = n3
            t = n4  # n1,n3,n4,n2,n5
    if n1 > n3 and n1 < n4:
        s = n1
        t = n1
        c = n4  # n1,n3,n2,n4,n5
    if n1 < n3 and n1 > n4:
        s = n4
        t = n1
        c = n3  # n1,n4,n2,n3,n5
    if n1 < n3 and n1 < n4:
        s = n1
        if n3 > n4:
            t = n4
            c = n3  # n1,n2,n4,n3,n5
        if n3 < n4:
            t = n3
            c = n4  # n1,n2,n3,n4,n5


# todos con n3
if n3==menor and n1==mayor:
    p=n3
    q=n1
    #2,4,5
    if n2>n4 and n2>n5:
        c=n2 #n1,____n3,n2
        if n4>n5:
            s=n5
            t=n4 #n1,n5,n4,n3,n2
        if n4<n5:
            s=n4
            t=n5 #n1,n4,n5,n3,n2
    if n2>n4 and n2<n5:
            s=n4
            t=n2
            c=n5 #n1,n4,n3,n5,n2
    if n2<n4 and n2>n5:
            s=n5
            t=n2
            c=n4 #n1,n5,n3,n4,n2
    if n2<n4 and n2<n5:
        s=n2
        if n4>n5:
            t=n5
            c=n4 #n1,n3,n5,n4,n2
        if n4<n5:
            t=n4
            c=n5 #n1,n3,n4,n5,n2

if n3 == menor and n2 == mayor:
    p=n3
    q=n2
    #1,4,5
    if n1>n4 and n1>n5:
        c=n1 #n1,____n3,n2
        if n4>n5:
            s=n5
            t=n4 #n1,n5,n4,n2,n3
        if n4<n5:
            s=n4
            t=n5 #n1,n4,n5,n2,n3
    if n1>n4 and n1<n5:
            s=n4
            t=n1
            c=n5 #n1,n4,n2,n5,n3
    if n1<n4 and n1>n5:
            s=n5
            t=n1
            c=n4 #n1,n5,n2,n4,n3
    if n1<n4 and n1<n5:
        s=n1
        if n4>n5:
            t=n5
            c=n4 #n1,n2,n5,n4,n3
        if n4<n5:
            t=n4
            c=n5 #n1,n2,n4,n5,n3

if n3 == menor and n4 == mayor:
    p = n3
    q = n4
    if n2 > n1 and n2 > n5:
        c = n2  # n1,____n3,n2
        if n1 > n5:
            s = n5
            t = n1  # n1,n5,n3,n2,n4
        if n1 < n5:
            s = n1
            t = n5  # n1,n3,n5,n2,n4
    if n2 > n1 and n2 < n5:
        s = n1
        t = n2
        c = n5  # n1,n3,n2,n5,n4
    if n2 < n1 and n2 > n5:
        s = n5
        t = n2
        c = n1  # n1,n5,n2,n3,n4
    if n2 < n1 and n2 < n5:
        s = n2
        if n1 > n5:
            t = n5
            c = n3  # n1,n2,n5,n3,n4
        if n1 < n5:
            t = n3
            c = n5  # n1,n2,n3,n5,n4

if n3 == menor and n5 == mayor:
    p = n3
    q = n5
    if n2 > n1 and n2 > n4:
        c = n2  # n1,____n3,n2
        if n1 > n4:
            s = n4
            t = n1  # n1,n4,n3,n2,n5
        if n1 < n4:
            s = n1
            t = n4  # n1,n3,n4,n2,n5
    if n2 > n1 and n2 < n4:
        s = n1
        t = n2
        c = n4  # n1,n3,n2,n4,n5
    if n2 < n1 and n2 > n4:
        s = n4
        t = n2
        c = n1  # n1,n4,n2,n3,n5
    if n2 < n1 and n2 < n4:
        s = n2
        if n1 > n4:
            t = n4
            c = n1  # n1,n2,n4,n3,n5
        if n1 < n4:
            t = n1
            c = n4  # n1,n2,n3,n4,n5

#todo con n4
if n4==menor and n1==mayor:
    p=n4
    q=n1
    #2,4,5
    if n2>n3 and n2>n5:
        c=n2 #n1,____n3,n2
        if n3>n5:
            s=n5
            t=n3 #n1,n5,n4,n3,n2
        if n3<n5:
            s=n3
            t=n5 #n1,n4,n5,n3,n2
    if n2>n3 and n2<n5:
            s=n3
            t=n2
            c=n5 #n1,n4,n3,n5,n2
    if n2<n3 and n2>n5:
            s=n5
            t=n2
            c=n3 #n1,n5,n3,n4,n2
    if n2<n3 and n2<n5:
        s=n2
        if n3>n5:
            t=n5
            c=n4 #n1,n3,n5,n4,n2
        if n3<n5:
            t=n4
            c=n5 #n1,n3,n4,n5,n2

if n4 == menor and n2 == mayor:
    p=n4
    q=n2
    #1,4,5
    if n1>n3 and n1>n5:
        c=n1 #n1,____n3,n2
        if n3>n5:
            s=n5
            t=n3 #n1,n5,n4,n2,n3
        if n3<n5:
            s=n3
            t=n5 #n1,n4,n5,n2,n3
    if n1>n3 and n1<n5:
            s=n3
            t=n1
            c=n5 #n1,n4,n2,n5,n3
    if n1<n3 and n1>n5:
            s=n5
            t=n1
            c=n3 #n1,n5,n2,n4,n3
    if n1<n3 and n1<n5:
        s=n1
        if n3>n5:
            t=n5
            c=n3 #n1,n2,n5,n4,n3
        if n3<n5:
            t=n3
            c=n5 #n1,n2,n4,n5,n3

if n4 == menor and n3 == mayor:
    p = n4
    q = n3
    if n2 > n1 and n2 > n5:
        c = n2  # n1,____n3,n2
        if n1 > n5:
            s = n5
            t = n1  # n1,n5,n3,n2,n4
        if n1 < n5:
            s = n1
            t = n5  # n1,n3,n5,n2,n4
    if n2 > n1 and n2 < n5:
        s = n1
        t = n2
        c = n5  # n1,n3,n2,n5,n4
    if n2 < n1 and n2 > n5:
        s = n5
        t = n2
        c = n1  # n1,n5,n2,n3,n4
    if n2 < n1 and n2 < n5:
        s = n2
        if n1 > n5:
            t = n5
            c = n3  # n1,n2,n5,n3,n4
        if n1 < n5:
            t = n1
            c = n5  # n1,n2,n3,n5,n4

if n4 == menor and n5 == mayor:
    p = n4
    q = n5
    if n2 > n1 and n2 > n3:
        c = n2  # n1,____n3,n2
        if n1 > n3:
            s = n3
            t = n1  # n1,n4,n3,n2,n5
        if n1 < n3:
            s = n1
            t = n3  # n1,n3,n4,n2,n5
    if n2 > n1 and n2 < n3:
        s = n1
        t = n2
        c = n3  # n1,n3,n2,n4,n5
    if n2 < n1 and n2 > n3:
        s = n3
        t = n2
        c = n1  # n1,n4,n2,n3,n5
    if n2 < n1 and n2 < n3:
        s = n2
        if n1 > n3:
            t = n3
            c = n1  # n1,n2,n4,n3,n5
        if n1 < n3:
            t = n1
            c = n3  # n1,n2,n3,n4,n5
#todo con n5

if n5==menor and n1==mayor:
    p=n5
    q=n1
    #2,4,5
    if n2>n3 and n2>n4:
        c=n2 #n1,____n3,n2
        if n3>n4:
            s=n4
            t=n3 #n1,n5,n4,n3,n2
        if n3<n4:
            s=n3
            t=n4 #n1,n4,n5,n3,n2
    if n2>n3 and n2<n4:
            s=n3
            t=n2
            c=n4 #n1,n4,n3,n5,n2
    if n2<n3 and n2>n4:
            s=n4
            t=n2
            c=n3 #n1,n5,n3,n4,n2
    if n2<n3 and n2<n4:
        s=n2
        if n3>n4:
            t=n4
            c=n3 #n1,n3,n5,n4,n2
        if n3<n4:
            t=n3
            c=n4 #n1,n3,n4,n5,n2

if n5 == menor and n2 == mayor:
    p=n5
    q=n2
    #1,3,4
    if n1>n3 and n1>n4:
        c=n1 #n1,____n3,n2
        if n3>n4:
            s=n4
            t=n3 #n1,n5,n4,n2,n3
        if n3<n4:
            s=n3
            t=n4 #n1,n4,n5,n2,n3
    if n1>n3 and n1<n4:
            s=n3
            t=n1
            c=n4 #n1,n4,n2,n5,n3
    if n1<n3 and n1>n4:
            s=n4
            t=n1
            c=n3 #n1,n5,n2,n4,n3
    if n1<n3 and n1<n4:
        s=n1
        if n3>n4:
            t=n4
            c=n3 #n1,n2,n5,n4,n3
        if n3<n4:
            t=n3
            c=n4 #n1,n2,n4,n5,n3

if n5 == menor and n3 == mayor:
    p = n5
    q = n3
    #1,2,4
    if n2 > n1 and n2 > n4:
        c = n2  # n1,____n3,n2
        if n1 > n4:
            s = n4
            t = n1  # n1,n5,n3,n2,n4
        if n1 < n4:
            s = n1
            t = n4  # n1,n3,n5,n2,n4
    if n2 > n1 and n2 < n4:
        s = n1
        t = n2
        c = n4  # n1,n3,n2,n5,n4
    if n2 < n1 and n2 > n4:
        s = n4
        t = n2
        c = n1  # n1,n5,n2,n3,n4
    if n2 < n1 and n2 < n4:
        s = n2
        if n1 > n4:
            t = n4
            c = n3  # n1,n2,n5,n3,n4
        if n1 < n4:
            t = n1
            c = n4  # n1,n2,n3,n5,n4

if n5 == menor and n4 == mayor:
    p = n5
    q = n4
    if n2 > n1 and n2 > n3:
        c = n2  # n1,____n3,n2
        if n1 > n3:
            s = n3
            t = n1  # n1,n4,n3,n2,n5
        if n1 < n3:
            s = n1
            t = n3  # n1,n3,n4,n2,n5
    if n2 > n1 and n2 < n3:
        s = n1
        t = n2
        c = n3  # n1,n3,n2,n4,n5
    if n2 < n1 and n2 > n3:
        s = n3
        t = n2
        c = n1  # n1,n4,n2,n3,n5
    if n2 < n1 and n2 < n3:
        s = n2
        if n1 > n3:
            t = n3
            c = n1  # n1,n2,n4,n3,n5
        if n1 < n3:
            t = n1
            c = n3  # n1,n2,n3,n4,n5











print("El número mayor es: ",mayor)


print("ascendente",p," ",s," ",t," ",c," ",q);

