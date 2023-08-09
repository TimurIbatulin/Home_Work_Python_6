''' Задача: Расчет финансовых показателей портфеля акций
Описание задачи:
Вы являетесь инвестором и хотите создать программу для расчета нескольких финансовых показателей вашего портфеля акций. Создайте модуль Python под названием "portfolio.py", который будет содержать функции для выполнения следующих операций:
Расчет общей стоимости портфеля акций: Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float принимает два аргумента: stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.), и значениями - количество акций каждого символа. prices - словарь, где ключами являются символы акций, а значениями - текущая цена каждой акции. Функция должна вернуть общую стоимость портфеля акций на основе количества акций и их текущих цен. Пример: Пришло
stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
Вышло:
16410,25
'''
'''
Расчет доходности портфеля: Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float принимает два аргумента: initial_value - начальная стоимость портфеля акций. current_value - текущая стоимость портфеля акций. Функция должна вернуть процентную доходность портфеля. Пример:
Пришло:
10000.0
15000.0
Вышло:
50%
'''
'''
Определение наиболее прибыльной акции: Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str принимает два аргумента: stocks - словарь с акциями и их количеством. prices - словарь с акциями и их текущими ценами. Функция должна вернуть символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью. Начальная стоимость - первый вызов calculate_portfolio_value, данные из этого вызова следует сохранить в защищенную переменную на уровне модуля.
Пример:
Пришло: 
stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
Вышло:
MSFT

Тестирование модуля:
Напишите небольшую программу, которая импортирует модуль "portfolio.py" и демонстрирует использование всех трех функций.
Создайте словари для акций и цен, запустите функции и выведите результаты.
Примечание:
В реальном мире вы можете использовать API для получения актуальных данных о ценах акций. В данной задаче можно использовать фиктивные данные для тестирования и обучения
'''
_INSIDE_STOCKS = {}
_INSIDE_PRICES = {}
def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    _INSIDE_STOCKS = stocks
    global _INSIDE_PRICES
    _INSIDE_PRICES = prices
    calculete = 0
    for a in stocks:
        for b in prices:
            if a == b:
                buffer = stocks.get(a) * prices.get(b)
                calculete += buffer
    return calculete

def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    diferent = current_value - initial_value
    persent_diferent = diferent/(initial_value/100)
    return persent_diferent

def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    global _INSIDE_PRICES
    name_shares = None
    diferent_prise = 0
    diferent_prise_1 = 0
    for a in prices:
        for b in _INSIDE_PRICES:
            if a == b:
                diferent_prise = prices.get(a) - _INSIDE_PRICES.get(b)
                if diferent_prise > diferent_prise_1:
                    diferent_prise_1 = diferent_prise
                    name_shares = a
    return name_shares







