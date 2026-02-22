def maxProfit(prices:list[int])->int :

            maxp=0
            min_price=max_price=prices[0]
            i=1
            while(i<len(prices)):
                    if(min_price>prices[i]):
                            min_price=prices[i]
                            max_price=min_price
                    elif(max_price<prices[i]):
                            max_price=prices[i]
                            if(maxp<max_price-min_price):
                               maxp=max_price-min_price
                    i+=1



            return maxp


prices=[10,3,9,2,26]
prices=[10,3,9,2,26]
prices=[10,4,6,2,5,1]
prices=[1,2]
result=maxProfit(prices)
print(result)