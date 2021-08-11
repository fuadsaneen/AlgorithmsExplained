# Program : Binary search in an array.
# Input : size = 5, array = [1, 2, 3, 4, 5], target = 2
# Output : 1
# Language : Python3

# O(log(n)) time | O(1) space
def binary_search(size, array, target):

    # Initialize the left and right pointers as zero and size-1.
    left = 0
    right = size - 1

    # Till the left <= right.
    while left <= right:

        # Compute the middle index and middle element.
        middle_index = left + (right - left) // 2
        middle_element = array[middle_index]

        # If the middle element is equal to the target, then return middle index.
        if middle_element == target:
            return middle_index
        # If the middle element is less than the target, then increment left pointer.   
        elif middle_element < target:
            left = left + 1
        # Otherwise, ie, if the middle element is greater than the target, then decrement right pointer.  
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

    # Find the index of the target and store it in answer variable.
    answer = binary_search(size, array, target)

    # Print answer.
    print(answer)