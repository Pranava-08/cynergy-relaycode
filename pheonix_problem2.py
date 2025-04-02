#Pranava Team Pheonix
r={'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000}

def r_to_d(rn:str)->int:
    sum=0
    rn=rn.lower()
    for i in range(len(rn)-1):
        if r[rn[i]]<r[rn[i+1]]:
            sum-=r[rn[i]]
        else:
            sum+=r[rn[i]]
    sum+=r[rn[-1]]
    return sum

def d_to_r(n:int)->str:
    if n>1000 or n<1:
        raise "give number between 1-1000"
    l=[]
    c=0
    while n!=0:
        l.append(n%10*(10**c))
        n=n//10
        c+=1
    r=''
    for i in l[::-1]:
        if len(str(i))==1:
            if i == 1:
                r+='i'
            elif i==2:
                r+='ii'
            elif i==3:
                r+='iii'
            elif i==4:
                r+='iv'
            elif i==5:
                r+='v'
            elif i==6:
                r+='vi'
            elif i==7:
                r+="vii"
            elif i==8:
                r+='viii'
            elif i==9:
                r+='ix'
        elif len(str(i))==2:
            if i == 10:
                r+='x'
            elif i==20:
                r+='xx'
            elif i==30:
                r+='xxx'
            elif i==40:
                r+='xl'
            elif i==50:
                r+='l'
            elif i==60:
                r+='lx'
            elif i==70:
                r+="lxx"
            elif i==80:
                r+='lxxx'
            elif i==90:
                r+='xc'
        elif len(str(i))==3:
            if i ==100:
                r+='c'
            elif i==200:
                r+='cc'
            elif i==300:
                r+='ccc'
            elif i==400:
                r+='cd'
            elif i==500:
                r+='d'
            elif i==600:
                r+='dc'
            elif i==700:
                r+="dcc"
            elif i==800:
                r+='dccc'
            elif i==900:
                r+='cm'        

        elif len(str(i))==4:
            if i == 1000:
                r+='m'
        
    return r
