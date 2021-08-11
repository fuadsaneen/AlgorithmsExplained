# Program : Print n*n box.
# Input : number = 4
# Output : * * * *
#          * * * *
#          * * * *
#          * * * *
# Explanation : 4 rows and 4 coloumns of star is printed.
# Language : Python3

# O(n) time | O(1) space
def n_by_n_box(n):

    # For each row.
    for i in range(4):
        # For each coloumn.
        for j in range(4):
            # Print * followed by an empty space.
            print("*", end = " ")
        # Go to new line.    
        print("")  

# Main function.
if __name__ == '__main__':

    # Declare n.
    n = 4

    # Execute n_by_n_box().
    n_by_n_box(n)     