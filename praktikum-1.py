from bisect import bisect_left

def lengthOfLIS(nums):
    ans = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > ans[-1]:
            ans.append(nums[i])
        else:
            low = bisect_left(ans, nums[i])
            ans[low] = nums[i]

    return len(ans), ans

nums_input = input("Enter a list of numbers separated by spaces: ")
nums = list(map(int, nums_input.split()))

length, lis_elements = lengthOfLIS(nums)

print("Input from user:", nums)
print("Length of LIS is", length)
print("The LIS elements are", lis_elements)
