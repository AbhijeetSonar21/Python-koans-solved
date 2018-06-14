import random

a=random.randint(1,6)
b=random.randint(1,6)
c=random.randint(1,6)
d=random.randint(1,6)
e=random.randint(1,6)


l=[a,b,c,d,e]
print l

x=0
y=0
z=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
f=0
g=0
h=0
if l.count(1)==3:
    x=1000

if l.count(2)<=2 & l.count(3)<=2 & l.count(4)<=2 & l.count(6)<=2:
    y=0

if l.count(1)==1:
    s=100

if l.count(1)==2:
    t=200

if l.count(1)==4:
    u=1100

if l.count(1)==5:
    v=1200
if l.count(2)==3:
    z=200

if l.count(3)==3:
    p=300

if l.count(4)==3:
    q=400

if l.count(5)==3:
    r=500

if l.count(5)==1:
    w=50

if l.count(5)==2:
    f=100

if l.count(5)==4:
    g=550

if l.count(5)==5:
    h=600

sum_of_points=v+u+t+s+x+y+z+p+q+r+w+f+g+h

if sum_of_points==0:
    print "Unfortunately You Lost!!! :("
else:
    print "Wow!!!! Your Score is: ",sum_of_points

