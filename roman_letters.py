roman={
    'i':1,
    'v':5,
    'x':10,
    'l':50
}

a=input("Enter roman number:\n")

val=0
prev=0
for i in range(len(a)-1,-1,-1):
    temp=roman[a[i]]
    if(i!=len(a)-1):
        if(roman[a[i+1]]>temp):
            val-=2*temp
    val+=temp

print(val)
