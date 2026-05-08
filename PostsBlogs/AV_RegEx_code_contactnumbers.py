import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from retry import retry
from selenium.common.exceptions import StaleElementReferenceException

import urllib2

BSNL_Maharashtra = "http://dq.wdc.bsnl.co.in/bsnl-web/residentialSearch.seam"
Google_Search = "https://www.google.co.in"
LinkedIn_Search = "https://www.linkedin.com/"

@retry(StaleElementReferenceException, tries=3)
def find_element(driver, id, clear=True):
    try:
        print (id)
        elem = driver.find_element_by_id(id)
        print('Found <%s> element with that class name!' % (elem.tag_name))
    except:
        print('Was not able to find an element with that name.')

    if clear:
        elem.clear()
    elem.click()
    return elem

def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 10) #  to wait for UI elements to appear
    return driver

def BSNL_MH_lookup(driver, lastname, city):
    driver.get(BSNL_Maharashtra)
    print ("Browser window invoked.")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID,"residential:button1")))
    print ("Looking at {} for {} and {}".format(BSNL_Maharashtra,lastname,city))

    box_lastname = find_element(driver, "residential:firstField")
    box_city = find_element(driver, "residential:city")
    button = driver.find_element_by_id("residential:button1")
    box_lastname.send_keys(lastname)
    box_city.send_keys(city)
    button.click()

def google_scrape(query):
    address = "http://www.google.com/search?q=%s&num=100&hl=en&start=0" % (urllib.quote_plus(query))
    request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    urlfile = urllib2.urlopen(request)
    page = urlfile.read()
    soup = BeautifulSoup(page)

    linkdictionary = {}

    for li in soup.findAll('li', attrs={'class':'g'}):
        sLink = li.find('a')
        sSpan = li.find('span', attrs={'class':'st'})

        linkeDictionary['href'] = sLink['href']
        linkedDictionary['sSpan'] = sSpan

    return linkdictionary

def Google_lookup(driver, query):
    driver.get(Google_Search)
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

if __name__ == "__main__":
    driver = init_driver()
    firstname = 'Anup'
    lastname = "Sable"
    city = "Pune"
    company = "KPIT"
    # person_details = firstname + " " + lastname + " " +  city + " " + company
    # LinkedIn_query = person_details + " site:linkedin.com"
    # Google_lookup(driver, LinkedIn_query)
    BSNL_MH_lookup(driver,lastname,city)
    time.sleep(5)
    driver.quit()
