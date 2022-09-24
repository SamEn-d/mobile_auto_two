from allure_commons._allure import step
from selene import be
from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy

def screen_language_and_skip_btn():
    if browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).matching(be.visible):
        with step('Click skip button'):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()