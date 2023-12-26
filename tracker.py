from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def scrape_data(driver):
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    locations = []  # array to store the locations
    worlds = []  # array to store the world numbers

    # Find all 'td' with class 'specialwidth' elements
    for td_special in soup.find_all('td', class_='specialwidth'):
        locations.append(td_special.text.strip())

    # Find all 'td' elements that contain an 'img' with class 'worldicon'
    for td in soup.find_all('td'):
        img = td.find('img', class_='worldicon')
        if img:
            # Extract the integer from the text of the 'td'
            int_value = int(td.text.strip())
            worlds.append(int_value)

    # Pair each location with its corresponding world number
    data = list(zip(worlds, locations))

    # Present data on console
    for item in data:
        print(item)

url = "https://osrsportal.com/shooting-stars-tracker"

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

try:
    while True:
        scrape_data(driver)
        # Wait for N seconds
        time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()