# Program : Binary search in an array.
# Input : size = 5, array = [1, 3, 5, 2, 4], target = 2
# Output : 3
# Language : Python3

# O(log(n)) time | O(1) space
def binary_search(size, array, target):

    # Initialize left and right pointers.
    left = 0
    right = size - 1

    # Do while left <= right.
    while left <= right:

        # Compute the middle index and middle element.
        middle_index = right - left // 2
        middle_element = array[middle_index]

        # If the middle element is equal to the target, then return middle index.
        if middle_element == target:
            return middle_index
        # If the middle element is less than the target, then increment left pointer.   
        elif middle_element < target:
            left = left + 1
        # Otherwise, ie, If the middle element is greater than the target, then decrement right pointer.  
        else:
            right = right - 1

    # If the target is not found, then return -1
    return -1                


# Main function.
if __name__ == '__main__':

    # Declare the size, array and target.
    size = 5
    array = [1, 3, 5, 2, 4]
    target = 2

    # Find the index of the target and store it in answer variable.
    answer = binary_search(size, array, target)

    # Print answer.
    print(answer)