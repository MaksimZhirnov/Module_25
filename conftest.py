from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('/tests_drivers/chromedriver.exe')

   pytest.driver.set_window_size(1400, 1000)
   # Переход на страницу авторизации
   pytest.driver.get('https://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()