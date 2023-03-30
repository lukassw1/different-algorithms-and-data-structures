class Node:
    def __init__(self, position, cost):
        self.position = position
        self.cost = cost
        self.neighbours = []
        self.visited = False
        self.visible = False

    def add_neighbour(self, neighbouring_node):
        self.neighbours.append(neighbouring_node)
        # self._neighbours.sort(key=lambda node: node.cost)

    def set_visited(self):
        self.visited = True

    def set_visible(self):
        self.visible = True


def make_table(file_handle):
    str_table = file_handle.read()
    return [list(i) for i in str_table.split('\n')]


def create_nodes(table):
    nodes = []
    for i in range(len(table)):
        sub_nodes = []
        for j in range(len(table[i])):
            new_node = Node((i, j), int(table[i][j]))
            sub_nodes.append(new_node)
        nodes.append(sub_nodes)
    return nodes


def add_neighbours(nodes):
    for i in range(len(nodes)):
        for j in range(len(nodes[i])):
            node = nodes[i][j]
            if j != 0:
                node.add_neighbour(nodes[i][j-1])
            if j != len(nodes[i])-1:
                node.add_neighbour(nodes[i][j+1])
            if i != 0:
                node.add_neighbour(nodes[i-1][j])
            if i != len(nodes)-1:
                node.add_neighbour(nodes[i+1][j])


def get_nodes(file):
    with open(file, 'r') as fh:
        table = make_table(fh)
    nodes = create_nodes(table)
    add_neighbours(nodes)
    out_nodes = []
    for sub_nodes in nodes:
        for node in sub_nodes:
            out_nodes.append(node)
    return out_nodes, len(nodes[0])


def dijkstra(nodes):
    start = None
    end = None
    visited_nodes = set()
    not_visited = set()
    costs_dict = {}
    previous_nodes_dict = {}
    for node in nodes:
        costs_dict[node] = float("inf")
        previous_nodes_dict[node] = -1
        if node.cost == 0:
            if start is None:
                start = node
            else:
                end = node
    costs_dict[start] = 0
    not_visited = set(nodes)
    while len(not_visited) != 0:
        queue = sorted(not_visited, key=lambda node: costs_dict[node])
        visited_nodes.add(queue[0])
        not_visited.remove(queue[0])
        for neighbour in queue[0].neighbours:
            if neighbour in not_visited:
                if costs_dict[neighbour] > costs_dict[queue[0]] + neighbour.cost:
                    costs_dict[neighbour] = costs_dict[queue[0]] + neighbour.cost
                    previous_nodes_dict[neighbour] = queue[0]
                    neighbour.set_visited()
    temp = end
    while temp != start:
        temp.set_visible()
        prev = previous_nodes_dict[temp]
        temp = prev
    start.set_visible()
    start.set_visited()
    return nodes


def print_nodes(nodes: list, width):
    text = ''
    for i, node in enumerate(nodes):
        if node.visible and node.visited:
            text += str(node.cost)
        else:
            text += ' '
        if i % width == width - 1:
            text += '\n'
    return text[:len(text) - 1]


def main():
    nodes, width = get_nodes("graph1.txt")
    nodes = dijkstra(nodes)
    print(print_nodes(nodes, width))


if __name__ == "__main__":
    main()
