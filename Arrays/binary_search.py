# Program : Binary search in an array.
# Input : size = 5, array = [1, 2, 3, 4, 5], target = 2
# Output : 1
# Explanation : The index of the element 2 is 1.
# Language : Python3

# O(log(n)) time | O(1) space
def binary_search(size, array, target):

    # Initialize the left and right pointers as zero and size-1.
    left = 0
    right = size - 1

    # Do till the left less than or equal to right.
    while left <= right:

        # Compute the middle index and the middle element.
        middle_index = left + (right - left) // 2
        middle_element = array[middle_index]

        # If the middle element is equal to the target, then return the middle index.
        if middle_element == target:
            return middle_index
        # If the middle element is less than the target, then increment the left pointer.   
        elif middle_element < target:
            left = left + 1
        # Otherwise, if the middle element is greater than the target, then decrement the right pointer.  
        else:
            right = right - 1

    # If the target is not found, then return -1
    return -1                


# Main function.
if __name__ == '__main__':

    # Declare the size, array and target.
    size = 5
    array = [1, 2, 3, 4, 5]
    target = 2

    # Find the index of the target and store the result in the answer variable.
    answer = binary_search(size, array, target)

    # Print the answer.
    print(answer)