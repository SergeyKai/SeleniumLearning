from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from random import randint

class_day = 'Day_dayNumber__aag3f'


def tail(wd: webdriver.Chrome):
    events = wd.find_elements(By.CLASS_NAME, 'Calendar_slot__Kb0cx')
    r_num = randint(0, len(events) - 1)
    print(r_num)
    print(events[r_num])
    wd.execute_script('window.scrollTo(0, 900);')
    time.sleep(2)

    events[r_num].click()
    time.sleep(30)


def main():
    # today = date.today().day
    url = 'https://russia.znanierussia.ru/'

    wd = webdriver.Chrome()
    wd.get(url)

    today_teg = wd.find_element(By.CLASS_NAME, 'Day_active__QCGbu').find_element(By.CLASS_NAME, class_day)

    today = int(today_teg.text)

    current_days = range(today, today + 5 + 1)

    current_mont = today_teg.find_element(By.XPATH, '../../..').find_elements(By.CLASS_NAME, 'Day_dayWrapper__X8TwM')

    time.sleep(2)
    for day in current_mont:
        if day.find_element(By.CLASS_NAME, 'Day_dayName__3_opY').text.strip().lower() == 'пн':
            continue
        try:
            date = int(day.find_element(By.CLASS_NAME, 'Day_dayNumber__aag3f').text)
            if date in current_days:
                print(day.find_element(By.CLASS_NAME, 'Day_dayNumber__aag3f').text)
                if date == today + 5:
                    print('---')
                    day.click()
                    time.sleep(1)
                    tail(wd)
                    break
        except ValueError:
            pass


if __name__ == '__main__':
    main()
