# input = [3,2,4]
# target=6
# output = [1,2]
# def twosum(nums, target):
#     for i in range(len(nums)):
#         for j in range(len(nums[1:])):
#             if(nums[i]+nums[j] == target):
#                 return {i, j}
#     return [2]

def twosum(nums,target):
    a =[]
    for i in range(len(nums)):
        x = target - nums[i]
        if x in a:
            return [a.index(x),i]
        else:
            a.append(nums[i])

# def twosum(nums, target):
#     for i in range(0, len(nums)):
#         if ((target - nums[i]) in nums[0:i]) and (i != nums.index(target - nums[i])):
#             return nums.index(target - nums[i]),i
#     # return i, nums.index(target - nums[i])


a = [3,2,4]
target = 7
# for i in twosum(a, target):
print("the index : ", twosum(a,target))

