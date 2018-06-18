import random
global o
global val
p1score=0
p2score=0
switch=2
p1_getin=False
p2_getin=False
val=0
def pl1():
    global switch,x
    switch=1
    print p1,"Your score is ",p1score
    x=input("Press 1 to roll dice: ")
    if x==1:
        roll_dice()
    else:
        exit()
def pl2():
    global switch,y
    switch=2
    print p2,"Your score is ",p2score
    y=input("Press 1 to roll dice: ")
    if y==1:
        roll_dice()
    else:
        exit()

def switchplayers():

    global switch
    if switch==2:
        pl1()
    if switch==1:
        pl2()
    




def roll_dice():
    global l
    l=[random.randint(1,6) for i in range(1,6)]
    print l
    no_of_times()

def no_of_times():
    global n1,n2,n3,n4,n5,n6,l,n
    n1=l.count(1)
    n2=l.count(2)
    n3=l.count(3)
    n4=l.count(4)
    n5=l.count(5)
    n6=l.count(6)
    n=[n1,n2,n3,n4,n5,n6]
    calculate()

def calculate():
    global n1,n2,n3,n4,n5,n6,l,n,val
    val=0
    if n1>2:
        val+=1000
        n1=n1-3

    else:
        for i in l:
            if l.count(i)>2:
                val+=100*i
                if i==5:
                        n5=n5-3
                break

    if n5>0:
        for i in range (n5):
                val+=50

    if n1>0:    
        for i in range (0,n1):
            val+=100
  
    n[0]=0
    n[4]=0


    print "Your Score Is ",val

    if val==0 and switch==1:
        p1score=0
        switchplayers()
    if val==0 and switch==2:
        p1score=0
        switchplayers()
    
    decide()
    
def decide():
    global n1,n5,n,p1_getin,p2_getin,p1score,p2score
    global val
    
    
    
    if switch==1 and val>=300 and p1_getin==False:
        p1_getin=True
        print "Player1 you are In!!!"

    if switch==2 and val>=300 and p2_getin==False:
        p2_getin=True
        print "Player2 you are in!!!"

    if switch==1 and p1_getin==True:
        p1score=p1score+val
        next_round()

    if switch==2 and p2_getin==True:
        p2score=p2score+val
        next_round()

    else:
        print val
        switchplayers()


def next_round():
    
     o=raw_input('want to throw another dice?  (Y/N/EXIT)....')
     if o=='Y' or o=='y':
         throw_next()
     if o=='N' or o=='n':
        switchplayers()
     if p1score>=3000:
         print "Congratulations!!! ",p1," you won!"
     if p2score>=3000:
         print "Congratulations!!! ",p2," you won!"

     else:
         next_round()

def throw_next():
    for i in l:
        if i>1 & i<5 & i>5 & l.count(i)==3:
            roll_dice()
            break
        else:
            roll_dice2()
            break

def roll_dice2():
    global n
    total=0
    global l
    for i in n:
        total=total+i
    print "You can throw ",total,"dices!"
    l=[random.randint(1,6) for i in range(total)]
    print l

    no_of_times()

print "*************************************************************************************"

p1=raw_input("Enter Your Name: ")
p2=raw_input("Enter Your Name: ")

switchplayers()
