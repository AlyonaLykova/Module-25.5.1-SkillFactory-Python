import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_have_different_names(go_to_my_pets):
   '''Поверяем что на странице со списком моих питомцев, у всех питомцев разные имена'''

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   name_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Настраиваем неявные ожидания:
   pytest.driver.implicitly_wait(10)

   # Проверяем, что у всех питомцев разные имена:
   list_name_my_pets = []
   for i in range(len(name_my_pets)):
       list_name_my_pets.append(name_my_pets[i].text)
   set_pet_data = set(list_name_my_pets)  # преобразовываем список в множество
   assert len(list_name_my_pets) == len(set_pet_data)  # сравниваем длину списка и множества: без повторов должны совпасть

# python -m pytest -v --driver Chrome --driver-path /tests/chromedriver.exe tests/test_all_pets_have_different_name.py