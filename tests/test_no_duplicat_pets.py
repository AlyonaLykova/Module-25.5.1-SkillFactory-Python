import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_no_duplicate_pets(go_to_my_pets):
    '''Поверяем что на странице со списком моих питомцев нет повторяющихся питомцев'''

    # Устанавливаем явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    # Сохраняем в переменную pet_data элементы с данными о питомцах
    data_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Настраиваем неявные ожидания:
    pytest.driver.implicitly_wait(10)

    # Проверяем, что в списке нет повторяющихся питомцев:
    list_data_my_pets = []
    for i in range(len(data_my_pets)):
        list_data = data_my_pets[i].text.split("\n")  # отделяем от данных питомца "х" удаления питомца
        list_data_my_pets.append(list_data[0])  # выбираем элемент с данными питомца и добавляем его в список
    set_data_my_pets = set(list_data_my_pets)  # преобразовываем список в множество
    assert len(list_data_my_pets) == len(set_data_my_pets)  # сравниваем длину списка и множества: без повторов должны совпасть

# python -m pytest -v --driver Chrome --driver-path /tests/chromedriver.exe tests/test_no_duplicat_pets.py