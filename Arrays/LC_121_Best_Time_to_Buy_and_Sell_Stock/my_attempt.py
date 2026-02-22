def maxProfit(prices:list[int])->int :
    
        i=j=0
        length=len(prices)
        min_price = max_price = prices[0]
        maxp=0
        while(i<len(prices)):
                if prices[i]<min_price :
                        min_price=prices[i]
                        max_price=min_price
                        i+=1
                        j=i
                        print(min_price,max_price,"j:",j)
                        while(j<length):
                        #    max_price=min_price //wrong it set max_price every time
                           if max_price < prices[j] :
                              max_price=prices[j]
                              if maxp<max_price-min_price:
                                   maxp=max_price-min_price
                                   print(maxp)
                           j+=1       
                else :i+=1
        return maxp

prices=[10,3,9,2,26]
result=maxProfit(prices)
print(result)