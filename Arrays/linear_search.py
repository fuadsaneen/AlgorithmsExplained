# Program : Linear search in an array.
# Input : size = 5, array = [1, 3, 5, 2, 4], target = 5
# Output : 2
# Explanation : The index of element 5 is 2.
# Language : Python3

# O(n) time | O(1) space
def linear_search(size, array, target):

    # Do for each element in the array.
    for i in range(size):
        # Declare the current element.
        current_element = array[i]
        # If the current element is equal to the target, then return current index.
        if current_element == target:
            return i

    # If the target is not found, then return -1.
    return -1

# Main function.
if __name__ == '__main__':

    # Declare the size, array and target.
    size = 5
    array = [1, 3, 5, 2, 4]
    target = 5

    # Find the index of the target and store the result in answer variable.
    answer = linear_search(size, array, target)

    # Print answer.
    print(answer)