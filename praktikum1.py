# Praktikum 1 - Teori Graf (D)
# Kelompok 6

# Anggota Kelompok:
# - Nabila Aidah Diani        (5025211032)
# - Mashita Dewi              (5025211036)
# - Andhika Lingga Mariano    (5025211161)

from bisect import bisect_left

def lengthOfLIS(nums):
    # Initialize the LIS with the first element of the input list
    ans = [nums[0]]

    # Iterate through the input list starting from the second element
    for i in range(1, len(nums)):
        # If the current element is greater than the last element of the LIS, add it to the LIS
        if nums[i] > ans[-1]:
            ans.append(nums[i])
        else:
            # If the current element does not extend the LIS, perform binary search to find the index where it should be inserted
            low = bisect_left(ans, nums[i])
            # Update the element at the found index with the current element
            ans[low] = nums[i]

    # Return both the length of the LIS and the LIS itself
    return len(ans), ans

# Take user input for a list of numbers
nums_input = input("Enter a list of numbers separated by spaces: ")
nums = list(map(int, nums_input.split()))

# Calculate the length of the LIS and get the LIS elements
length, lis_elements = lengthOfLIS(nums)

# Print the input list, length of the LIS, and the LIS elements
print("Input from user:", nums)
print("Length of LIS is", length)
print("The LIS elements are", lis_elements)
