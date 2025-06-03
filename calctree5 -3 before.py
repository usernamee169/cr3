'''
 CalcTree5. В текстовом файле с именем filename дано арифметическое выражение в
 префиксной форме. Операндами в выражении являются целые числа из промежутка от 0
 до 9. Используемые операции: сложение (+), вычитание (-), умножение (*) и деление
 нацело(/). Постройте дерево, соответствующее данному выражению. Знаки операций
 кодируйте числами: сложение(-1), вычитание(-2), умножение(-3), деление(-4).
 Преобразуйте дерево так, чтобы в нем не было операций сложения и вычитания. Иными
 словами, замените поддеревья, в которых есть сложение или вычитание значением
 данного поддерева. Выведите указатель на корень полученного дерева.
 
 Языковая модель: https://giga.chat
 '''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(tokens):
    if not tokens:
        return None
    
    # Получаем первый элемент списка (операцию или число)
    token = tokens.pop()
    
    # Если токен — операция, создаем узел и рекурсивно строим левое и правое поддерево
    if isinstance(token, int) and token < 0:
        node = TreeNode(token)
        node.right = build_tree(tokens)
        node.left = build_tree(tokens)
    else:
        # Иначе токен — число, создаём листовой узел
        node = TreeNode(int(token))
        
    return node


# Функция оценки значения поддерева
def evaluate(node):
    if node is None:
        return 0
    
    # Если узел — число, возвращаем его значение
    if node.value >= 0:
        return node.value
    
    left_value = evaluate(node.left)
    right_value = evaluate(node.right)
    
    # Вычисление результата в зависимости от типа операции
    if node.value == -1:  # +
        result = left_value + right_value
    elif node.value == -2:  # -
        result = left_value - right_value
    elif node.value == -3:  # *
        result = left_value * right_value
    elif node.value == -4:  # /
        result = left_value // right_value
    
    return result


# Удаляет операции сложения и вычитания путем замены узлов результатами вычислений
def remove_add_subtract(root):
    if root is None or root.value >= 0:
        return root
    
    # Обрабатываем сначала потомков
    root.left = remove_add_subtract(root.left)
    root.right = remove_add_subtract(root.right)
    
    # Если узел — сложение или вычитание, заменяем его результатом
    if root.value in [-1, -2]:
        new_value = evaluate(root)
        root.value = new_value
        root.left = None
        root.right = None
    
    return root


# Функция печати дерева (для проверки)
def print_tree_inorder(node):
    if node is None:
        return
    print_tree_inorder(node.left)
    print(f'Value: {node.value}')
    print_tree_inorder(node.right)


# Основная программа
if __name__ == "__main__":
    import sys
    input_file = 'filename'
    with open(input_file, 'r') as f:
        expression = f.read().strip()  # Читаем данные из файла
    
    tokens = list(reversed(expression.split()))  # Разбиваем строку на токены и переворачиваем список
    
    # Переводим знаки операций в коды
    for i in range(len(tokens)):
        if tokens[i] == '+':
            tokens[i] = '-1'
        elif tokens[i] == '-':
            tokens[i] = '-2'
        elif tokens[i] == '*':
            tokens[i] = '-3'
        elif tokens[i] == '/':
            tokens[i] = '-4'
    
    # Построение исходного дерева
    tree_root = build_tree(tokens)
    
    # Убираем сложение и вычитание
    final_root = remove_add_subtract(tree_root)
    
    # Печать итогового дерева (опционально)
    print("Final tree:")
    print_tree_inorder(final_root)
