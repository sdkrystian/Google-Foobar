def answer(xs):
    nums = []
    negs = []
    maxpower = 1
    if (max(xs) == 0 and min(xs) < 0):
        return str(0)
    if (max(xs) == 0 and min(xs) == 0):
        return str(0)
    for i in xs:
        if (i != 0):
            nums.append(i)  
            if i < 0:
                negs.append(i)
    if (max(nums) < 0 and len(nums) == 1):
        return nums[0]
    if (len(negs) % 2 == 1 and len(negs) >= 1):
        negs.sort()
        nums.remove(negs[len(negs) - 1])
    for i in nums:
        maxpower *= i
    return str(maxpower)