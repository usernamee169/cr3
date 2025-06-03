"""
Graf7. Две корпорации хотят разделить сферы влияния, выбрав два разных города для
размещения своих штаб-квартир так, чтобы все города, в некоторой округе от штаб
квартиры не были доступны для конкурентов. Схема автомобильного сообщения между
городами задана в текстовом файле с именем FileName в виде матрицы смежности. Первая
строка файла содержит количество городов (n, n<=25), связанных дорогами, а следующие
n строк хранят матрицу (m), m[i][j]=0, если нет дороги из города i в город j, иначе m[i][j]=1.
Даны два города-кандидата с номерами K1 и K2 для этих двух штаб-квартир. Определить
есть ли города, в которые можно попасть из обоих штаб-квартир, если двигаться от
каждой штаб-квартиры не более чем через L промежуточных городов. Перечислите
номера таких городов в порядке возрастания. Нумерация городов начинается с 1. Если
таких городов нет, выведите число (-1).

Языковая модель: https://giga.chat
"""

from collections import deque

def bfs(matrix, start_city, max_hops):
    """
    Возвращает множество достижимых городов из стартового города,
    проходя не более max_hops промежуточных переходов.
    """
    visited = set([start_city])
    queue = deque([(start_city, 0)])  # пара (текущий город, глубина)
    
    while queue:
        current_city, depth = queue.popleft()
        
        if depth > max_hops:
            continue
            
        for next_city in range(len(matrix[current_city])):
            if matrix[current_city][next_city] == 1 and next_city not in visited:
                visited.add(next_city)
                queue.append((next_city, depth + 1))
                
    return visited

def find_common_cities(file_name, k1, k2, l):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        num_cities = int(lines[0].strip())
        adjacency_matrix = []
        
        for line in lines[1:num_cities+1]:
            row = list(map(int, line.strip().split()))
            adjacency_matrix.append(row)
    
    # Выполняем BFS для нахождения достижимых городов из каждой штаб-квартиры
    reachable_from_k1 = bfs(adjacency_matrix, k1-1, l)
    reachable_from_k2 = bfs(adjacency_matrix, k2-1, l)
    
    # Пересечение множеств доступных городов
    common_cities = sorted(list(reachable_from_k1 & reachable_from_k2))
    
    if len(common_cities) == 0:
        return [-1]
    else:
        return [city + 1 for city in common_cities]  # Индексация с единицы

# Тестируем программу
file_name = 'FileName.txt'
k1 = 1
k2 = 2
l = 2
result = find_common_cities(file_name, k1, k2, l)
print(result)
