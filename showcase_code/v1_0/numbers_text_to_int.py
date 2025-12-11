from difflib import get_close_matches as gcm
import math


NUMS_RAW = {
    'ноль': 0,
    'нуль': 0,
    'один': 1,
    'два': 2,
    'две': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
    'сто': 100,
    'двести': 200,
    'триста': 300,
    'четыреста': 400,
    'пятьсот': 500,
    'шестьсот': 600,
    'семьсот': 700,
    'восемьсот': 800,
    'девятьсот': 900,
    'тысяча': 10**3,
    'миллион': 10**6,
    'миллиард': 10**9,
    'триллион': 10**12,
}

OPERATORS = {
    'сложение': '+',
    'сложить с': '+',
    'прибавить': '+',
    'плюс': '+',
    'сложи': '+',
    'вычитание': '-',
    'отнять': '-',
    'минус': '-',
    'вычесть': '-',
    'умножение': '*',
    'умножить': '*',
    'перемножить': '*',
    'деление': '/',
    'поделить': '/',
    'расделить': '/',
    'разделить на': '/',
    'деление нацело': '//',
    'остаток от деления': '%',
    'возведение в степень': '**',
    'в степени': '**',
    'меньше': '<',
    'меньше или равно': '<=',
    'больше': '>',
    'больше или равно': '>=',
    'равно': '==',
    'равно ли': '==',
    'равен': '==',
    'не равно': '!=',
    'корень': 'sqrt',
}

DECIMALS = {
    'десятых': 1,
    'сотых': 2,
    'тысячных': 3,
}

def find_closest_input(word, dictionary):
    '''
    Find the closest input in the dictionary based on the word provided.

    Args:
        word (str): The word to find the closest match for.
        dictionary (dict): A dictionary containing possible inputs as keys.

    Returns:
        str: The closest match found in the dictionary, or None if no close match is found.

    --------------------------------------

    Найдите ближайшее входное значение в словаре на основе предоставленного слова.

    Аргументы:
    word (str): Слово, для которого нужно найти ближайшее соответствие.
    dictionary (dict): словарь, содержащий возможные входные данные в виде ключей.

    Возврат:
    str: ближайшее совпадение, найденное в словаре, или «Нет», если близкое совпадение не найдено.
    '''
    possible_inputs = list(dictionary.keys())
    closest_matches = gcm(word, possible_inputs, n=1, cutoff=0.8)
    if closest_matches:
        return closest_matches[0]
    return None

def apply_operator(operator, left, right):
    '''
    Apply the specified operator on the given operands and return the result.
    :param operator: The operator to apply (e.g., '+', '-', '*', '/', '//', '%', '**', 'sqrt')
    :param left: The left operand
    :param right: The right operand (only for binary operators)
    :return: The result of applying the operator on the operands

    --------------------------------------

    Примените указанный оператор к заданным операндам и верните результат.
    :param operator: Применяемый оператор (например, '+', '-', '*', '/', '//', '%', '**', 'sqrt')
    :param left: Левый операнд (число с лева)
    :param right: Правый операнд (число с права, только для бинарных операторов).
    :return: Результат применения оператора к операндам
    '''
    operator_functions = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '//': lambda x, y: x // y,
        '%': lambda x, y: x % y,
        '**': lambda x, y: x ** y,
        'sqrt': lambda x: math.sqrt(x)
    }
    if operator in operator_functions:
        if operator == 'sqrt':
            return operator_functions[operator](right)
        else:
            return operator_functions[operator](left, right)
    return None

def evaluate_expression(numbers, operators):
    """
    Evaluate an expression given a list of numbers and operators.

    Args:
        numbers (list): A list of numbers to be evaluated.
        operators (list): A list of operators to apply on the numbers.

    Returns:
        float: The result of the evaluated expression.

    --------------------------------------

    Вычислите выражение по списку чисел и операторов.

    Аргументы:
    numbers (list): список чисел, подлежащих оценке.
    operators (list): список операторов, применяемых к номерам.

    Возвращает:
    float: результат вычисленного выражения.
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '//': 2, '%': 2, '**': 3, 'sqrt': 4}
    while operators:
        max_precedence = max(precedence[op] for op in operators)
        for i, op in enumerate(operators):
            if precedence[op] == max_precedence:
                left = numbers[i]
                right = numbers[i + 1]
                result = apply_operator(op, left, right)
                numbers[i:i + 2] = [result]
                operators.pop(i)
                break
    return numbers[0]

def parse_number(words, num_dict):
    '''
    Parse a list of words representing numbers and convert them to numerical values based on the provided number dictionary.

    Args:
        words (list): A list of words representing numbers to be parsed.
        num_dict (dict): A dictionary mapping words to their corresponding numerical values.

    Returns:
        int: The total sum of the numerical values parsed from the input words.

    --------------------------------------

    Разберите список слов, представляющих числа, и преобразуйте их в числовые значения на основе предоставленного словаря чисел.

    Аргументы:
    words  (list): список слов, представляющих числа для анализа.
    num_dict (dict): словарь, отображающий слова в соответствующие числовые значения.

    Возвращает:
    int: общая сумма числовых значений, полученных из входных слов.
    '''
    result = 0
    for word in words:
        closest_match = find_closest_input(word, num_dict)
        if closest_match:
            result += num_dict[closest_match]
    return result

def parse_decimal_number(words, num_dict, decimal_dict):
    '''
    Parse a list of words representing a decimal number using the provided dictionaries for numbers and decimal places. 
    Calculate the decimal value based on the matched words and return the result.

    --------------------------------------

    Разберите список слов, представляющих десятичное число, используя предоставленные словари чисел и десятичных знаков. 
    Вычислите десятичное значение на основе совпадающих слов и верните результат.

    '''
    current_number = 0
    place_value = 1
    for word in words:
        closest_match = find_closest_input(word, num_dict)
        if closest_match:
            current_number = current_number * 10 + num_dict[closest_match]
        else:
            closest_match = find_closest_input(word, decimal_dict)
            if closest_match:
                place_value = 10 ** -decimal_dict[closest_match]
    decimal_result = current_number * place_value

    return decimal_result

def parse_number_expression(words, num_dict, decimal_dict):  
    '''
    Parse a number expression consisting of words representing integers and decimal places. 
    If the word 'и' is present in the input words list, split the expression into integer and decimal parts. 
    Convert the integer and decimal parts into numerical values using the provided dictionaries. 
    Combine the integer and decimal parts to get the final parsed number. 
    
    Return: 
     - float number. 

    --------------------------------------

    Разберает числовое выражение, состоящее из слов, представляющих целые числа и десятичные знаки.
    Если в списке входных слов присутствует слово «и», разбейте выражение на целую и десятичную части.
    Преобразуйте целую и десятичную части в числовые значения, используя предоставленные словари.
    Объедините целую и десятичную части, чтобы получить окончательное проанализированное число.

    Возвращает:
     - float число.
    '''
    if 'и' in words:
        split_index = words.index('и')
        integer_part_words = words[:split_index]
        decimal_part_words = words[split_index + 1:]
        integer_part = parse_number(integer_part_words, num_dict)
        decimal_place_word = find_closest_input(decimal_part_words[-1], decimal_dict)
        if decimal_place_word:
            place_value = 10 ** -decimal_dict[decimal_place_word]
        decimal_part_number_words = decimal_part_words[:-1]
        decimal_part = parse_number(decimal_part_number_words, num_dict)
        decimal_part *= place_value
        return integer_part + decimal_part
    else:
        return parse_number(words, num_dict)

def process_expressions(expressions, num_dict, decimal_dict):
    '''
    Process a list of expressions to calculate final numbers.

    Parameters:
    - expressions (list): A list of expressions to be processed.
    - num_dict (dict): A dictionary mapping number words to their numerical values.
    - decimal_dict (dict): A dictionary mapping decimal place words to their corresponding values.

    Returns:
    - list: A list of final numbers calculated from the expressions.

    --------------------------------------

    Обработайте список выражений для вычисления окончательных чисел.

    Параметры:
    - выражения (список): список выражений, подлежащих обработке.
    - num_dict (dict): словарь, отображающий числовые слова в их числовые значения.
    - decimal_dict (dict): словарь, сопоставляющий слова с десятичными знаками их соответствующим значениям.

    Возвращает:
    - list: список итоговых чисел, рассчитанных на основе выражений.
    '''
    final_numbers = []
    for expr in expressions:
        final_number = parse_number_expression(expr, num_dict, decimal_dict)
        final_numbers.append(final_number)
    return final_numbers

def split_by_operators(input_string, operators):
    '''
    Split the input string by the provided operators.
    Parameters:
    - input_string: A string containing the expression to be split.
    - operators: A dictionary mapping words to their corresponding operators.
    Returns:
    - A tuple containing a list of expressions split by operators and a list of operators used.

    --------------------------------------

    Разделяет входную строку с помощью предоставленных операторов.
    Параметры:
    - input_string: строка, содержащая выражение, которое нужно разделить.
    - operators: словарь, отображающий слова на соответствующие им операторы.

    Возвращает:
    - Кортеж, содержащий список выражений, разделенных по операторам, и список используемых операторов.
    '''

    words = input_string.split()
    current_expression = []
    expressions = []
    operator_list = []

    for word in words:
        closest_match = find_closest_input(word, operators)
        if closest_match:
            operator = operators[closest_match]
            if current_expression:
                expressions.append(current_expression)
                current_expression = []
            operator_list.append(operator)
        else:
            current_expression.append(word)

    if current_expression:
        expressions.append(current_expression)

    return expressions, operator_list

def reading_start(string_input):
    '''
    Reads a string input, processes expressions split by operators, 
    calculates final numbers using numerical and decimal dictionaries, 
    determines decimal places, evaluates the expression, and returns the rounded result 
    or an exception if encountered.
    --------------------------------------
    Считывает введенную строку, обрабатывает выражения, разделенные операторами, 
    вычисляет окончательные числа с использованием числовых и десятичных словарей, 
    определяет десятичные знаки, оценивает выражение и возвращает округленный 
    результат или исключение, если оно встречается.
    '''
    expressions, operators = split_by_operators(string_input, OPERATORS)
    if expressions:
        numbers = process_expressions(expressions, NUMS_RAW, DECIMALS)
        decimal_places = 0
        for expr in expressions:
            for word in expr:
                decimal_place_word = find_closest_input(word, DECIMALS)
                if decimal_place_word:
                    decimal_places = DECIMALS[decimal_place_word]
                    break
        try:
            result = evaluate_expression(numbers, operators)
            return round(result, decimal_places)
        except Exception as e:
            return (F"калькулятор сломался")
    else:
        return
