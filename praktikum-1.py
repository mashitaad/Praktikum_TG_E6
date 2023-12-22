def LMIS(nums):
    n = len(nums)
    if n == 0:
        return 0, []

    # Initialize an array to store the length of the longest increasing subsequence
    lis_length = [1] * n

    # Initialize an array to store the LMIS
    lis_list = [[num] for num in nums]

    # Perform dynamic programming to find the LMIS
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and lis_length[i] < lis_length[j] + 1:
                lis_length[i] = lis_length[j] + 1
                lis_list[i] = lis_list[j] + [nums[i]]

    # Find the maximum length of the LMIS
    max_lmis_index = lis_length.index(max(lis_length))
    max_lmis = lis_list[max_lmis_index]

    return max_lmis

# User input for the list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Calculate and display the LMIS
lmis = LMIS(nums)
print("Length of LMIS is", len(lmis))
print("Longest Monotonically Increasing Subsequence (LMIS):", lmis)
