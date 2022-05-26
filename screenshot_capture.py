from selenium import webdriver
import os
from slate import Slate


def grab_screenshot(driver: webdriver.Chrome, url: str, screenshot_name: str = None) -> bool:
    driver.get(url)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
    return driver.find_element_by_tag_name('body').screenshot(screenshot_name)


def get_chrome_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.headless = True

    return webdriver.Chrome('./chromedriver', options=options)


def pngify(filename):
    if not filename[-3:] == '.png':
        return filename + '.png'
    return filename


def get_multiple_screenshots(urls: dict) -> None:
    for url in urls:
        tag, filename = urls[url]
        os.makedirs(os.path.join(".", "screenshots", tag), exist_ok=True)
        grab_screenshot(get_chrome_driver(), url, os.path.join(".", "screenshots", tag, pngify(filename)))


def upload_all_files(tag: str) -> None:
    files = [os.path.join(".", "screenshots", tag, file) for file in os.listdir(os.path.join(".", "screenshots", tag))]
    slate = Slate()
    slate.upload_files(files)


if __name__ == '__main__':
    tag = 'aws'
    urls_to_process = {
        'https://aws.amazon.com/s3': (tag, 'landing_page'),
        'https://aws.amazon.com/s3/features': (tag, 'features'),
        'https://aws.amazon.com/s3/storage-classes': (tag, 'storage-classes'),
        'https://aws.amazon.com/s3/pricing': (tag, 'pricing'),
        'https://aws.amazon.com/s3/security': (tag, 'security'),
        'https://aws.amazon.com/s3/resources': (tag, 'resources'),
        'https://aws.amazon.com/s3/faqs': (tag, 'faqs'),
    }
    get_multiple_screenshots(urls_to_process)
    upload_all_files(tag)
