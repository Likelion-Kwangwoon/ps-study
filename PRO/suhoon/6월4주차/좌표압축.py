from copy import deepcopy
N = int(input())
nums = list(map(int,input().split()))
nums_2 = deepcopy(nums)
nums = list(set(nums))
nums.sort()
ans = []
#print(nums, nums_2)
def binary_search(start, end ,nums,target  ):
   
    while start <= end:
        middle = (start + end) // 2 
        if nums[middle ] == target:
            return middle
        elif nums[middle] >target:
            end = middle -1
        elif nums[middle] < target:
            start = middle +1
    



for item in nums_2:

    ans.append(binary_search(0, len(nums)-1 , nums , item))


print(*ans)




