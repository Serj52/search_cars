'''Импорты'''
import unittest
from .task import search_car, add_list


class MyTest(unittest.TestCase):
    """Класс по тестирования функций search_car(), add_list()"""
    def test_first_search_car(self) -> None:
        """Только один покупатель John Perry себе может позволить купить авто"""
        result = ["Conor John dosn't have money",
                  "Shultz Alex dosn't have money",
                  "Taker Max dosn't have money",
                  'Car Ford Bronco can be offered for John Perry',
                  'Car Pontiac GTO 1964 can be offered for John Perry',
                  'Car Rolls Royce Ghost can be offered for John Perry',
                  "Smith Ann dosn't have money"]

        shop = {'cars': [
            {'id': '593ecb64-c393-4882-bc5e-59f0fc32acca',
             'brand': 'Rolls Royce', 'model': 'Ghost',
             'color': 'silver', 'price': 5285714},
            {'id': 'e1cca2d3-e39b-44b8-b694-7fa12305152a',
             'brand': 'Pontiac', 'model': 'GTO 1964',
             'color': 'green', 'price': 2642857},
            {'id': '5ec55bd7-1747-4c28-b324-bd0c62ff5463',
             'brand': 'Ford', 'model': 'Bronco', 'color': 'brown',
             'price': 857142}],
                'customers': [
                    {'id': 'b0a252c0-6385-4788-8256-29cf09095094',
                     'firstname': 'John', 'lastaname': 'Conor', 'balance': 123},
                    {'id': 'cffd5598-61af-49e4-aae6-0e8eb0f1efaf',
                     'firstname': 'Alex', 'lastaname': 'Shultz', 'balance': 859},
                    {'id': '0d45d35b-89ee-4d81-9d06-85af8ea0dee6',
                     'firstname': 'Max', 'lastaname': 'Taker', 'balance': 2903},
                    {'id': '359ee85a-e647-4cc4-9146-4a18dc83ab2f',
                     'firstname': 'John', 'lastaname': 'Perry', 'balance': 98470},
                    {'id': 'be01232b-3f63-4414-a9db-98438beb8153',
                     'firstname': 'Ann', 'lastaname': 'Smith', 'balance': 578}]}
        self.assertEqual(result, search_car(shop))

        # Проверки:
        # -отсуствие повторений автомобилей у продавца,
        # -наличие всех покупателей в итоговом списке
        names = ['{} {}'.format(customer['lastaname'], customer['firstname'])
                 for customer in shop['customers']] # type:list
        amount_customers = len(shop['cars']) # type:int
        for name in names:
            count = 0 # type:int
            # Подсчет числа имен в итоговом результате
            for res in result:
                if name in res:
                    count += 1
            # Число имен в результате не должно превышать числа автомобилей
            self.assertLessEqual(count, amount_customers)


    def test_second_search_car(self) -> None:
        """Все покупатели себе могут позволить купить все авто"""
        result = ['Car Ford Bronco can be offered for John Conor',
                  'Car Pontiac GTO 1964 can be offered for John Conor',
                  'Car Rolls Royce Ghost can be offered for John Conor',
                  'Car Ford Bronco can be offered for Alex Shultz',
                  'Car Pontiac GTO 1964 can be offered for Alex Shultz',
                  'Car Rolls Royce Ghost can be offered for Alex Shultz',
                  'Car Ford Bronco can be offered for Max Taker',
                  'Car Pontiac GTO 1964 can be offered for Max Taker',
                  'Car Rolls Royce Ghost can be offered for Max Taker',
                  'Car Ford Bronco can be offered for John Perry',
                  'Car Pontiac GTO 1964 can be offered for John Perry',
                  'Car Rolls Royce Ghost can be offered for John Perry',
                  'Car Ford Bronco can be offered for Ann Smith',
                  'Car Pontiac GTO 1964 can be offered for Ann Smith',
                  'Car Rolls Royce Ghost can be offered for Ann Smith']

        shop = {'cars': [
            {'id': '593ecb64-c393-4882-bc5e-59f0fc32acca',
             'brand': 'Rolls Royce', 'model': 'Ghost', 'color': 'silver',
             'price': 5285714},
            {'id': 'e1cca2d3-e39b-44b8-b694-7fa12305152a',
             'brand': 'Pontiac', 'model': 'GTO 1964', 'color': 'green',
             'price': 2642857},
            {'id': '5ec55bd7-1747-4c28-b324-bd0c62ff5463',
             'brand': 'Ford', 'model': 'Bronco', 'color': 'brown',
             'price': 857142}],
                'customers': [
                    {'id': 'b0a252c0-6385-4788-8256-29cf09095094',
                     'firstname': 'John', 'lastaname': 'Conor',
                     'balance': 123000},
                    {'id': 'cffd5598-61af-49e4-aae6-0e8eb0f1efaf',
                     'firstname': 'Alex', 'lastaname': 'Shultz',
                     'balance': 85900},
                    {'id': '0d45d35b-89ee-4d81-9d06-85af8ea0dee6',
                     'firstname': 'Max', 'lastaname': 'Taker',
                     'balance': 290300},
                    {'id': '359ee85a-e647-4cc4-9146-4a18dc83ab2f',
                     'firstname': 'John', 'lastaname': 'Perry',
                     'balance': 984700},
                    {'id': 'be01232b-3f63-4414-a9db-98438beb8153',
                     'firstname': 'Ann', 'lastaname': 'Smith',
                     'balance': 57800}]}
        self.assertEqual(result, search_car(shop))

        # Проверки: -отсуствие повторений автомобилей у продавца,
        # -наличие всех покупателей в итоговом списке
        names = ['{} {}'.format(customer['lastaname'], customer['firstname'])
                 for customer in shop['customers']] # type: list
        amount_customers = len(shop['cars']) # type: int
        for name in names:
            count = 0
            # Подсчет числа имен в итоговом результате
            for res in result:
                if name in res:
                    count += 1
            # Число имен в результате не должно превышать числа автомобилей
            self.assertLessEqual(count, amount_customers)


    def test_third_search_car(self) -> None:
        """У Покупателей не могут позволить купить авто"""
        result = ["Conor John dosn't have money",
                  "Shultz Alex dosn't have money",
                  "Taker Max dosn't have money",
                  "Perry John dosn't have money"]
        shop = {'cars': [
            {'id': '593ecb64-c393-4882-bc5e-59f0fc32acca',
             'brand': 'Rolls Royce', 'model': 'Ghost', 'color': 'silver',
             'price': 5285714},
            {'id': 'e1cca2d3-e39b-44b8-b694-7fa12305152a',
             'brand': 'Pontiac', 'model': 'GTO 1964', 'color': 'green',
             'price': 2642857},
            {'id': '5ec55bd7-1747-4c28-b324-bd0c62ff5463',
             'brand': 'Ford', 'model': 'Bronco', 'color': 'brown',
             'price': 857142}],
                'customers': [{'id': 'b0a252c0-6385-4788-8256-29cf09095094',
                               'firstname': 'John', 'lastaname': 'Conor',
                               'balance': 12},
                              {'id': 'cffd5598-61af-49e4-aae6-0e8eb0f1efaf',
                               'firstname': 'Alex', 'lastaname': 'Shultz',
                               'balance': 85},
                              {'id': '0d45d35b-89ee-4d81-9d06-85af8ea0dee6',
                               'firstname': 'Max', 'lastaname': 'Taker',
                               'balance': 29},
                              {'id': '359ee85a-e647-4cc4-9146-4a18dc83ab2f',
                               'firstname': 'John', 'lastaname': 'Perry',
                               'balance': 98}]}
        self.assertEqual(result, search_car(shop))

        # Проверки:
        # -отсуствие повторений автомобилей у продавца,
        # -наличие всех покупателей в итоговом списке
        names = ['{} {}'.format(customer['lastaname'], customer['firstname'])
                 for customer in shop['customers']] # type: list
        amount_customers = len(shop['cars']) # type: int
        for name in names:
            count = 0
            # Подсчет числа имен в итоговом результате
            for res in result:
                if name in res:
                    count += 1
            # Число имен в результате не должно превышать числа автомобилей
            self.assertLessEqual(count, amount_customers)


    def test_fifth_search_car(self) -> None:
        """Проверка целостности данных на болшем числе покупателей"""
        result = ["Conor John dosn't have money",
                  'Car Ford Bronco can be offered for Alex Shultz',
                  'Car Ford Bronco can be offered for Max Taker',
                  'Car Pontiac GTO 1964 can be offered for Max Taker',
                  'Car Ford Bronco can be offered for John Perry',
                  'Car Pontiac GTO 1964 can be offered for John Perry',
                  'Car Rolls Royce Ghost can be offered for John Perry',
                  "Smith Ann dosn't have money",
                  "Nolan Kris dosn't have money", "Presli Elvis dosn't have money",
                  "Black Jon dosn't have money",
                  "Stone Kate dosn't have money"]

        shop = {'cars': [
            {'id': '593ecb64-c393-4882-bc5e-59f0fc32acca',
             'brand': 'Rolls Royce', 'model': 'Ghost', 'color': 'silver',
             'price': 5285714},
            {'id': 'e1cca2d3-e39b-44b8-b694-7fa12305152a',
             'brand': 'Pontiac', 'model': 'GTO 1964', 'color': 'green',
             'price': 2642857},
            {'id': '5ec55bd7-1747-4c28-b324-bd0c62ff5463',
             'brand': 'Ford', 'model': 'Bronco', 'color': 'brown',
             'price': 857142}],
                'customers': [{'id': 'b0a252c0-6385-4788-8256-29cf09095094',
                               'firstname': 'John', 'lastaname': 'Conor',
                               'balance': 1230},
                              {'id': 'cffd5598-61af-49e4-aae6-0e8eb0f1efaf',
                               'firstname': 'Alex', 'lastaname': 'Shultz',
                               'balance': 8591},
                              {'id': '0d45d35b-89ee-4d81-9d06-85af8ea0dee6',
                               'firstname': 'Max', 'lastaname': 'Taker',
                               'balance': 29030},
                              {'id': '359ee85a-e647-4cc4-9146-4a18dc83ab2f',
                               'firstname': 'John', 'lastaname': 'Perry',
                               'balance': 98470},
                              {'id': 'be01232b-3f63-4414-a9db-98438beb8153',
                               'firstname': 'Ann', 'lastaname': 'Smith',
                               'balance': 578},
                              {'id': 'be01232b-3f63-4414-a9db-98438beb8153',
                               'firstname': 'Kris', 'lastaname': 'Nolan',
                               'balance': 1000},
                              {'id': 'be01232b-3f63-4414-a9db-98438beb8153',
                               'firstname': 'Elvis', 'lastaname': 'Presli',
                               'balance': 1000},
                              {'id': 'be01232b-3f63-4414-a9db-98438beb8153',
                               'firstname': 'Jon', 'lastaname': 'Black',
                               'balance': 100},
                              {'id': 'be01232b-3f63-4414-a9db-98438beb8153',
                               'firstname': 'Kate', 'lastaname': 'Stone',
                               'balance': 1000}]}
        # Проверки:
        # -отсуствие повторений автомобилей у продавца,
        # -наличие всех покупателей в итоговом списке
        names = ['{} {}'.format(customer['lastaname'], customer['firstname'])
                 for customer in shop['customers']] # type: list
        amount_customers = len(shop['cars']) # type: int
        for name in names:
            count = 0
            # Подсчет числа имен в итоговом результате
            for res in result:
                if name in res:
                    count += 1
            # Число имен в результате не должно превышать числа автомобилей
            self.assertLessEqual(count, amount_customers)

    def test_add_list(self) -> None:
        """Проверка работы функции add_list"""
        shop = {'cars': [
            {'id': '593ecb64-c393-4882-bc5e-59f0fc32acca',
             'brand': 'Rolls Royce', 'model': 'Ghost',
             'color': 'silver', 'price': 5285714},
            {'id': 'e1cca2d3-e39b-44b8-b694-7fa12305152a',
             'brand': 'Pontiac', 'model': 'GTO 1964',
             'color': 'green', 'price': 2642857},
            {'id': '5ec55bd7-1747-4c28-b324-bd0c62ff5463',
             'brand': 'Ford', 'model': 'Bronco', 'color': 'brown',
             'price': 857142}],
                'customers': [{'id': 'b0a252c0-6385-4788-8256-29cf09095094',
                               'firstname': 'John', 'lastaname': 'Conor',
                               'balance': 12},
                              {'id': 'cffd5598-61af-49e4-aae6-0e8eb0f1efaf',
                               'firstname': 'Alex', 'lastaname': 'Shultz',
                               'balance': 8590},
                              {'id': '0d45d35b-89ee-4d81-9d06-85af8ea0dee6',
                               'firstname': 'Max', 'lastaname': 'Taker',
                               'balance': 29},
                              {'id': '359ee85a-e647-4cc4-9146-4a18dc83ab2f',
                               'firstname': 'John', 'lastaname': 'Perry',
                               'balance': 9889}]}
        list_result = [] # type: list
        cars = shop['cars'] # type: list
        customer = shop['customers'][0] # type: dict
        available_price = [price['price'] for price in cars] # type: list
        result = add_list(cars, customer, list_result, available_price) # type: list
        # Проверка равенства переданного списка цен авто и результата
        self.assertEqual(len(available_price), len(result))
        # Проверка работы функции при отсуствии денег у Покупателя
        result = add_list(cars, customer, list_result)
        self.assertIn("{} {} dosn't have money".format(customer['lastaname'],
                                                       customer['firstname']), result)


if __name__ == '__main__':
    unittest.main()
