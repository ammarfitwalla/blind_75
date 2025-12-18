def moveZeroes(nums):
    """
    Move all zeroes to the end of the array in-place while maintaining the relative order of non-zero elements
    
    Args:
        nums: List[int] - Input array of integers
    """
    # Initialize position for the next non-zero element
    pos = 0
    
    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is non-zero
        if nums[i] != 0:
            # Swap the current element with the element at the 'pos' index
            nums[pos], nums[i] = nums[i], nums[pos]
            # Increment the 'pos' index to point to the next position for a non-zero element
            pos += 1

# Example usage
if __name__ == "__main__":
    # Test cases
    nums1 = [1, 0, 1, 0, 3, 12]
    print("Original array:", nums1)
    moveZeroes(nums1)
    print("After moving zeroes:", nums1)
    
    nums2 = [0, 2, 0, 4, 0, 5]
    print("\nOriginal array:", nums2)
    moveZeroes(nums2)
    print("After moving zeroes:", nums2)