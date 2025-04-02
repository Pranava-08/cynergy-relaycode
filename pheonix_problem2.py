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
    l=[]
    c=0
    while i!=0:
        l.append(i%10*(10**c))
        i=i//10
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


        elif len(str(i))==3:
            if i ==100:
                r+='c'        

        elif len(str(i))==4:
            if i == 1000:
                r+='m'
    return r

