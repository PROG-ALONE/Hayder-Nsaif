# input = "hello world i'm hayder"
# output = "olleh world m'i hayder"

def check_length(st):
    return st if len(st)>1 else False

#first solution
# def reverse_string(st):
#     alist=[]
#     for (index , value) in enumerate(check_length(st.split())):
#         if( index % 2 == False): 
#             alist.append(''.join([value[i] for i in range(len(value)-1,-1,-1)]))
#             # print(value[::-1])  #first way to reverse string but not better 
#             # return alist.append[value[index]]
#         else:alist.append(value)
#     return ' '.join(alist)

#second soluton
def reverse_string(st):
    alist=[]
    ss=list(st.split())
    for i in range(len(ss)):
        sum=""
        if( i % 2 == 0): 
            for j in range(len(ss[i])-1,-1,-1):   # using External for
                # alist.append(''.join([ss[i][j] for j in range(len(ss[i])-1,-1,-1)]))        # using inline for
                sum+=ss[i][j]
            alist.append( sum )
        else:alist.append( ss[i] )
    return ' '.join(alist)
    
#####        MAIN       #####
st="hello world i'm hayder"
print(reverse_string(st))