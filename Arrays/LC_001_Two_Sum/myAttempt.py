def twosum(nums:list[int],target:int)->list[int]:
      b=1
      a=0
      i=0
      while (a<len(nums) ):
           print("i:",i)
           i+=1
           if b >= len(nums):   # b ran out → move a forward, reset b
             a += 1
             b = a + 1;print("hi")
        #    if nums[a]>target :
        #        a+=1
        #        continue 
           sum=nums[a]+nums[b]
           print(sum)
           if sum>target or sum<target : 
               b+=1
               print("B:",b)
          
           else : return [a,b]           

      return [0,0]

result=twosum([-1,-2,-3,-4,-5],-8)
# for x in result:print(x)
print(result)