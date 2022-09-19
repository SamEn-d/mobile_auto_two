from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from mobile_auto_browserstack.browser_options import browser_options, browser_options_loc

from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from tests.config import video_from_browserstack



def test_wiki_in_documentation():
    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=browser_options())
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('BrowserStack')
    browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))
    session_id = browser.driver.session_id
    video_from_browserstack(session_id)

def test_wiki_post_open():
    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=browser_options())
    # browser.config.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=browser_options_loc())
    time.sleep(1)
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Selene')
    browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).with_(timeout=10).should(be.visible)
    time.sleep(9)
    browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView"))[1].click()
    time.sleep(9)
    # session_id = browser.driver.session_id
    # video_from_browserstack(session_id)
