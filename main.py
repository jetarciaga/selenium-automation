import random
import time
from pathlib import Path

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

CWD = Path(__file__).resolve().parent

geckodriver_path = CWD / ".utils" / "geckodriver.exe"
fake = Faker("en_PH")

class Person:
    def __init__(self, name):
        self.name = name
        self.firstname = name.split(" ")[0].lower()
        self.lastname = name.split(" ")[1].lower()

    def generate_email(self):
        print("generating random email")
        domain = random.choice(["gmail.com", "yahoo.com", "gmail.com.ph", "yahoo.com.ph", "plmun.edu.ph"])
        name = [self.firstname, self.lastname]
        random.shuffle(name)
        joining_str = random.choice(["", ".", "_"])

        return f"{name[0]}{joining_str}{name[1]}@{domain}"

def click_next(driver: webdriver.Firefox):
    print("clicking next")
    next = driver.find_element(By.XPATH, ".//span[text()='Susunod']/parent::span/parent::div")
    next.click()

def multiple_choice(driver: webdriver.Firefox, class_name: str):
    print("handling multiple choices")
    multiple_choices = driver.find_elements(By.XPATH, f".//div[@class='{class_name}']")

    for i in multiple_choices:
        choices = i.find_elements(By.XPATH, ".//div[@class='vd3tt']")
        element = random.choice(choices)
        element.click()

def check_box(driver: webdriver.Firefox, parent_class: str, child_class: str):
    print("handling checkboxes")
    learnPLMun = driver.find_elements(By.XPATH, f".//div[@class='{parent_class}']")[-1]
    elements = learnPLMun.find_elements(By.XPATH, f".//div[@class='{child_class}']")
    print(len(elements))
    random.shuffle(elements)
    for i in range(random.randrange(1, len(elements))):
        elements[i].click()

def click_submit(driver: webdriver.Firefox):
    print("clicking submit")
    submit = driver.find_element(By.XPATH, ".//span[text()='Submit']/parent::span/parent::div")
    submit.click()

def populate_form(driver: webdriver.Firefox):
    print("populating forms")
    robot = Person(name=fake.name())
    time.sleep(2)
    email_input = driver.find_element(By.XPATH, ".//input[@type='email']")
    email_input.send_keys(robot.generate_email())

    consent = driver.find_element(By.XPATH, ".//div[@id='i11']")
    consent.click()

    full_name = driver.find_element(By.XPATH ,".//div[@class='Xb9hP']/input[@type='text']")
    full_name.send_keys(robot.name)

    multiple_choice(driver, "oyXaNc")
    check_box(driver, "geS5n", "uVccjd aiSeRd FXLARc wGQFbe BJHAP oLlshd")
    click_next(driver)
    time.sleep(3)
    check_box(driver, "geS5n AFppSc", "uVccjd aiSeRd FXLARc wGQFbe BJHAP oLlshd")
    time.sleep(1)
    multiple_choice(driver, 'geS5n')
    click_next(driver)
    time.sleep(3)
    multiple_choice(driver, 'geS5n AFppSc')
    click_next(driver)
    time.sleep(3)
    multiple_choice(driver, 'geS5n AFppSc')
    multiple_choice(driver, 'geS5n')
    click_next(driver)
    time.sleep(2)
    click_submit(driver)



# a = Person()
# email = a.generate_email()
# print(email)

if __name__ == "__main__":
    for i in range(50):
        try:
            options = Options()
            # options.add_argument("--headless")
            browser = webdriver.Firefox(options=options)
            browser.get("https://forms.gle/cKf3t5umBnT3ZZvC8")
            populate_form(browser)
            browser.close()
        except Exception as e:
            print(e)
            print("Encountered error: looping back")