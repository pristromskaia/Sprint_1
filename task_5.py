class TestCase:

    def __init__(self):
        self.steps = {}
        self.results = None
    
    #Метод set_step — добавляет в словарь steps шаг тест-кейса
    def set_step (self, step_number, step_text):
        self.steps[step_number] = step_text

    #Метод delete_step — удаляет из словаря steps шаг тест-кейса по его номеру
    def delete_step (self, step_number):
        del self.steps[step_number]
    
    #Метод set_result — устанавливает ожидаемый результат
    def set_result (self, result):
        self.results = result
    
    #Метод get_test_case — печатает информацию о составе тест-кейса
    def get_test_case (self):
        test_case_dict = {
            'Шаги': self.steps,
            'Ожидаемый результат': self.results
        }
        #
        print(test_case_dict)
        
test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 