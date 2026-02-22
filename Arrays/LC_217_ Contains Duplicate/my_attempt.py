def containsDuplicate(nums: list[int]) -> bool:
     
        #solution-1
        #  snums=sorted(nums)
        #  for i  in range(len(nums)-1):
        #          if snums[i]==snums[i+1]:return True
        """  
        TE->O(n*Log(n))
        SE->O(1)
       
        """

        #solution-2
        #  seen={}
        #  j=0
        #  for i in nums:
        #          if i in seen.values():
        #                 print("if i",i)
        #                 print("if seen:",seen)
        #                 return True
        #          else: 
        #                  seen[j]=i
        #                  print("else seen:",seen)
        #                  j+=1
                         
        """ 
        TE->O(n^2)
        SE->O(n)
        """
         #final optimal Solution
        """ 
          TE->O(n)
          SE->O(n)
        """
        seen=set()
        for n in nums:
               if n in seen:return True
               seen.add(n)

        return False

nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3,4]
nums = [1,2,3,1]
print(containsDuplicate(nums))
