from selenium import webdriver


def grab_screenshot(driver, url, screenshot_name=None):
    driver.get(url)
    return driver.save_screenshot(screenshot_name or url + ".png")


if __name__ == '__main__':
    DRIVER = './chromedriver'
    URL = 'https://aws.amazon.com/s3/features'
    chrome_driver = webdriver.Chrome(DRIVER)
    grab_screenshot(chrome_driver, URL, "test2.png")
    chrome_driver.quit()
