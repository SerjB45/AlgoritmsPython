# Пример с рюкзаком
# задача о рюкзаке с дробимыми предметами (Knapsack Problem)

def greedy_knapsack(items, capacity):
    items.sort(key=lambda x: x['value'] / x['weight'], reverse=True)  # Сортируем по ценности единицы массы
    total_value = 0
    remaining_capacity = capacity

    result = []

    for item in items:
        if remaining_capacity >= item['weight']:
            # Берём весь предмет целиком
            result.append({'item': item, 'fraction': 1})
            total_value += item['value']
            remaining_capacity -= item['weight']
        elif remaining_capacity > 0:
            # Берём только часть предмета, подходящую по остаточной вместимости
            fraction = remaining_capacity / item['weight']
            result.append({'item': item, 'fraction': fraction})
            total_value += item['value'] * fraction
            break  # Осталось меньше вместимости, останавливаемся

    return total_value, result


def test_greedy_knapsack():
    # Пример набора предметов
    items = [
        {"name": "Item1", "value": 60, "weight": 10},  # Предмет 1: стоимость 60, масса 10 кг
        {"name": "Item2", "value": 100, "weight": 20}, # Предмет 2: стоимость 100, масса 20 кг
        {"name": "Item3", "value": 120, "weight": 30}, # Предмет 3: стоимость 120, масса 30 кг
    ]
    capacity = 50  # Максимальная грузоподъёмность рюкзака

    total_value, result = greedy_knapsack(items, capacity)

    print("Максимальная общая ценность:", total_value)
    print("Выбранные предметы:")
    for r in result:
        print(f"{r['item']['name']} ({r['fraction']*100:.2f}%)")
        
        
        
# Interval Scheduling problem. Суть задачи состоит в следующем: 
# имеется множество временных интервалов, и нужно выбрать подмножество 
# неперекрывающихся интервалов так, чтобы общее количество выбранных 
# интервалов было максимальным.       
def interval_scheduling(intervals):
    # Сортируем интервалы по правому краю (концу интервала)
    intervals.sort(key=lambda x: x[1])

    schedule = []  # Список выбранных интервалов
    last_end_time = float('-inf')  # Время окончания последнего выбранного интервала

    for interval in intervals:
        start, end = interval
        if start >= last_end_time:
            # Интервал не пересекается с последним выбранным
            schedule.append(interval)
            last_end_time = end

    return schedule

def test_interval_scheduling():
    # Пример входных данных
    intervals = [(1, 3), (2, 4), (3, 5), (6, 8), (9, 11), (8, 10)]
    result = interval_scheduling(intervals)

    print("Максимальное количество неперекрывающихся интервалов:")
    for interval in result:
        print(interval)