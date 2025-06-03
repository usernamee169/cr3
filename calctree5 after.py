class TreeNodeClass:
    """Класс для представления узла бинарного дерева выражений.
    
    Attributes:
        value (int): Значение узла (операнд или код операции)
        left (TreeNodeClass): Левый потомок
        right (TreeNodeClass): Правый потомок
    """
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def build_expression_tree(tokens: list[str]) -> TreeNodeClass:
    """Строит дерево выражения из префиксной записи.
    
    Args:
        tokens: Список токенов выражения в префиксной форме
        
    Returns:
        TreeNode: Корень построенного дерева выражений
        
    Raises:
        ValueError: Если выражение содержит недопустимые токены
    """
    def rec() -> TreeNodeClass:
        """Рекурсивное построение дерева."""
        nonlocal index
        if index >= len(tokens):
            raise ValueError("Недостаточно токенов в выражении")
            
        token = tokens[index]
        index += 1
        
        if token.isdigit():
            return TreeNodeClass(int(token))
        try:
            node = TreeNodeClass(operation_to_code(token))
            node.left = rec()
            node.right = rec()
            return node
        except KeyError:
            raise ValueError(f"Недопустимый оператор: {token}")
    
    index = 0
    return rec()


def operation_to_code(op: str) -> int:
    """Конвертирует оператор в числовой код.
    
    Args:
        op: Строковое представление оператора (+, -, *, /)
        
    Returns:
        int: Числовой код операции
        
    Raises:
        KeyError: Если оператор не поддерживается
    """
    return {
        '+': -1,
        '-': -2,
        '*': -3,
        '/': -4
    }[op]


def evaluate_tree(node: TreeNodeClass) -> int:
    """Вычисляет значение поддерева.
    
    Args:
        node: Корень поддерева для вычисления
        
    Returns:
        int: Результат вычисления поддерева
        
    Raises:
        ValueError: Если встречена неизвестная операция
    """
    if node is None:
        return 0
    if node.value >= 0: 
        return node.value
    
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    
    if node.value == -1: 
        return left_val + right_val
    elif node.value == -2: 
        return left_val - right_val
    elif node.value == -3: 
        return left_val * right_val
    elif node.value == -4:  
        return left_val // right_val
    else:
        raise ValueError(f"Неизвестная операция: {node.value}")


def replace_add_sub_with_values(node: TreeNode) -> TreeNode:
    """Заменяет поддеревья с сложением/вычитанием на их значения.
    
    Args:
        node: Корень дерева для преобразования
        
    Returns:
        TreeNodeClass: Корень преобразованного дерева
    """
    if node is None:
        return None
    
    if node.value in (-1, -2): 
        return TreeNodeClass(evaluate_tree(node))
    
    node.left = replace_add_sub_with_values(node.left)
    node.right = replace_add_sub_with_values(node.right)
    return node


def process_expression(filename: str) -> TreeNodeClass:
    """Обрабатывает выражение из файла и возвращает преобразованное дерево.
    
    Args:
        filename: Путь к файлу с выражением
        
    Returns:
        TreeNodeClass: Корень преобразованного дерева
        
    Raises:
        IOError: Если файл не может быть прочитан
        ValueError: Если выражение некорректно
    """
    try:
        with open(filename, 'r') as file:
            expression = file.read().strip()
    except IOError as e:
        raise IOError(f"Ошибка чтения файла: {e}")
    
    if not expression:
        raise ValueError("Файл пуст")
    
    tokens = expression.split()
    if not tokens:
        raise ValueError("Нет токенов для обработки")
    
    root = build_expression_tree(tokens)
    return replace_add_sub_with_values(root)


if __name__ == "__main__":
    try:
        with open('expression.txt', 'w') as f:
            f.write("+ * 3 4 - 5 2")  
        
        root = process_expression('expression.txt')
        print("Преобразование выполнено успешно")
        print(root)
        
    except Exception as e:
        print(f"Ошибка: {e}")
