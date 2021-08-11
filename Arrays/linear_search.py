# Program : Linear search in an array.
# Input : size = 5, array = [1, 3, 5, 2, 4], key = 5
# Output : 2
# Language : Python3

# O(n) time | O(1) space
def linear_search(size, array, key):

    # Do for each element in the array.
    for i in range(size):
        # Declare the current element.
        current_element = array[i]
        # If the current element is equal to key, then return the current index.
        if current_element == key:
            return i

    # If the key is not found, then return -1.
    return -1

# Main function.
if __name__ == '__main__':

    # Declare the size, array and key.
    size = 5
    array = [1, 3, 5, 2, 4]
    key = 10

    # Find the index of the key and store it in answer variable.
    answer = linear_search(size, array, key)

    # Print answer.
    print(answer)