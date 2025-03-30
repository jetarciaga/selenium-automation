import random
import time
from pathlib import Path
from typing import List

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from main import Person

fake = Faker("en_PH")

def organize_form(driver: webdriver.Firefox):
    forms = driver.find_elements(By.CLASS_NAME, "geS5n")
    short_answer = forms[0:5]
    radio_answer = forms[5:15]
    comment_answer = forms[15:]

    return short_answer, radio_answer, comment_answer

def short_answers(element: WebElement, answer: str):
    selection = element.find_element(By.TAG_NAME, "input")
    selection.send_keys(answer)

def radio_answers(elements: List[WebElement]):
    print("Randomizing selection.")
    for element in elements:
        radios = element.find_elements(By.XPATH, ".//div[@class='AB7Lab Id5V1']")
        random.choice(radios).click()

def comment_answers(element: WebElement, answer: str):
    selection = element.find_element(By.TAG_NAME, "textarea")
    selection.send_keys(answer)


def populate_form(driver: webdriver.Firefox):
    bot_name = fake.name()
    print(f"populating forms as {bot_name}.")
    robot = Person(name=bot_name)
    time.sleep(1)

    short, radio, comment = organize_form(driver)

    short_answers(short[0], robot.name)
    short_answers(short[1], random.randrange(30, 59))
    short_answers(short[2], random.randrange(5, 10))
    selections = [
        "Admin aide III",
        "Admin aide IV",
        "Master Teacher I",
        "Teacher I",
        "Teacher II",
        "Head Teacher I"
    ]
    short_answers(short[3], random.choice(selections))
    departments = [
        "Lakeview Integrated School",
        "Schools Division Office",
        "Itaas Elementary School",
        "F. De Mesa Elementary School",
        "Pedro E. Diaz"
    ]
    short_answers(short[4], random.choice(departments))

    radio_answers(radio)

    comment_answers(comment[0], random.choice(["Yes", "No"]))
    comment_answers(comment[1], "No comment!")

    driver.find_element(By.XPATH, ".//span[text()='Submit']").click()


if __name__ == "__main__":
    for i in range(30):
        print(f"Run: {i+1}")
        options = Options()
        options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)
        browser.get("https://forms.gle/VVwi24yWFHmbkSsAA")
        time.sleep(1)
        populate_form(browser)
        browser.close()