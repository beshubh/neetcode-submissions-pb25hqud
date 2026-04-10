class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = {x: [] for x in range(n)}
        for (src, dst) in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in graph.get(node, []):
                if nei not in visited:
                    dfs(nei)

        connected_components = 0 
        for node in graph:
            if node not in visited:
                dfs(node)
                connected_components += 1
        return connected_components


