import heapq

def dijkstra(graph, start_vertex):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаем устаревшие расстояния
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найден путь короче, обновляем расстояние
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def test_dijkstra():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
   
    start_vertex = 'A'
    shortest_distances = dijkstra(graph, start_vertex)

    for vertex, dist in shortest_distances.items():
        print(f"Кратчайший путь от '{start_vertex}' до '{vertex}' составляет: {dist}")