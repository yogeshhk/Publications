import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from retry import retry
from selenium.common.exceptions import StaleElementReferenceException

def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 10) #  to wait for UI elements to appear
    return driver

def Google_lookup(driver, query):
    driver.get("https://www.google.co.in")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "q"))) # Get handle to the SEARCH box
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "btnK"))) # Get handle to the SERACH button
        box.send_keys(query)
        try:
            button.click()
        except ElementNotVisibleException:
            button = driver.wait.until(EC.visibility_of_element_located(
                (By.NAME, "btnG")))
            button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")

    # the page is ajaxy so the title is originally this:
    print(driver.title)
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains(query))
    print("Got results at " + driver.title)
    result = driver.find_elements_by_xpath("//ol[@id='rso']/li")[0] #make a list of results and get the first one
    result.find_element_by_xpath("./div/h3/a").click() #click its href
    print(result)

if __name__ == "__main__":
    driver = init_driver()
    firstname = 'Yogesh'
    lastname = "Kulkarni"
    city = "Pune"
    company = "COEP"
    person_details = firstname + " " + lastname + " " +  city + " " + company
    #LinkedIn_query = person_details + " site:linkedin.com"
    LinkedIn_query = person_details + " site:linkedin.com/in/ OR site:linkedin.com/pub/ -intitle:profiles -inurl:'/dir'"
    Google_lookup(driver, LinkedIn_query)
    time.sleep(5)
    driver.quit()
