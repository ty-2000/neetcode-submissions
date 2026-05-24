class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        node_to_index = {}
        copied_list = []


        copied_root = Node(-1)

        cur = head
        copied_prev = copied_root
        i = 0
        while cur:
            # Creat a map
            node_to_index[cur] = i

            # Create a copied list
            copied_prev.next = Node(cur.val)
            copied_prev = copied_prev.next
            cur = cur.next

            # Keep the copied list as list
            copied_list.append(copied_prev)

            i += 1
        
        # Create a ranom map for the copied list
        cur = head
        copied_cur = copied_root.next
        while cur:
            if cur.random is not None:
                i = node_to_index[cur.random]
                copied_cur.random = copied_list[i]
            cur = cur.next
            copied_cur = copied_cur.next

        return copied_root.next

