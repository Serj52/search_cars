''' Импорты'''
import base64
import json



def decoded_file(path: str) -> dict:
    """ Декодирование файла """
    try:
        with open(path) as file:
            text = file.read()  # type: str
            text_decode = base64.b64decode(text).decode('UTF-8')  # type: str
            result = json.loads(text_decode)  # type: dict
            return result
    except FileNotFoundError as error:
        print('Файл не найден')
        raise error
    except ValueError as error:
        print('Данные в файле невозможно декодировать')
        raise error


def add_list(cars=None, customer=None, list_result=None, available_price=None) -> list:
    """Добавление в итоговый лист результатов поиска доступных автомобилей"""

    # Баланса не хвататет для покупки автомобиля
    if available_price is None:
        list_result.append("{} {} dosn't have money".format(customer['lastaname'],
                                                            customer['firstname']))
    else:
        for price in available_price:
            for car in cars:
                # Поиск автомобиля по цене
                if price in car.values():
                    list_result.append('Car {} {} can be offered for {} {}'.
                                       format(car['brand'], car['model'],
                                              customer['firstname'], customer['lastaname']))

    return list_result

def search_car(shop: dict) -> list:
    """ Поиск автомобилей для покупателей"""
    list_result = []  # type:list
    cars = shop['cars']  # type:list
    customers = shop['customers']  # type:list
    # Получение списка цен автомобилей и их сортировка
    cars_prices = sorted([price['price'] for price in cars]) # type:list
    # Поиск доступных автомобилей спомощью бинарного поиска
    # - на случай большого кол-ва предложений по автомобилям.
    for customer in customers:
        low = 0  # type:int
        high = len(cars_prices) - 1  # type:int
        # Находим средний индекс последовательности
        index = (low + high) // 2 # type:int
        balance_cent = customer['balance'] * 100 # type:int
        # Если баланс текущего покупателя меньше самой низкой цены автомобиля
        if balance_cent < min(cars_prices):
            # Добавление результата в итоговый список
            add_list(cars, customer, list_result)
            continue
            # Поиск максимально доступной цены автомобилей
        while index <= (len(cars_prices) - 1):
            # 1. Если текущая цена меньше баланса проверяем слудущую в списке
            if balance_cent < cars_prices[index]:
                # Если следущая цена в списке меньше баланса, то заканчиваем поиск доступных цен
                if balance_cent > cars_prices[index - 1]:
                    # Доступные цены автомобилей
                    available_price = cars_prices[:(index - 1) + 1]
                    # Добавление результата в итоговый список
                    add_list(cars, customer, list_result, available_price)
                    break
                # Если следущая цена в списке все равно больше баланса, то уменьшаем индекс,
                # берем следущую цену
                high = index - 1
                index = (low + high) // 2
            # 2. Если баланс больше текущей цены
            elif balance_cent > cars_prices[index]:
                # Если текущий индекс последний в списке:
                if index == (len(cars_prices) - 1):
                    # Доступные цены автомобилей
                    available_price = cars_prices[:index + 1]
                    # Добавление результата в итоговый список
                    add_list(cars, customer, list_result, available_price)
                    break
                # Если следущая цена в списке все равно меньше баланса,
                # то увеличиваем индекс, берем следущую цену
                low = index + 1
                index = (low + high) // 2

    return list_result


if __name__ == '__main__':
    shop_decoded = decoded_file('text')  # type:dict
    print(search_car((shop_decoded)))
