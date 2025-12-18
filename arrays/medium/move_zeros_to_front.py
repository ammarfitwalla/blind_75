# def move_zeros_to_front(nums):
#     n = len(nums)
#     write_index = n - 1  # Start from the end of the array

#     # Traverse the array from the end
#     for read_index in range(n - 1, -1, -1):
#         if nums[read_index] != 0:
#             nums[write_index] = nums[read_index]
#             write_index -= 1
#     print(f"write_index: {write_index}, nums: {nums}")
#     # Fill the remaining positions with zeros
#     while write_index >= 0:
#         nums[write_index] = 0
#         write_index -= 1


def moveZeroesToFront(nums):
    """
    Move all zeroes to the front of the array in-place while maintaining the relative order of non-zero elements.
    
    Args:
        nums: List[int] - Input array of integers
    """
    pos = len(nums) - 1
    
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos -= 1

# Example usage
nums = [1, 1, 1, 0, 1, 0, 3, 12]
moveZeroesToFront(nums)
print(nums)  # Output: [0, 0, 1, 3, 12]