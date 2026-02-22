def twosum(nums:list[int],target:int)->list[int]:
    seen={}
    for i in range(len(nums)):
        s=target-nums[i]
        if s in seen:return [seen[s],i]
        seen[nums[i]]=i
        # print(seen)
    return []

nums=[-1,-2,-3,-4,-5]
target=-8
result=twosum(nums,target)
print(result) 