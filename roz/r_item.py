from datetime import date
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

phone_number = '9669553456'


def main():
    url = 'https://russia.znanierussia.ru/slot/parad-planet-chyornye-dyry-i-opasnye-asteroidy-issledovaniya-neb-66622/'

    wd = webdriver.Chrome()

    wd.maximize_window()

    wd.get(url)

    time.sleep(10)

    register_btn = wd.find_element(By.CLASS_NAME, 'RegistrationBlock_button__tD_EH')
    register_btn.click()
    time.sleep(2)

    another_method_btn = wd.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/button')
    another_method_btn.click()
    time.sleep(3)

    input_field = wd.find_element(By.XPATH, '//*[@id="phone"]')

    input_field.send_keys(phone_number)

    time.sleep(20)


if __name__ == '__main__':
    main()
