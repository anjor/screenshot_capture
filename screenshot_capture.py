from selenium import webdriver


DRIVER = 'chromedriver'
URL = 'https://aws.amazon.com/s3'
driver = webdriver.Chrome(DRIVER)
driver.get(URL)
screenshot = driver.save_screenshot('my_screenshot.png')
driver.quit()
