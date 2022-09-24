from appium.webdriver.common.appiumby import AppiumBy


def accessibility_id(text):
    return (AppiumBy.ACCESSIBILITY_ID, text)

def class_name(name):
    return (AppiumBy.CLASS_NAME, name)

def id(name):
    return (AppiumBy.ID, name)