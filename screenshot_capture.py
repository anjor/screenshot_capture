from selenium import webdriver


def grab_screenshot(driver: webdriver.Chrome, url: str, screenshot_name: str = None) -> bool:
    driver.get(url)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
    return driver.find_element_by_tag_name('body').screenshot(screenshot_name)


def get_chrome_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.headless = True

    return webdriver.Chrome('./chromedriver', options=options)


if __name__ == '__main__':
    URL = 'https://aws.amazon.com/s3/features'
    grab_screenshot(get_chrome_driver(), URL, "test5.png")
