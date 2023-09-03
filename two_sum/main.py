# 1. Given an array of integers and a target of the sum
# 2. No repeat of elements to sum
# 3. Output will be a list containing the index of two number which sum match the target

nums = [3,3]
target = 6
    

def twoSum(nums, target):
    num_set = set()
    pairs = []
    for i in range(len(nums)):
        if nums[i] not in num_set:
            complement = target - nums[i]
            num_set.add(complement)
        else:
            complement = target- nums[i]
            pairs.append(nums.index(complement))
            pairs.append(i)

    return pairs
        

twoSum(nums, target)



    
    