import math
from collections import Counter

# Евклидово расстояние между двумя точками
def euclidean_distance(point1, point2):
    # Передаем только координаты (без последней метки класса)
    sum_squared_diff = sum((x - y) ** 2 for x, y in zip(point1[:-1], point2[:-1]))  # игнорируем последний элемент (класс)
    return math.sqrt(sum_squared_diff)

# Основной алгоритм KNN
def knn_classify(train_data, test_point, k=3):
    # Вычислим расстояния от тестовой точки до всех точек тренировочного набора
    distances = [(point, euclidean_distance(test_point, point[0])) for point in train_data]

    # Отсортируем точки по возрастанию расстояния
    sorted_points = sorted(distances, key=lambda x: x[1])

    # Возьмем k ближайших соседей
    k_nearest_neighbors = sorted_points[:k]

    # Определим класс большинством голосов среди ближайших соседей
    labels = [point[0][-1] for point in k_nearest_neighbors]  # берем последнюю позицию (класс)
    label_counts = Counter(labels)
    most_common_label = label_counts.most_common(1)[0][0]

    return most_common_label

def test_knn_classify():
    # Тренировочный набор данных (каждый элемент — кортеж признаков и метка класса)
    train_data = [
        ([1, 2], 'A'),
        ([2, 1], 'A'),
        ([2, 3], 'A'),
        ([3, 2], 'A'),
        ([6, 5], 'B'),
        ([5, 6], 'B'),
        ([5, 4], 'B'),
        ([6, 7], 'B')
    ]

    # Тестовая точка
    test_point = [3, 3]

    # Количество ближайших соседей
    k = 3
    
    predicted_class = knn_classify(train_data, test_point, k=k)

    print(f"Предсказанная метка класса для точки {test_point}: {predicted_class}")