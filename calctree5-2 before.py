'''
 CalcTree5. В текстовом файле с именем filename дано арифметическое выражение в
 префиксной форме. Операндами в выражении являются целые числа из промежутка от 0
 до 9. Используемые операции: сложение (+), вычитание (-), умножение (*) и деление
 нацело(/). Постройте дерево, соответствующее данному выражению. Знаки операций
 кодируйте числами: сложение(-1), вычитание(-2), умножение(-3), деление(-4).
 Преобразуйте дерево так, чтобы в нем не было операций сложения и вычитания. Иными
 словами, замените поддеревья, в которых есть сложение или вычитание значением
 данного поддерева. Выведите указатель на корень полученного дерева.
 
 Языковая модель: https://chat.deepseek.com
 '''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(tokens):
    def helper():
        nonlocal index
        if index >= len(tokens):
            return None
        token = tokens[index]
        index += 1
        if token.isdigit():
            return TreeNode(int(token))
        else:
            node = TreeNode(operation_to_code(token))
            node.left = helper()
            node.right = helper()
            return node
    
    index = 0
    return helper()

def operation_to_code(op):
    return {
        '+': -1,
        '-': -2,
        '*': -3,
        '/': -4
    }[op]

def evaluate_tree(node):
    if node is None:
        return 0
    if node.value >= 0:  # Это операнд
        return node.value
    
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    
    if node.value == -1:  # Сложение
        return left_val + right_val
    elif node.value == -2:  # Вычитание
        return left_val - right_val
    elif node.value == -3:  # Умножение
        return left_val * right_val
    elif node.value == -4:  # Деление
        return left_val // right_val

def replace_add_sub_with_values(node):
    if node is None:
        return None
    
    # Если текущий узел - операция сложения или вычитания
    if node.value in (-1, -2):
        # Вычисляем значение поддерева
        value = evaluate_tree(node)
        # Заменяем узел на новый с вычисленным значением
        return TreeNode(value)
    else:
        # Рекурсивно обрабатываем детей
        node.left = replace_add_sub_with_values(node.left)
        node.right = replace_add_sub_with_values(node.right)
        return node

def process_expression(filename):
    with open(filename, 'r') as file:
        expression = file.read().strip()
    
    tokens = expression.split()
    root = build_expression_tree(tokens)
    modified_root = replace_add_sub_with_values(root)
    return modified_root

# Пример использования:
# Создаем тестовый файл с выражением (например, "+ * 3 4 - 5 2" - префиксная запись для (3*4)+(5-2))
with open('expression.txt', 'w') as f:
    f.write("+ * 3 4 - 5 2")

# Получаем корень модифицированного дерева
root = process_expression('expression.txt')
