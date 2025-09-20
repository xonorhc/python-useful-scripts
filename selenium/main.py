import shutil
import tempfile
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

user_data_dir = tempfile.mkdtemp()


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    browser = webdriver.Chrome(
        options=chrome_options,
    )

    return browser


if __name__ == "__main__":
    TIME_TO_WAIT = 10
    try:
        options = (
            "--disable-extensions",
            "--disable-gpu",
            f"--user-data-dir={user_data_dir}",
        )

        browser = make_chrome_browser(*options)
        browser.get("https://duckduckgo.com/")

        search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_input.send_keys("Hello World!")
        search_input.send_keys(Keys.ENTER)

        results = browser.find_element(By.ID, "r1-0")
        links = results.find_elements(By.TAG_NAME, "a")

        for i, e in enumerate(links):
            print(i, e.text)

        links[4].click()

        sleep(TIME_TO_WAIT)

    finally:
        if "browser" in locals() and browser:
            browser.quit()

        # Clean up the temporary directory
        shutil.rmtree(user_data_dir)
