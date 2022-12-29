import pytest
from settings import valid_email, valid_password
from selenium.webdriver.common.by import By

def test_show_pet_friends():
   '''Проверка карточек питомцев'''

   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)

   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   assert names[0].text != ''

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ',' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

# python -m pytest -v --driver Chrome --driver-path /tests/chromedriver.exe tests/test_show_pet_friends.py

# Тест упал, так как не все карточки питомца имеют фото (отсутствует атрибут 'src')