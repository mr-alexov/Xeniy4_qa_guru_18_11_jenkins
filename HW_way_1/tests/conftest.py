import os
import logging
from selene import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from HW_way_1.Utils import attach

logger = logging.getLogger(__name__)

load_dotenv()
selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")

@pytest.fixture
def selenoid():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.window_height = 1080  # задает высоту окна браузера
    browser.config.window_width = 1920

    browser.config.driver = driver

    yield
    browser.quit()


@pytest.fixture()
def selenoid2():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }



    selenoid_full_url = f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub"
    selenoid_full_url = f"https://user1:1234@selenoid.autotests.cloud/wd/hub"

    logger.info(f"Selenoid url: {selenoid_full_url}")
    print()
    print(f"Selenoid url: {selenoid_full_url}")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=selenoid_full_url,
        options=options)

    browser.config.window_height = 1080  # задает высоту окна браузера
    browser.config.window_width = 1920

    browser.config.driver = driver

    yield

    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    attach.add_screenshot(browser)


@pytest.fixture(scope='session')
def browser_manager():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
