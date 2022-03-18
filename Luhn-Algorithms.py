# 1-input 15 numbers of credit card
# 2-if index is even sum_even it else number multiple 2 if number greater or equal 10 subtract 9 else sum_odd
# 3 - then sum all of summations and if the summation divide 10 without any more return 1 or true else false or 0

# Solution 1:
# def Luhn_algorithm(card):
#     sum_even,sum_odd=0,0
#     samelist=' '.join(card).split(' ')
#     list_card=list(map(int,samelist))
#     list_even=list()
#     for index in range(len(list_card)):
#         if index % 2 == True:  sum_even+=list_card[index]
#         else:
#             list_even.append(list_card[index] * 2)
#     for check in list_even:
#         if check >= 10 :
#             check=check-9
#         sum_odd+= check
#     return (sum_odd + sum_even) % 10 == False

# Solution 3:
def Luhn_algorithm(Num_card):
    sum_even, sum_odd = 0, 0
    samelist = ' '.join(Num_card).split(' ')    #join 1 2 3 4 5  and then split recording to space then put in list
    list_card = list(map(int, samelist))   #the list will be string so map(convert to int,list i used it) put in list of int
    for index in range(len(list_card)):
        if index % 2 == True:
            sum_even += list_card[index]
        else:
            check = list_card[index] * 2
            if check >= 10:
                check -= 9
            sum_odd += check
    return (sum_odd + sum_even) % 10 == False

######    MAIN    ######
# card = "5560593098175339"
Num_card = "4137894711755904"
print(Luhn_algorithm(Num_card))
