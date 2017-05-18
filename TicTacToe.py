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
    for k in xrange(3):
        if temp1==3 or temp2==-3:
            print "GAME OVER"
            return True
        temp1=0
        temp2=0
        for h in xrange(3):
            if a[k][h]==1:
                temp1+=1
            elif a[k][h]==-1:
                temp2-=1
    temp1=temp2=0
    for k in xrange(3):
        #print temp1
        #print temp2
        if temp1==3 or temp2==-3:
            print "GAME OVER"
            return True
        temp1=0
        temp2=0
        for h in xrange(3):
            if a[h][k]==1:
                temp1+=1
                #print temp1
            elif a[h][k]==-1:
                temp2-=1
                #print temp2
    temp1=0
    temp2=0
    k=0
    h=0
    while(h!=3):
        if a[h][k]==1:
            temp1+=1
        if a[h][k]==-1:
            temp2-=1
        h+=1
        k+=1
    if (temp1==3 or temp2==-3):
        print "GAME OVER"
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
    if temp1==3 or temp2==-3:
        print "GAME OVER"
        return True
    temp=0
    for h in xrange(3):
        for k in xrange(3):
            if a[k][h]!=0:
                temp+=1
    if temp==9:
        print "GAME OVER"
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
print "Who Makes the First Move?(u/c)"
choice=raw_input()
if(choice=='u'):
    while(Check()!=True):
        print "Make Move"
        i=int(raw_input('i:'))
        j=int(raw_input('j:'))
        a[i][j]=-1
        print a
        if Check()==True:
            print "GAME OVER"
            break
        max_val=np.zeros((3,3,2))
        for k in xrange(3):
            for h in xrange(3):
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
            for h in xrange(3):
                if flag==1:
                    break;
                for k in xrange(3):
                    if max_val[h][k][0]==d or max_val[h][k][1]==d:
                        a[h][k]=1
                        flag=1
                        break;
        if Check()==True:
            print "GAME OVER"
            break
        print a
else:
    flag1=0
    while(Check()!=True):
        if flag1==0:
            h=randint(0,2)
            k=randint(0,2)
            a[h][k]=1
            flag1+=1
            print a
        else:    
            max_val=np.zeros((3,3,2))
            for k in xrange(3):
                for h in xrange(3):
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
                for h in xrange(3):
                    if flag==1:
                        break;
                    for k in xrange(3):
                        if max_val[h][k][0]==d or max_val[h][k][1]==d:
                            a[h][k]=1
                            flag=1
                            break;
            print a
            if Check()==True:
                print "GAME OVER"
                break
        print "Make Move"
        i=int(raw_input('i:'))
        j=int(raw_input('j:'))
        a[i][j]=-1
        print a
        if Check()==True:
            print "GAME OVER"
            break

                
            
        
            
            
