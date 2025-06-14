def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]
    
    return result


def merge_all_lists(lists):
    """Рекурсивная функция, которая объединяет несколько отсортированных списков."""
    if len(lists) == 1:
        return lists[0]  # Базовый случай: возвращаем единственный список
    elif len(lists) > 1:
        mid = len(lists) // 2
        left_half = merge_all_lists(lists[:mid])  # Рекурсивно объединяем левую половину
        right_half = merge_all_lists(lists[mid:])  # Правую половину тоже объединяем
        return quick_merge(left_half, right_half)  # Объединяем левое и правое половинки

