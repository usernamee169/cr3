def count_numbers_with_consecutive_zeros(K: int, N: int) -> int:
    """
    Подсчет K-ичных чисел из N разрядов с двумя+ подряд нулями
    
    Args:
        K: Основание системы счисления (2-10)
        N: Количество разрядов (2-19)
    
    Returns:
        Количество чисел, удовлетворяющих условию
    
    Raises:
        ValueError: Если параметры K или N выходят за допустимые пределы
    """
    if not 2 <= K <= 10:
        raise ValueError("K должно быть от 2 до 10")
        
    if not 2 <= N <= 19:
        raise ValueError("N должно быть от 2 до 19")

    dp = [[0, 0] for _ in range(N + 1)]
    dp[1][0] = 1    # "0"
    dp[1][1] = K - 1 # "1".."K-1"

    for i in range(2, N + 1):
        dp[i][0] = dp[i-1][1] # Добавляем 0 после не-нуля
        dp[i][1] = (dp[i-1][0] + dp[i-1][1]) * (K - 1) # Добавляем не-0 цифру

    total = K**N - K**(N-1) # Всего чисел без ведущих нулей
    valid = dp[N][0] + dp[N][1] # Числа без двух подряд нулей
    return total - valid


def main():
    """Основная функция для взаимодействия с пользователем"""
    print("Подсчет K-ичных чисел из N разрядов с двумя и более подряд нулями")
    
    while True:
        try:
            K = int(input("Введите основание системы счисления K (2-10): "))
            N = int(input("Введите количество разрядов N (2-19): "))
            
            result = count_numbers_with_consecutive_zeros(K, N)
            print(f"Количество чисел: {result}")
            break
            
        except ValueError as e:
            print(f"Ошибка: {e}\nПожалуйста, попробуйте снова.\n")
            
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
            break


if __name__ == "__main__":
    main()
