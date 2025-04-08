import pytest
from sort import get_order, check_str, sort_string


@pytest.mark.smoke
@pytest.mark.crit_path
@pytest.mark.parametrize(
    'order, string, sorted_string',
    [
        ('З<С<К', 'КСККСЗСКЗ', 'ЗЗСССКККК'),
        ('К<С', 'СКССК', 'ККССС')
    ],
    ids=['Sort: order 3 letters, string 9 chars', 'Sort: order 2 letters, string 5 chars', ]
)
def test_sort_valid(order, string, sorted_string):
    assert sort_string(order, string) == sorted_string

@pytest.mark.extended
@pytest.mark.parametrize(
    'order, string, err_message',
    [
        ('З<С<К', 'КСККС', 'Правило и строка должны содержать одинаковые буквы'),
        ('К<С', 'ЗКСЗК', 'Правило и строка должны содержать одинаковые буквы'),
    ],
    ids=['Sort: char in order not present in a string', 'Sort: char in string not present in an order', ]
)
def test_sort_invalid(order, string, err_message):
    with pytest.raises(ValueError, match=err_message):
        sort_string(order, string)


@pytest.mark.crit_path
@pytest.mark.parametrize(
    'order, output_order',
    [
        ('К<З', 'КЗ'),
        ('З<С<К', 'ЗСК')
    ],
    ids=['Order: length is 2 letters', 'Order: length is 3 letters']
)
def test_order_valid(order, output_order):
    assert get_order(order) == output_order

@pytest.mark.extended
@pytest.mark.parametrize(
    'order, err_message',
    [
        (' ', 'В правиле некорректный символ " ". Для правила можно ввести только символы З, С, К и знак "<"'),
        ('', 'Правило должно содержать минимум 2 буквы'),
        ('К', 'Правило должно содержать минимум 2 буквы'),
        ('З<С<К<З', 'Правило не должно содержать повторяющиеся буквы'),
        ('З<С<К<З<З<С<К<З<З<С<К<З', 'Правило не должно содержать повторяющиеся буквы'),
        ('з', 'В правиле некорректный символ "з". Для правила можно ввести только символы З, С, К и знак "<"'),
        ('с', 'В правиле некорректный символ "с". Для правила можно ввести только символы З, С, К и знак "<"'),
        ('к', 'В правиле некорректный символ "к". Для правила можно ввести только символы З, С, К и знак "<"'),
        ('А', 'В правиле некорректный символ "А". Для правила можно ввести только символы З, С, К и знак "<"'),
        ('б', 'В правиле некорректный символ "б". Для правила можно ввести только символы З, С, К и знак "<"'),
        ('K', 'В правиле некорректный символ "K". Для правила можно ввести только символы З, С, К и знак "<"'),
        ('&^', 'В правиле некорректный символ "&". Для правила можно ввести только символы З, С, К и знак "<"'),
        ('С36', 'В правиле некорректный символ "3". Для правила можно ввести только символы З, С, К и знак "<"'),
        ('😀', 'В правиле некорректный символ "😀". Для правила можно ввести только символы З, С, К и знак "<"'),
        ('日', 'В правиле некорректный символ "日". Для правила можно ввести только символы З, С, К и знак "<"'),
        ('К<К', 'Правило не должно содержать повторяющиеся буквы'),
    ],
    ids=['Order: space', 'Order: empty string', 'Order: length is 1 letter', 'Order: length is 4 letters', 'Order: length is 12 letters', 
         'Order: lowercase of a valid cyrillic char з', 'Order: lowercase of a valid cyrillic char с', 'Order: lowercase of a valid cyrillic char к',
         'Order: invalid uppercase cyrillic char', 'Order: invalid lowercase cyrillic char', 'Order: invalid latin char', 
         'Order: & char', 'Order: integer', 'Order: emoji', 'Order: hieroglyph', 'Order: duplicate valid letter', ]
)
def test_order_invalid(order, err_message):
    with pytest.raises(ValueError, match=err_message):
        get_order(order)


@pytest.mark.crit_path
@pytest.mark.parametrize(
    'string',
    [
        ('ЗЗ'),
        ('КСК'),
        ('ЗКСЗКЗЗ'),
        ('КККККСЗСЗС')
    ],
    ids=['String: length is 2 letters', 'String: length is 3 letters', 'String: length is 7 letters', 'String: length is 10 letters']
)
def test_string_valid(string):
    assert check_str(string) == string

@pytest.mark.extended
@pytest.mark.parametrize(
    'string, err_message',
    [
        ('С К', 'В строке некорректный символ " ". Для сортировки можно ввести только символы З, С, К'),
        ('', 'Введите строку от 2 до 10 символов включительно'),
        ('З', 'Введите строку от 2 до 10 символов включительно'),
        ('СЗКЗСЗКЗКЗС', 'Введите строку от 2 до 10 символов включительно'),
        ('СССКЗКЗКЗССССЗЗКСЗСССКЗКЗКЗССССЗЗКСЗСССКЗКЗКЗССССЗЗКСЗ', 'Введите строку от 2 до 10 символов включительно'),
        ('зЗ', 'В строке некорректный символ "з". Для сортировки можно ввести только символы З, С, К'),
        ('Кс', 'В строке некорректный символ "с". Для сортировки можно ввести только символы З, С, К'),
        ('кКККС', 'В строке некорректный символ "к". Для сортировки можно ввести только символы З, С, К'),
        ('КСЧ', 'В строке некорректный символ "Ч". Для сортировки можно ввести только символы З, С, К'),
        ('ъжК', 'В строке некорректный символ "ъ". Для сортировки можно ввести только символы З, С, К'),
        ('KZ', 'В строке некорректный символ "K". Для сортировки можно ввести только символы З, С, К'),
        (';;"', 'В строке некорректный символ ";". Для сортировки можно ввести только символы З, С, К'),
        ('9К', 'В строке некорректный символ "9". Для сортировки можно ввести только символы З, С, К'),
        ('К😀З', 'В строке некорректный символ "😀". Для сортировки можно ввести только символы З, С, К'),
        ('日KC', 'В строке некорректный символ "日". Для сортировки можно ввести только символы З, С, К'),
    ], 
    ids=['String: space', 'String: empty string', 'String: length is 1 letter', 'String: length is 11 letters', 'String: length is 54 letters', 
         'String: lowercase of a valid cyrillic char з', 'String: lowercase of a valid cyrillic char с', 'String: lowercase of a valid cyrillic char к',
         'String: invalid uppercase cyrillic char', 'String: invalid lowercase cyrillic char', 'String: invalid latin char', 
         'String: ; char', 'String: integer', 'String: emoji', 'String: hieroglyph', ]
)
def test_string_invalid(string, err_message):
    with pytest.raises(ValueError, match=err_message):
        check_str(string)
