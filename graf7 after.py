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
        except Exception as e:
            raise ValueError(f"Ошибка при чтении файла: {str(e)}")

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

    try:
        matrix = read_adjacency_matrix(filename)
        if start_city1 <= 0 or start_city2 <= 0:
            raise ValueError("Номера городов должны быть положительными числами")
        if max_hops < 0:
            raise ValueError("Максимальное количество переходов не может быть отрицательным")
        
        n = len(matrix)
        if start_city1 > n or start_city2 > n:
            raise ValueError(f"Номер города превышает количество городов в матрице (максимум {n})")
            
        reachable1 = get_reachable_cities(matrix, start_city1 - 1, max_hops)
        reachable2 = get_reachable_cities(matrix, start_city2 - 1, max_hops)
        
        common = sorted([city + 1 for city in reachable1 & reachable2])
        return common if common else [-1]
    except ValueError as e:
        print(f"Ошибка: {str(e)}")
        return [-1]
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")
        return [-1]


if __name__ == "__main__":
    try:
        # Пример использования
        filename = input("Введите путь к файлу с матрицей смежности: ")
        city1 = int(input("Введите номер первого города: "))
        city2 = int(input("Введите номер второго города: "))
        hops = int(input("Введите максимальное количество переходов: "))
        
        result = find_common_cities(filename, city1, city2, hops)
        print("Результат:", result)
    except Exception as e:
        print(f"Ошибка:"{e})
