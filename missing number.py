# input = [1,2,3,8,10]
# output = ['4','5','6','7','9']    or [4,5,6,7,9]
def mis_number(l):
    n = 0
    a = []
    for i in range(min(l), max(l)):
        if(i not in l):
            a.insert(n, i)
            n += 1
    if n:
        return a
    else:
        return "Not Find Missing Number"


l = [1, 2, 3, 8, 10,]
s = ""
# for j in mis_number(l):
    # if str(j).isnumeric():
    #     print(j)
    # else:
    # s += str(j)+' '
print(mis_number(l))
# for j in range(len(mis_number(l))):print(mis_number(l)[j]) # print the result using index of items
