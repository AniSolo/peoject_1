from collections import deque

def find_farthest_vertex(tree, start):
    # Функция для поиска самой удаленной вершины от данной
    visited = set()
    max_distance = [0] * (len(tree) + 1)
    
    queue = deque([(start, 0)])  # Очередь для обхода в ширину
    while queue:
        node, distance = queue.popleft()
        visited.add(node)
        for neighbor, weight in tree[node]:
            if neighbor not in visited:
                max_distance[neighbor] = max(max_distance[neighbor], distance + weight)
                queue.append((neighbor, distance + weight))
    
    farthest_vertex = max(enumerate(max_distance[1:], start=1), key=lambda x: x[1])
    return farthest_vertex

def find_tree_diameter(tree):
    # Находим диаметр дерева - максимальное расстояние между вершинами
    start_vertex = 1  # Можно начать с любой вершины
    farthest_vertex_1, _ = find_farthest_vertex(tree, start_vertex)
    farthest_vertex_2, diameter = find_farthest_vertex(tree, farthest_vertex_1)
    return diameter

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

diameter = find_tree_diameter(tree)
print(diameter)
