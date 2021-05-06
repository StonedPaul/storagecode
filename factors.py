def factors(num):
    nums = []
    for i in range(1, num):
        if num % i == 0:
            nums.append(i)
    return nums
maxnum, pos = 0, 0
for i in range(1, 101):
    arr = factors(i)
    maxnum = max(maxnum, sum(arr))
    print(f"{i}  :  {arr}")
print(f"Max sum was:  {maxnum}")

