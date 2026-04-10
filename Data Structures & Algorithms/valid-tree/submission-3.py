class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {x: [] for x in range(n)}
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = set()
        def dfs_cycle(node: int, parent: int) -> True:
            visited.add(node)
            for nei in graph.get(node, []):
                if nei not in visited:
                    if dfs_cycle(nei, node):
                        return True
                elif nei != parent:
                    return True
            return False

        itr, cycle = 0, False
        for node in graph:
            if node not in visited:
                itr += 1
                if itr > 1:
                    return False
                cycle = dfs_cycle(node, -1)
        return not cycle
