'''
 CalcTree5. В текстовом файле с именем filename дано арифметическое выражение в
 префиксной форме. Операндами в выражении являются целые числа из промежутка от 0
 до 9. Используемые операции: сложение (+), вычитание (-), умножение (*) и деление
 нацело(/). Постройте дерево, соответствующее данному выражению. Знаки операций
 кодируйте числами: сложение(-1), вычитание(-2), умножение(-3), деление(-4).
 Преобразуйте дерево так, чтобы в нем не было операций сложения и вычитания. Иными
 словами, замените поддеревья, в которых есть сложение или вычитание значением
 данного поддерева. Выведите указатель на корень полученного дерева.
 
 Языковая модель: https://chatgptchatapp.com
 '''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(expression):
    """
    Строит дерево выражения из префиксной записи.
    """
    tokens = expression.split()
    index = 0

    def build_tree_recursive():
        nonlocal index
        token = tokens[index]
        index += 1

        if token.isdigit():
            return Node(int(token))
        else:
            node = Node(get_operation_code(token))  # Кодируем операции числами
            node.left = build_tree_recursive()
            node.right = build_tree_recursive()
            return node

    return build_tree_recursive()

def get_operation_code(op):
    """
    Возвращает числовой код для операции.
    """
    if op == "+":
        return -1
    elif op == "-":
        return -2
    elif op == "*":
        return -3
    elif op == "/":
        return -4
    else:
        raise ValueError("Неизвестная операция: {}".format(op))

def evaluate_tree(node):
    """
    Вычисляет значение поддерева.
    """
    if node.data >= 0:  # Операнд
        return node.data
    else:
        left_val = evaluate_tree(node.left)
        right_val = evaluate_tree(node.right)

        if node.data == -1:  # Сложение
            return left_val + right_val
        elif node.data == -2:  # Вычитание
            return left_val - right_val
        elif node.data == -3:  # Умножение
            return left_val * right_val
        elif node.data == -4:  # Деление
            return left_val // right_val  # Нацело
        else:
            raise ValueError("Неизвестный код операции: {}".format(node.data))

def transform_tree(root):
    """
    Преобразует дерево, удаляя операции сложения и вычитания.
    """
    if root is None:
        return None

    if root.data == -1 or root.data == -2:
        # Если корень - сложение или вычитание, заменяем поддерево значением
        return Node(evaluate_tree(root))
    else:
        # Иначе рекурсивно обрабатываем дочерние узлы
        root.left = transform_tree(root.left)
        root.right = transform_tree(root.right)
        return root

def read_expression_from_file(filename):
    """
    Считывает арифметическое выражение из файла.
    """
    try:
        with open(filename, 'r') as file:
            expression = file.readline().strip()
            return expression
    except FileNotFoundError:
        print("Файл не найден: {}".format(filename))
        return None
    except Exception as e:
        print("Ошибка при чтении файла: {}".format(e))
        return None
    
def print_tree(root):
    """
    Выводит дерево в инфиксной форме (для отладки).
    """
    if root:
        print_tree(root.left)
        print(root.data, end=" ")
        print_tree(root.right)

# Основная часть программы
filename = "expression.txt"  # Замените на имя вашего файла
expression = read_expression_from_file(filename)

if expression:
    tree = build_tree(expression)
    transformed_tree = transform_tree(tree)

    # Выводим указатель на корень преобразованного дерева (для демонстрации)
    print("Указатель на корень преобразованного дерева:", transformed_tree)

    # (Опционально) Выводим дерево для проверки (в инфиксной форме, для отладки)
    # print("Преобразованное дерево (инфиксная форма):")
    # print_tree(transformed_tree)

    # (Опционально) Выводим значение всего дерева
    #print("\nЗначение преобразованного дерева:", evaluate_tree(transformed_tree))