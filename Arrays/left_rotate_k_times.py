# Program : Left rotate the array k times.
# Input : size = 5, array = [1, 3, 5, 2, 4], k = 2
# Output : [5, 2, 4, 1, 3]
# Language : Python3

# O(n) time | O(1) space
def left_rotate_by_one(size, array):

    # Store first element.
    first_element = array[0]

    # Do for each element starting from position 0 to size - 2 (ie, excluding last element).
    for i in range(size - 1):
        # Copy next element to current element.
        array[i] = array[i + 1]

    # Copy first element to last position.
    array[-1] = first_element   

# O(k) time | O(1) space
def left_rotate_by_k(size, array, k):

    # Do for k times.
    for i in range(k):
        # Left rotate the array by one position.
        left_rotate_by_one(size, array)

    # Return the updated array.
    return array    

# Main function.
if __name__ == '__main__':

    # Declare the size, array and k.
    size = 5
    array = [1, 3, 5, 2, 4]
    k = 2

    # Left rotate the array by k positions and store it in answer variable.
    answer = left_rotate_by_k(size, array, k)

    # Print answer.
    print(answer)