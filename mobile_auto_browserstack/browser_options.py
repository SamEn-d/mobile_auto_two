import os

from appium.options.android import UiAutomator2Options

userName = os.getenv('userNameBS')
accessKey = os.getenv('accessKey')

def test_sad():
    print(userName)
    print(accessKey)

def browser_options():
    browser_options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName" : "android",
        "platformVersion" : "9.0",
        "deviceName" : "Google Pixel 3",

        # Set URL of the application under test
        "app" : "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",

        # Set other BrowserStack capabilities
        'bstack:options' : {
            "projectName" : "First Python project",
            "buildName" : "browserstack-build-1",
            "sessionName" : "BStack first_test",

            # Set your access credentials
            "userName" : userName,
            "accessKey" : accessKey
        }
    })
    return browser_options

def browser_options_loc():
    browser_options = UiAutomator2Options().load_capabilities({
    "autoGrantPermissions" :True,
    "app": "C:\mobile_auto_browserstack-master/app-alpha-universal-release.apk",
    "appName" : "org.wikipedia.alpha",
    "appWaitActivity" : "org.wikipedia.*",
    "newCommandTimeout": 60000,
    "appWaitDuration": 60000
    }
    )
    return browser_options