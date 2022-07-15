from constant import CSS_SELECTOR, cookies
import time
from selenium import webdriver
from googleSheet_operations import updateStatus
from datetime import datetime
import random


def sent_linkedin_request(linkedin_url, linkedin_cookies, message):
    return 'sent '


def wait(t):
    time.sleep(t)


def random_wait(a, b):
    t = random.randint(a, b)
    wait(t)


def chrome_driver():
    driver_location = "C:/Users/gkhom/OneDrive/Desktop/chrome_driver/chromedriver"
    binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    CHROMEDRIVER_LOCATION = "C:/Users/gkhom/OneDrive/Desktop/chrome_driver/chromedriver"
    BINARY_LOCATION = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.binary_location = binary_location
    web_driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    return web_driver


def add_cookies_in_driver(driver):
    for cookie in cookies:
        driver.add_cookie(cookie)

    return driver


def connect_request_sent(driver, message, prospect_linkedin):
    is_sent = False
    # print(message)
    # url = f"https://www.linkedin.com/in/{prospect_linkedin}"
    url = prospect_linkedin

    if check_user(driver, message, url):
        is_sent = True

    return is_sent


def check_user(driver, message, url):
    request_sent = False
    try:
        driver.get(url)
        first_name = driver.find_element_by_css_selector(CSS_SELECTOR['profile_heading']).text.split(" ")[0]
        message = message.format(first_name)
        random_wait(2, 6)
        buttons = driver.find_element_by_css_selector(CSS_SELECTOR['buttons']).text.splitlines()
        print(buttons)
        random_wait(3, 6)
        # print(buttons)
        if buttons[0].lower() == "message" or buttons[0].lower() == "follow":
            buttons = driver.find_element_by_css_selector(CSS_SELECTOR['buttons'])
            print('Message or follow text found')

            request_sent = more_button(driver, request_sent, message)

        elif buttons[0].lower() == "pending":
            request_sent = True
        else:
            button_list = driver.find_element_by_css_selector(CSS_SELECTOR['buttons'])
            button_list.find_element_by_class_name('artdeco-button').click()
            random_wait(2, 5)
            request_sent = add_note(driver, request_sent, message)

        return request_sent
    except Exception as ex:
        # print("1", ex)
        return request_sent


def add_note(driver, request_sent, message):
    try:
        # add note
        print('add 546 note')

        add_note_button = driver.find_element_by_css_selector(CSS_SELECTOR['add_note_button']).click()
        # driver.find_element_by_class_name('artdeco-button__text').click()
        # print(len(add_note_button))
        # add_note_button.click()
        random_wait(3, 6)
        # note_area = driver.find_element_by_css_selector(CSS_SELECTOR['note_area'])

        note_area = driver.find_element_by_id('custom-message')
        print('note area found')
        random_wait(3, 8)
        # print(message)
        note_area.send_keys(message)
        random_wait(1, 4)

        # send button
        driver.find_element_by_css_selector(CSS_SELECTOR['send_button']).click()
        request_sent = True
        random_wait(2, 4)
        return request_sent
    except Exception as ex:
        print(ex)
        return request_sent


def inside_connect_button(driver, request_sent, message):
    try:
        driver.find_element_by_css_selector(CSS_SELECTOR['connect_inside_button']).click()
        random_wait(5, 10)
        request_sent = add_note(driver, request_sent, message)
        return request_sent

    except Exception as ex:
        print("3", ex)
        return request_sent


def more_button(driver, request_sent, message):
    # print("More button")
    try:
        # Click on more button
        # print([i.text for i in driver.find_elements_by_css_selector(CSS_SELECTOR['more_button'])])
        driver.find_elements_by_css_selector(CSS_SELECTOR['more_button'])[1].click()
        # print('clicked more button')
        wait(5)

        i = 1
        for item in driver.find_elements_by_css_selector(CSS_SELECTOR['more_button_dropdown']):
            if item.text == "Connect":
                item.click()
                print('Connect button clicked')
                random_wait(5, 10)


            elif item.text.lower() == "pending":
                request_sent = True
                return request_sent

            elif item.text.lower() == "remove connection":
                return True
            i += 1

        # request_sent = inside_connect_button(driver, request_sent, message)
        request_sent = add_note(driver, request_sent, message)
        return request_sent

    except Exception as ex:
        # print("2", ex)
        print(ex)
        return request_sent


def crm_li_outreach(linkedin_url_list, message, sheet):
    driver = chrome_driver()
    driver.get("https://linkedin.com")
    driver = add_cookies_in_driver(driver)
    driver.get("https://linkedin.com")
    time.sleep(5)
    try:
        count = 0
        for each_url in linkedin_url_list:
            # name = each_url['name']
            name = ''
            # linkedin = each_url['linkedin']
            linkedin = each_url
            if linkedin != '':
                if connect_request_sent(driver, message, linkedin):
                    count += 1
                    print(count, "Updated", name, linkedin)
                    updateStatus(linkedin, sheet, 1, 'Success')
                else:
                    print(count, "Unable to send", name, linkedin)
    except Exception as ex:
        print(ex)
    wait(5)
    driver.close()


def get_recent_accept_request_list(driver):
    driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
    time.sleep(5)
    connection_list = driver.find_element_by_class_name('scaffold-finite-scroll__content')
    details_card = connection_list.find_elements_by_class_name('mn-connection-card')
    person_list = []
    for each_person in details_card:
        name_div = each_person.find_element_by_class_name('mn-connection-card__name')
        name = name_div.text
        linkedin_div = each_person.find_element_by_class_name('mn-connection-card__picture')
        linkedin = linkedin_div.get_attribute('href')
        position_div = each_person.find_element_by_class_name('mn-connection-card__occupation')
        position = position_div.text
        accepted_time_div = each_person.find_element_by_class_name('time-badge')
        accepted_time = accepted_time_div.text
        temp_list = accepted_time.split(' ')
        # if 'seconds' in temp_list or 'hours' in temp_list or 'minutes' in temp_list:
        person_list.append(
            {'name': name, 'linkedin': linkedin, 'position': position, 'acceptance_time': accepted_time}
        )
    return person_list


def generate_accepted_request_report(sheet):
    driver = chrome_driver()
    driver.get("https://linkedin.com")
    driver = add_cookies_in_driver(driver)
    driver.get("https://linkedin.com")
    time.sleep(5)
    accepted_request = get_recent_accept_request_list(driver)
    print(accepted_request)
    for each_accepted in accepted_request:
        updateStatus(each_accepted['linkedin'], sheet, 2, 'Yes')
