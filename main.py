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
