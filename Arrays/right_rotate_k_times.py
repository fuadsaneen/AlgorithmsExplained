# Program : Right rotate the array k times.
# Input : size = 5, array = [1, 3, 5, 2, 4], k = 2
# Output : [2, 4, 1, 3, 5]
# Explanation : The array is rotated k times in the right direction.
# Language : Python3

# O(n) time | O(1) space
def right_rotate_one_time(size, array):

    # Store the last element.
    last_element = array[-1]

    # Do for each element starting from position size - 2 to 0 (ie, excluding last element) in the array.
    for i in reversed(range(size - 1)):
        # Copy the current element to the next element.
        array[i + 1] = array[i]

    # Copy the last element to the first position.
    array[0] = last_element   

# O(k) time | O(1) space
def right_rotate_k_times(size, array, k):

    # Do for k times.
    for i in range(k):
        # Right rotate the array for one time.
        right_rotate_one_time(size, array)

    # Return the array.
    return array    

# Main function.
if __name__ == '__main__':

    # Declare the size, array and k.
    size = 5
    array = [1, 3, 5, 2, 4]
    k = 2

    # Right rotate the array k times and store in answer variable.
    answer = right_rotate_k_times(size, array, k)

    # Print answer.
    print(answer)