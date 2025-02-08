import sys

new_limit = sys.getrecursionlimit()*10
sys.setrecursionlimit(new_limit)

def create_node(index, value):
    """Create a tree node with its index and (x, y) coordinates."""
    return {"index": index, "value": value, "left": None, "right": None}

def insert(node, index, value):
    """Insert a node based on X-coordinate while keeping Y structure."""
    if node is None:
        return create_node(index, value)
    
    if value[0] < node["value"][0]:  # Compare X-coordinate
        node["left"] = insert(node["left"], index, value)
    else:
        node["right"] = insert(node["right"], index, value)
    
    return node

def preorder_traversal(node):
    """Preorder Traversal (Root -> Left -> Right), returning node indices."""
    if node is None:
        return []
    return [node["index"]] + preorder_traversal(node["left"]) + preorder_traversal(node["right"])

def postorder_traversal(node):
    """Postorder Traversal (Left -> Right -> Root), returning node indices."""
    if node is None:
        return []
    return postorder_traversal(node["left"]) + postorder_traversal(node["right"]) + [node["index"]]

def solution(nodeinfo):
    """Build tree and return preorder & postorder traversal based on node numbers."""
    # Ensure nodeinfo is a list of tuples
    nodeinfo = [tuple(node) for node in nodeinfo]  # Convert lists to tuples
    
    # Assign node numbers (1-based index) while keeping original order
    indexed_nodes = [(i + 1, node[0], node[1]) for i, node in enumerate(nodeinfo)]
    
    # Sort nodes by Y-coordinate (descending), then by X-coordinate (ascending)
    indexed_nodes.sort(key=lambda x: (-x[2], x[1]))  # Highest Y first, then left to right
    
    # Build tree
    tree = None
    for index, x, y in indexed_nodes:
        tree = insert(tree, index, (x, y))

    # Get traversal results using node indices
    return [preorder_traversal(tree), postorder_traversal(tree)]

# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.4MB)
# 테스트 6 〉	통과 (101.04ms, 11.3MB)
# 테스트 7 〉	통과 (105.11ms, 11.3MB)
# 테스트 8 〉	통과 (62.41ms, 12.7MB)
# 테스트 9 〉	통과 (348.42ms, 16.9MB)
# 테스트 10 〉	통과 (19.85ms, 11.3MB)
# 테스트 11 〉	통과 (270.09ms, 16.6MB)
# 테스트 12 〉	통과 (386.93ms, 16.9MB)
# 테스트 13 〉	통과 (0.50ms, 10.2MB)
# 테스트 14 〉	통과 (4.41ms, 10.8MB)
# 테스트 15 〉	통과 (21.22ms, 13.3MB)
# 테스트 16 〉	통과 (45.59ms, 16.2MB)
# 테스트 17 〉	통과 (4.80ms, 10.7MB)
# 테스트 18 〉	통과 (55.42ms, 16.4MB)
# 테스트 19 〉	통과 (8.57ms, 11.3MB)
# 테스트 20 〉	통과 (21.14ms, 12.9MB)
# 테스트 21 〉	통과 (29.88ms, 13.9MB)
# 테스트 22 〉	통과 (53.45ms, 16.1MB)
# 테스트 23 〉	통과 (59.03ms, 16.8MB)
# 테스트 24 〉	통과 (0.02ms, 10.3MB)
# 테스트 25 〉	통과 (0.03ms, 10.3MB)
# 테스트 26 〉	통과 (159.85ms, 11.9MB)
# 테스트 27 〉	통과 (0.02ms, 10.1MB)
# 테스트 28 〉	통과 (0.05ms, 10.3MB)
# 테스트 29 〉	통과 (0.01ms, 10.2MB)
