
import math
nums = [1,2,3,4,1]




def func(nums):


    if(len(nums) <= pow(10,5) ):
       for i in nums:
         if i > pow(10,9):
           print(i)
           print(pow(10,9))
           return
            

    nums.sort()
    for i in range(len(nums) -1):
       if nums[i+1] == nums[i]:
        print('true')
        return             
       else : 
        print('false')


func(nums)

    









