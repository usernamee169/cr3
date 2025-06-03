#https://chatgptchatapp.com

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


ddef solve():
    def read_graph(filename):
        with open(filename, 'r') as f:
            n = int(f.readline().strip())
            matrix = []
            for _ in range(n):
                row = list(map(int, f.readline().strip().split()))
                matrix.append(row)
        return n, matrix

    def reachable_cities(start_city, graph, max_distance):
        n = len(graph)
        reachable = {start_city}
        queue = [(start_city, 0)]  # (city, distance)
        visited = {start_city}

        while queue:
            city, distance = queue.pop(0)
            if distance < max_distance:
                for neighbor in range(n):
                    if graph[city][neighbor] == 1 and neighbor not in visited:
                        reachable.add(neighbor)
                        queue.append((neighbor, distance + 1))
                        visited.add(neighbor)
        return reachable

    filename = input("Введите имя файла: ")
    K1 = int(input("Введите номер первого города-кандидата: ")) - 1  # adjust to 0-based index
    K2 = int(input("Введите номер второго города-кандидата: ")) - 1  # adjust to 0-based index
    L = int(input("Введите максимальное количество промежуточных городов: "))

    n, graph = read_graph(filename)

    reachable_from_K1 = reachable_cities(K1, graph, L)
    reachable_from_K2 = reachable_cities(K2, graph, L)

    intersecting_cities = sorted(list(reachable_from_K1.intersection(reachable_from_K2)))

    if intersecting_cities:
        result = [city + 1 for city in intersecting_cities] # adjust back to 1-based index
        print(*result)
    else:
        print(-1)

solve()