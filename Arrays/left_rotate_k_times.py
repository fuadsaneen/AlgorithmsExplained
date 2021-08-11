# Program : Left rotate the array k times.
# Input : size = 5, array = [1, 3, 5, 2, 4], k = 2
# Output : [5, 2, 4, 1, 3]
# Explanation : The array is rotated k times in the left direction.
# Language : Python3

# O(n) time | O(1) space
def left_rotate_one_time(size, array):

    # Store the first element.
    first_element = array[0]

    # Do for elements starting from position 0 to size - 2 (ie, excluding last element) in the array.
    for i in range(size - 1):
        # Copy the next element to the current element.
        array[i] = array[i + 1]

    # Copy the first element to the last position.
    array[-1] = first_element   

# O(k) time | O(1) space
def left_rotate_k_times(size, array, k):

    # Do for k times.
    for i in range(k):
        # Left rotate the array for one time.
        left_rotate_one_time(size, array)

    # Return the array.
    return array    

# Main function.
if __name__ == '__main__':

    # Declare the size, array and k.
    size = 5
    array = [1, 3, 5, 2, 4]
    k = 2

    # Left rotate the array k times and store the result in answer variable.
    answer = left_rotate_k_times(size, array, k)

    # Print answer.
    print(answer)