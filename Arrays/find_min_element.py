# Program : Find the minimum element in an array.
# Input : size = 5 and array = [1, 3, 5, 2, 4]
# Output : 1
# Language : Python3

# O(n) time | O(1) space
def find_min_element(size, array):

    # Assume that first element is the minimum element in the array.
    min_element = array[0]

    # Do for each element starting from position 1 to size-1.
    for i in range(1, size):
        # Declare the current element.
        current_element = array[i]
        # If current_element is less than min_element, then update min_element.
        if current_element < min_element:
            min_element = current_element

    # Return the min_element.
    return min_element 

# Main function.
if __name__ == '__main__':

    # Declare the size and array.
    size = 5
    array = [1, 3, 5, 2, 4]

    # Find minimum element and store it in answer variable.
    answer = find_min_element(size, array)

    # Print answer.
    print(answer)