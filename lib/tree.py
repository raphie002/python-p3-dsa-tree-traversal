# lib/tree.py
class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    """
    Searches the tree for the first element with the matching id using BFS.
    """
    if self.root is None:
      return None

    # Initialize a queue for BFS with the root element
    queue = [self.root]

    while queue:
      # Dequeue the first element
      current_element = queue.pop(0)

      # 1. Check if the current element has the matching id
      if current_element.get('id') == id:
        return current_element

      # 2. Add children to the queue for the next iteration
      # We assume 'children' is a list of elements/dictionaries
      # and handle the case where the key might not exist or is None
      children = current_element.get('children')
      if children and isinstance(children, list):
        # Extend the queue with the current element's children
        queue.extend(children)
        
    # If the loop finishes without finding a match
    return None