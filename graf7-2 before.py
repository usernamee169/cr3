"""Graf7. Две корпорации хотят разделить сферы влияния, выбрав два разных города для
 размещения своих штаб-квартир так, чтобы все города, в некоторой округе от штаб
квартиры не были доступны для конкурентов. Схема автомобильного сообщения между
 городами задана в текстовом файле с именем FileName в виде матрицы смежности. Первая
 строка файла содержит количество городов (n, n<=25), связанных дорогами, а следующие
 n строк хранят матрицу (m), m[i][j]=0, если нет дороги из города i в город j, иначе m[i][j]=1.
 Даны два города-кандидата с номерами K1 и K2 для этих двух штаб-квартир. Определить
 есть ли города, в которые можно попасть из обоих штаб-квартир, если двигаться от
 каждой штаб-квартиры не более чем через L промежуточных городов. Перечислите
 номера таких городов в порядке возрастания. Нумерация городов начинается с 1. Если
 таких городов нет, выведите число (-1)."""

#https://chat.deepseek.com


def read_adjacency_matrix(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().split()))
            matrix.append(row)
    return matrix

def get_reachable_cities(matrix, start, max_hops):
    n = len(matrix)
    reachable = set()
    reachable.add(start)
    current = {start}
    
    for _ in range(max_hops + 1):
        next_current = set()
        for city in current:
            for neighbor in range(n):
                if matrix[city][neighbor] == 1 and neighbor not in reachable:
                    reachable.add(neighbor)
                    next_current.add(neighbor)
        current = next_current
        if not current:
            break
    return reachable

def find_common_cities(filename, k1, k2, L):
    matrix = read_adjacency_matrix(filename)
    # Convert to 0-based indexing if necessary (assuming input is 1-based)
    k1 -= 1
    k2 -= 1
    
    reachable_k1 = get_reachable_cities(matrix, k1, L)
    reachable_k2 = get_reachable_cities(matrix, k2, L)
    
    common = reachable_k1 & reachable_k2
    common_sorted = sorted([city + 1 for city in common])  # Convert back to 1-based
    
    return common_sorted if common_sorted else [-1]

# Пример использования:
# result = find_common_cities("FileName.txt", K1, K2, L)
# print(result)

