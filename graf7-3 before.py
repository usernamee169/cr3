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

Языковая модель: https://trychatgpt.ru
"""


def read_graph(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        matrix = [list(map(int, f.readline().split())) for _ in range(n)]
    return n, matrix

def reachable_cities(matrix, start, L):
    from collections import deque

    n = len(matrix)
    visited = set()
    queue = deque()
    
    # (current_city, depth)
    queue.append((start-1, 0))
    visited.add(start-1)

    reachable = set()

    while queue:
        city, depth = queue.popleft()
        if depth > L:
            continue
        reachable.add(city + 1)  # сохраняем номера с 1
        if depth == L:
            continue
        for nxt in range(n):
            if matrix[city][nxt] == 1 and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, depth + 1))
    
    return reachable

def main():
    FileName = 'input.txt'  # имя файла с графом
    K1 = int(input("Введите номер первого города-кандидата: "))
    K2 = int(input("Введите номер второго города-кандидата: "))
    L = int(input("Введите максимальное количество промежуточных городов: "))

    n, matrix = read_graph(FileName)

    reachable_from_K1 = reachable_cities(matrix, K1, L)
    reachable_from_K2 = reachable_cities(matrix, K2, L)

    intersection = sorted(reachable_from_K1.intersection(reachable_from_K2))

    if intersection:
        print(*intersection)
    else:
        print(-1)

if __name__ == "__main__":
    main()