def func(nums,k):
    
    n = len(nums) 
    sum_ = 0 
    for i in range(k):
        sum_ += nums[i] 

    for j in range(k,n):
        tmp = sum_ - nums[j-k] + nums[j]
        sum_ = max(sum_,tmp)
        
    return sum_/k
        