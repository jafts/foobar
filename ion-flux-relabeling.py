'''
Ion Flux Relabeling
===================

Oh no! Commander Lambda's latest experiment to improve the efficiency of the LAMBCHOP doomsday device has backfired spectacularly. The Commander had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. Commander Lambda is having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly -- quickly enough, perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, Lambda performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:

   7
 3   6
1 2 4 5

Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter.  For example, solution(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth.  The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(5, {19, 14, 28})
Output:
    21,15,29

Input:
Solution.solution(3, {7, 3, 5, 1})
Output:
    -1,7,6,3

-- Python cases --
Input:
solution.solution(3, [7, 3, 5, 1])
Output:
    -1,7,6,3

Input:
solution.solution(5, [19, 14, 28])
Output:
    21,15,29
'''
# Drew out the second example on paper and concluded:
# The right side tree/subtrees can be thought of as mirrors of left side tree/subtrees
# We only need to focus on fully left side children, then add parent to find right side mirror
# The right side mirror node is equal to the left node plus its parent
# In the examples provided, the fully left side nodes are always equal to ((parent - 1) / 2)
# Right side nodes could be calculated using post-order traversal, but there would be more iterations
# Mixture of right then left nodes require extra calculation

def solution(h, q):
    found = []  # The list of identified parents
    for missing in q:  # iterate through the list of flux converters with missing parents
        node = (2 ** h) - 1  # identify the root value 2^h - 1
        parent = -1  # the root parent does not exist
        add_left = 0  # The amount we should add for right side mirrors
        while not missing == node:  # Traverse left side
            left_node = (node - 1) / 2  # fully left children are ((parent - 1) / 2)
            right_node = node - 1  # right child is (left child + 1) or (parent - 1)
            if not right_node == missing:
                if missing <= node // 2:  # if missing is on the left side
                    parent = node  # set current as parent
                    node = left_node  # move to left child
                else:  # missing must be on the right side
                    add_left += left_node  # add parent index to the amount we will add for right side mirrors
                    missing -= left_node  # set missing index to the left side mirror
                    parent = node  # set current as parent
                    node = left_node  # set current node to left side mirror
            else:  # we have found the node with a missing parent
                parent = node  # identify the parent
                node = right_node  # mark the node as found to exit loop
        found.append(parent + add_left)  # add the missing parent
    return found


'''
      7
  3       6
1   2   4   5
'''

print(solution(3, [7, 3, 5, 1]))
# print(solution(5, [19, 14, 28]))
