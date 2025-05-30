def bellman_ford(graph, source):
    # Инициализация расстояний: от начальной вершины до всех других вершин бесконечно далеко
    distance = {v: float('inf') for v in graph}
    distance[source] = 0  # Расстояние до самого себя равняется 0

    # Проходим по всем вершинам N раз (N - количество вершин)
    vertices_count = len(graph)
    for _ in range(vertices_count - 1):
        # Рассматриваем каждое ребро
        for u in graph:
            for v, w in graph[u].items():  # Просмотр соседних вершин и весов рёбер
                # Рассчитываем новое возможное расстояние
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    # Проверка наличия отрицательных циклов
    for u in graph:
        for v, w in graph[u].items():
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                raise ValueError("Граф содержит цикл с отрицательной суммой весов")

    return distance

def test_bellman_ford():
    graph = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2, 'E': 2},
        'C': {},
        'D': {'B': 1, 'C': 5},
        'E': {'D': -3}
    }
    
    # Начало поиска от вершины 'A'
    shortest_paths = bellman_ford(graph, 'A')

    for node, dist in shortest_paths.items():
        print(f"Кратчайший путь от 'A' до '{node}': {dist}")