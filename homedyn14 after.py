#Исходный код: Модель https://chatgptchatapp.com

def count_numbers_with_consecutive_zeros(K: int, N: int) -> int:
    """
    Подсчет K-ичных чисел из N разрядов с двумя+ подряд нулями
    
    Args:
        K: Основание системы счисления (2-10)
        N: Количество разрядов (2-19)
    
    Returns:
        Количество чисел, удовлетворяющих условию
    """
    if not 2 <= K <= 10:
        raise ValueError("K должно быть от 2 до 10")
    if not 2 <= N <= 19:
        raise ValueError("N должно быть от 2 до 19")

    # dp[i][0] - числа длины i, оканчивающиеся на 0
    # dp[i][1] - числа длины i, оканчивающиеся не на 0
    dp = [[0, 0] for _ in range(N + 1)]
    dp[1][0] = 1    # "0"
    dp[1][1] = K - 1 # "1".."K-1"

    for i in range(2, N + 1):
        dp[i][0] = dp[i-1][1] # Добавляем 0 после не-нуля
        dp[i][1] = (dp[i-1][0] + dp[i-1][1]) * (K - 1) # Добавляем не-0 цифру

    total = K**N - K**(N-1) # Всего чисел без ведущих нулей
    valid = dp[N][0] + dp[N][1] # Числа без двух подряд нулей
    return total - valid

result = count_numbers_with_consecutive_zeros(3, 5)
print(result)

# Вывод документации с использованием артибута __doc__:
print(count_numbers_with_consecutive_zeros.__doc__)