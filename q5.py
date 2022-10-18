# ------------------------------------------------------ #
# abstract : assignment 1 Question 5 Permutation
# author : hhk
# time : 2022.10.13
# ------------------------------------------------------ #
import copy

result = []  # The global variable
path = []

# --------- definition --------- #
def BackTracking(nums,used):
    """
    :param nums: The List of numbers to be arranged
    :param used: Store a Boolean list of numbers in nums that have not been used
    :return:
    """
    if(len(path) == len(nums)):
        result.append(path.copy())          # 必须要path.copy()，否则list更新错误
        return
    for i in range(len(nums)):
        if(used[i] is True):
            continue
        used[i] = True
        path.append(nums[i])
        BackTracking(nums,used)
        path.pop()
        used[i] = False

def permute(nums):
    used = []
    for i in range(len(nums)):    # define an all-false list
        used.append(False)
    BackTracking(nums,used)
    return result


# --------- main --------- #
nums = [1,2,3]
ans = permute(nums)
print(ans)