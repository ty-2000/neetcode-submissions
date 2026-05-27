"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        # In each step of the seach,
        #   If the node is already visited, return the copied value
        #   Mark the node as visitd
        #   Copy the original node to the copied graph

        # Map the original node to the copied node
        # Every time visiting a new node, sotre a copy to this
        old_to_new = {}
        def dfs(org: Node) -> Node:

            # If the node is already visited
            if org in old_to_new:
                return old_to_new[org]

            # Mark as visited
            cp = Node(org.val)
            old_to_new[org] = cp

            # Seach all neighbors
            for neighbor in org.neighbors:
                cp.neighbors.append(dfs(neighbor))
            
            # Finally return the copied node
            return cp
        
        return dfs(node) if node else None
