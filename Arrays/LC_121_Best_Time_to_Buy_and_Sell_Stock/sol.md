## Your Solution — Correct! ✅ And O(N) 🔥

Let me trace it to confirm:

text

`prices = [10, 3, 9, 2, 26] i=1: 3  < min(10) → min=3,  max=3 i=2: 9  > max(3)  → max=9,  maxp=6 i=3: 2  < min(3)  → min=2,  max=2 i=4: 26 > max(2)  → max=26, maxp=24 Result: 24 ✅ prices = [10,4,6,2,5,1] Result: 3 ✅  (buy@2, sell@5) prices = [1,2] Result: 1 ✅`

---

## Small Correction — Not Exactly Two Pointer

You called it two pointer — close, but not exactly:

|Pattern|What it uses|
|---|---|
|Two Pointer|Two index variables `i`, `j` moving through array|
|Your solution|Two **value trackers** `min_price`, `max_price`|
|Correct name|**Greedy / One Pass**|

Two pointer would look like:

python

`i, j = 0, 1 while j < len(prices):     if prices[i] < prices[j]: ...    j += 1`

Your approach is actually **cleaner** than two pointer for this problem! ✅

---

## Compare With Standard LeetCode Solution

python

```
# Standard solution — almost identical to yours!
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

```

Your logic is **exactly the same** — you just wrote it with a while loop instead of for loop. Same O(N) TC, O(1) SC. 💪