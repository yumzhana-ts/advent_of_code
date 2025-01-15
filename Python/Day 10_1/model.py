class Node:
    def __init__(self, x, y, case):
        self.x = x
        self.y = y
        self.case = case
        self.children = []
        self.parent = None

    def set_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_ancestors(self):
        ancestors = []
        current = self.parent
        while current:
            ancestors.append(current)
            current = current.parent
        return ancestors

    def get_all_children(self):
        all_children = []
        for child in self.children:
            all_children.append(child)
            all_children.extend(child.get_all_children())  # Рекурсивно добавляем детей детей
        return all_children

    def print_info(self):
        ancestors = self.get_ancestors()
        ancestors_values = [ancestor.case for ancestor in ancestors]  # Используем 'case' для предков
        children_values = [child.case for child in self.children]  # Используем 'case' для детей

        print(f"Node at position ({self.x}, {self.y}) with case: {self.case}")
        print(f"Ancestors' cases: {ancestors_values if ancestors_values else 'No ancestors'}")
        print(f"Children's cases: {children_values if children_values else 'No children'}")

    def __repr__(self):
        return f"Node(x={self.x}, y={self.y}, case={self.case})"

def get_all_paths(node, path=None):
    if path is None:
        path = []
    
    path.append(f"[{node.x},{node.y}]:{node.case}")
    if not node.children:
        return [" -> ".join(path)]
    else:
        paths = []
        for child in node.children:
            paths.extend(get_all_paths(child, path.copy()))
        return paths
