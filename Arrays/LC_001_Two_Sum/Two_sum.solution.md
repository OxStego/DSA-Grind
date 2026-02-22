## Longer Example — `[3, 5, 1, 8, 2, 7]`, target = `10`

text

```
seen = {}

i=0, num=3  → need = 10-3 = 7  → 7 in {}?        ❌ → store {3:0}
i=1, num=5  → need = 10-5 = 5  → 5 in {3:0}?     ❌ → store {3:0, 5:1}
i=2, num=1  → need = 10-1 = 9  → 9 in {3:0,5:1}? ❌ → store {3:0, 5:1, 1:2}
i=3, num=8  → need = 10-8 = 2  → 2 in seen?       ❌ → store {3:0, 5:1, 1:2, 8:3}
i=4, num=2  → need = 10-2 = 8  → 8 in seen?       ✅ → return [seen[8], 4] = [3, 4]

Answer: [3, 4]  → nums[3]+nums[4] = 8+2 = 10 ✅

```

Notice — you **never looked at index 5 (num=7)** because the answer was found at index 4. That's the power of one-pass.

---

## Your Complexity Question — Great Observation!

You are **almost right**, but small correction:

|Approach|Time Complexity|Breakdown|
|---|---|---|
|HashMap|O(n)|One pass through array|
|Sort + Two Pointer|O(n log n)|Sort costs O(n log n), two pointer costs O(n)|

It's **O(n log n)** not O(2n) for sort + two pointer — because sorting itself takes O(n log n). The two pointer after is just O(n), but the sort dominates.

text

```
O(n)        →  HashMap          ← fastest O(n log n)  →  Sort + 2 pointer ← slower but O(1) space O(n²)       →  Your brute force ← slowest
```

> **O(2n) = O(n)** mathematically — constants are dropped in Big O. So if something is O(2n), we just call it O(n).

---

## Which to Use When?

text

```
LeetCode Two Sum (unsorted, need indices) → HashMap ✅                                            Sort+2ptr ❌ (sorting changes indices!) Two Sum II (already sorted, just values)  → Two Pointer ✅                                            HashMap ✅ (both work)
```

This is the key insight — **Sort + Two Pointer breaks index tracking.** Since LeetCode Two Sum asks for the original indices, sorting shuffles them and you lose the answer. HashMap preserves everything because you store `{value: original_index}`.

---

## You Now Know Both Patterns 🔥
```
Pattern 1 — HashMap O(n)
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i

# Pattern 2 — Sort + Two Pointer O(n log n)
nums.sort()              # only when indices don't matter!
l, r = 0, len(nums)-1
while l < r:
    s = nums[l] + nums[r]
    if s == target:   return [l, r]
    elif s < target:  l += 1
    else:             r -= 1
```
    
