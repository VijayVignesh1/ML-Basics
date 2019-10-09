import numpy as np
from random import randint
up=down=left=right=0
#i=int(raw_input())
#j=int(raw_input())
a=np.zeros((3,3))
#a[1][1]=1
def Check():
    temp1=0
    temp2=0
    ## Checking Vertically
    for k in range(3):
        temp1=0
        temp2=0
        for h in range(3):
            if a[k][h]==1:
                temp1+=1
            elif a[k][h]==-1:
                temp2-=1
        if temp1==3:
            print("COMPUTER WINS!!")
            return True
        elif temp2==-3:
            print("YOU WIN!!")
            return True
    temp1=temp2=0
    ## Checking Horizontally
    for k in range(3):
        #print temp1
        #print temp2
        temp1=0
        temp2=0
        for h in range(3):
            if a[h][k]==1:
                temp1+=1
                #print temp1
            elif a[h][k]==-1:
                temp2-=1
                #print temp2
        if temp1==3:
            print("COMPUTER WINS!!")
            return True
        elif temp2==-3:
            print("YOU WIN!!")
            return True
    temp1=0
    temp2=0
    k=0
    h=0
    ## Checking Diagonals
    while(h!=3):
        if a[h][k]==1:
            temp1+=1
        if a[h][k]==-1:
            temp2-=1
        h+=1
        k+=1
    if temp1==3:
        print("COMPUTER WINS!!")
        return True
    elif temp2==-3:
        print("YOU WIN!!")
        return True
    k=0
    h=0
    temp1=temp2=0
    while(h!=3):
        if a[h][k]==1:
            temp1+=1
        if a[h][k]==-1:
            temp2-=1
        h+=1
        k+=1
    temp1=temp2=0
    h=0
    k=2
    while(k!=-1):
        if a[h][k]==1:
            temp1+=1
        if a[h][k]==-1:
            temp2-=1
        h+=1
        k-=1
    temp=0
    for h in range(3):
        for k in range(3):
            if a[k][h]!=0:
                temp+=1
    if temp==9:
        print("GAME DRAWN")
        return True
    if temp1==3:
        print("COMPUTER WINS!!")
        return True
    elif temp2==-3:
        print("YOU WIN!!")
        return True
    return False
ch='y'
def Cost(i,j):
    up=down=left=right=0
    temp1=i
    temp2=j
    while(i<3):
            i+=1
            if((i<0 or j<0) or (i>=3 or j>=3) or a[i][j]==0):
                    break;
            else:
                    down+=a[i][j]
    i=temp1
    j=temp2
    while(j<3):
            j+=1
            if((i<0 or j<0) or (i>=3 or j>=3) or a[i][j]==0):
                    break;
            else:
                    right+=a[i][j]
    #print right
    i=temp1
    j=temp2
    while(i>0):
            i-=1
            if((i<0 or j<0) or (i>=3 or j>=3) or a[i][j]==0):
                    break;
            else:
                    up+=a[i][j]
    i=temp1
    j=temp2
    while(j>0):
            j-=1
            if((i<0 or j<0) or (i>=3 or j>=3) or a[i][j]==0):
                    break;
            else:
                    left+=a[i][j]
    i=temp1
    j=temp2
    #print "up+down",(up+down)
    #print "right+left",(right+left)
    return ((up+down),(right+left))
'''a[1][1]=1
a[0][1]=1
a[2][2]=-1
a[2][1]=-1'''
print("Who Makes the First Move?(u/c)")
choice=input()
if(choice=='u'):
    while(Check()!=True):
        print("Make Move")
        i=int(input('i:'))
        j=int(input('j:'))
        a[i][j]=-1
        print("Table: \n",a)
        if Check()==True:
            #print("GAME OVER")
            break
        max_val=np.zeros((3,3,2))
        for k in range(3):
            for h in range(3):
                if a[k][h]!=0:
                    max_val[k][h]=99
                    continue;
                else:
                    max_val[k][h][0]=Cost(k,h)[0]
                    max_val[k][h][1]=Cost(k,h)[1]
        precedence=[2,-2,1,0,-1,99]
        flag=0
        for d in precedence:
            if flag==1:
                break;
            for h in range(3):
                if flag==1:
                    break;
                for k in range(3):
                    if max_val[h][k][0]==d or max_val[h][k][1]==d:
                        a[h][k]=1
                        flag=1
                        break;
        if Check()==True:
            #print("GAME OVER")
            break
        print("Table: \n",a)
else:
    flag1=0
    while(Check()!=True):
        if flag1==0:
            h=randint(0,2)
            k=randint(0,2)
            a[h][k]=1
            flag1+=1
            print("Table: \n",a)
        else:    
            max_val=np.zeros((3,3,2))
            for k in range(3):
                for h in range(3):
                    if a[k][h]!=0:
                        max_val[k][h]=99
                        continue;
                    else:
                        max_val[k][h][0]=Cost(k,h)[0]
                        max_val[k][h][1]=Cost(k,h)[1]
            precedence=[2,-2,1,0,-1,99]
            flag=0
            for d in precedence:
                if flag==1:
                    break;
                for h in range(3):
                    if flag==1:
                        break;
                    for k in range(3):
                        if max_val[h][k][0]==d or max_val[h][k][1]==d:
                            a[h][k]=1
                            flag=1
                            break;
            print("Table: \n",a)
            if Check()==True:
                #print("GAME OVER")
                break
        print("Make Move")
        while 1:
            i=int(input('i:'))
            j=int(input('j:'))
            if a[i][j]==0.:
                print("Move Made Successfully")    
                a[i][j]=-1
                break
            else:
                print("Move Cannot be Made!! Try another tile..")
        print("Table: \n",a)
        if Check()==True:
            #print("GAME OVER")
            break

                
            
        
            
            
