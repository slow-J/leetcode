def find_cycle(graph):
    # Simple BFS - would be more memory efficient with DFS.
    nodes_traversed = set()
    queue = [graph]
    current = []
    while queue:
        current, queue = queue, []
        for cur in current:
            for node in cur:
                if node in nodes_traversed:
                    return True
                else:
                    nodes_traversed.add(node)
                    queue.append(cur[node])
    return False


graph = {"a": {"a2": {}, "a3": {}}, "b": {"b2": {}}, "c": {}}
print(find_cycle(graph))
# False
graph["c"] = graph
print(find_cycle(graph))
# True
