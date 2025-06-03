'''
 CalcTree5. В текстовом файле с именем filename дано арифметическое выражение в
 префиксной форме. Операндами в выражении являются целые числа из промежутка от 0
 до 9. Используемые операции: сложение (+), вычитание (-), умножение (*) и деление
 нацело(/). Постройте дерево, соответствующее данному выражению. Знаки операций
 кодируйте числами: сложение(-1), вычитание(-2), умножение(-3), деление(-4).
 Преобразуйте дерево так, чтобы в нем не было операций сложения и вычитания. Иными
 словами, замените поддеревья, в которых есть сложение или вычитание значением
 данного поддерева. Выведите указатель на корень полученного дерева.
 
 Языковая модель: https://trychatgpt.ru
 '''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(prefix_expr):
    if not prefix_expr:
        return None
    
    # Считываем текущий элемент
    value = prefix_expr.pop(0)
    node = TreeNode(value)

    # Если это оператор, строим поддеревья
    if value in [-1, -2, -3, -4]:  # Операторы
        node.left = build_tree(prefix_expr)
        node.right = build_tree(prefix_expr)

    return node

def transform_tree(node):
    if node is None:
        return None
    
    # Рекурсивно преобразуем левое и правое поддеревья
    node.left = transform_tree(node.left)
    node.right = transform_tree(node.right)

    # Если это сложение или вычитание, возвращаем значение поддерева
    if node.value in [-1, -2]:  # Сложение или вычитание
        return evaluate(node)

    return node

def evaluate(node):
    if node is None:
        return 0
    
    if isinstance(node.value, int):  # Если это число (операнд)
        return node.value
    
    left_value = evaluate(node.left)
    right_value = evaluate(node.right)

    if node.value == -1:  # Сложение
        return left_value + right_value
    elif node.value == -2:  # Вычитание
        return left_value - right_value
    elif node.value == -3:  # Умножение
        return left_value * right_value
    elif node.value == -4:  # Деление нацело
        return left_value // right_value

def print_tree(node):
    if not node:
        return
    print(f'Node: {node.value}')
    print_tree(node.left)
    print_tree(node.right)

def main(filename):
    with open(filename, 'r') as file:
        prefix_expr = list(map(int, file.read().strip().split()))

    root = build_tree(prefix_expr)
    
    transformed_root = transform_tree(root)

    print("Transformed tree root:", transformed_root.value)
    
if __name__ == "__main__":
    main('filename.txt')