#Исходный код: Модель https://chat.deepseek.com

def find_common_cities(filename: str, start_city1: int, start_city2: int, max_hops: int) -> list[int]:
    """
    Находит города, достижимые из двух заданных городов с ограничением на переходы.
    
    Args:
        filename: Путь к файлу с матрицей смежности
        start_city1: Номер первого города (1-based)
        start_city2: Номер второго города (1-based)
        max_hops: Максимальное количество переходов
    
    Returns:
        Список общих городов или [-1] если таких нет
    """
    
    def read_adjacency_matrix(file_path: str) -> list[list[int]]:
        try:
            with open(file_path, 'r') as file:
                n = int(file.readline())
                return [list(map(int, file.readline().split())) for _ in range(n)]
        except FileNotFoundError:
            raise ValueError(f"Файл {file_path} не найден")

    def get_reachable_cities(matrix: list[list[int]], start: int, hops: int) -> set[int]:
        reachable = {start}
        current = {start}
        
        for _ in range(hops + 1):
            next_level = set()
            for city in current:
                for neighbor, connected in enumerate(matrix[city]):
                    if connected and neighbor not in reachable:
                        reachable.add(neighbor)
                        next_level.add(neighbor)
            current = next_level
            if not current:
                break
        return reachable

    filename= "C:/Users/default.DESKTOP-QPN4G4J/Documents/university/code review/SRS03/Filename.txt"
    matrix = read_adjacency_matrix(filename)
    reachable1 = get_reachable_cities(matrix, start_city1 - 1, max_hops)
    reachable2 = get_reachable_cities(matrix, start_city2 - 1, max_hops)
    
    common = sorted([city + 1 for city in reachable1 & reachable2])
    return common if common else [-1]


result = find_common_cities("Filename.txt", 1, 2, 2)
print(result)

# Вывод документации с использованием артибута __doc__:
print(find_common_cities.__doc__)
