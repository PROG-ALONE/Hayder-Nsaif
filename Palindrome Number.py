# input = 121
# output = True
def palin_num(x):
    s,st=str(x),""
    for i in range(len(s)-1,-1,-1): #begins from ladt index of string length=3 
        st+=s[i]
    return (st==s)==True

x=12345
print(palin_num(x))