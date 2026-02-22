#this is correct solution but issue is that it returns numbers of instead of indicies 
def twosum(nums:list[int],target:int)->list[int]:
        snums=sorted(nums)
        left=0
        right=len(snums)-1
        temp:list[int]=[]
        while(left<len(snums)-1 and right>0):
                s=snums[left]+snums[right]
                if(s>target) :right-=1
                elif(s<target):left+=1
                else:
                    temp.append(snums[left])
                    temp.append(snums[right])
                    break
        return []

nums=[-1,-2,-3,-4,-5]
result=twosum(nums,-8)
print(result)