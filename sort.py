
# Создаем правило
def get_order(order_str):

    # Проверяем правило
    allowed_chars = {'З', 'С', 'К', '<'}
    for char in order_str:
        if char not in allowed_chars:
            raise ValueError(f'В правиле некорректный символ "{char}". Для правила можно ввести только символы З, С, К и знак "<"')

    no_spaces = order_str.replace(' ', '')
    split_letters = no_spaces.split('<')

    # Сохраняем правило
    order = ''.join(split_letters)

    if len(split_letters) != len(set(split_letters)):
        raise ValueError('Правило не должно содержать повторяющиеся буквы')
    elif len(order) < 1 or len(order)==0 or (order.isalpha and len(order)== 1):
        raise ValueError('Правило должно содержать минимум 2 буквы')
    elif no_spaces.count('<') != len(order)-1:
        raise ValueError('Пропишите знак "<" для всех букв')
       
    return order

# Проверяем строку
def check_str(input_str):

    if len(input_str) < 2 or len(input_str) > 10:
        raise ValueError('Введите строку от 2 до 10 символов включительно')
    
    allowed_chars = {'З', 'С', 'К'}
    for char in input_str:
        if char not in allowed_chars:
            raise ValueError(f'В строке некорректный символ "{char}". Для сортировки можно ввести только символы З, С, К')
    
    return input_str


# Сортируем строку
def sort_string(input_order, input_str):

    # Проверяем правило и строку
    checked_order = get_order(input_order)
    checked_str = check_str(input_str)

    if set(checked_order) != set(checked_str):
        raise ValueError('Правило и строка должны содержать одинаковые буквы')

    # Считаем частоту символов
    def get_histogram(str):
        d = dict()
        for letter in str:
            d[letter] = d.get(letter, 0) + 1
        return d
    
    h = get_histogram(checked_str)
    
    # Получаем отсортированную строку
    def get_sorted_str():

        order = checked_order

        l = [i * int(h.get(i, 0)) for i in order]
        sorted_str = ''.join(str(x) for x in l)

        return sorted_str
    
    return get_sorted_str()


if __name__ == '__main__':

    print('Привет! Я умею сортировать строки из трёх букв: К, С и З в том порядке, который нужен вам. \n'
          'Напишите строку для сортировки длиной от 2 до 10 символов и правило в формате З<С<К \n')
    
    while True:
        try:
            input_str = input('Введите строку, которую нужно будет отсортировать: ')
            check_str(input_str)
            break

        except ValueError as e:
            print('Ошибка:', e)
            print('Попробуйте ещё раз.\n')

        except KeyboardInterrupt:
            print('Работа программы завершена')
            break

    while True:
        try:
            input_order = input('Введите правило сортировки: ')
            get_order(input_order)
            break

        except ValueError as e:
            print('Ошибка:', e)
            print('Попробуйте ещё раз.\n')

        except KeyboardInterrupt:
            print('Работа программы завершена')
            break

    result = sort_string(input_order, input_str)
    print('Результат сортировки:', result)