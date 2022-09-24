from allure_commons._allure import step
from appium import webdriver
from selene import have, be
from selene.support.shared import browser
from mobile_auto_browserstack import appium_by
from mobile_auto_browserstack.app import screen_language_and_skip_btn
import config
import time

def test_linkin_park():
    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )
    screen_language_and_skip_btn()
    with step('Search'):
        browser.element(appium_by.id('org.wikipedia.alpha:id/search_container')).click()
        browser.element(appium_by.id('org.wikipedia.alpha:id/search_src_text')).type('Linkin Park')
    with step('Opening in search list'):
        browser.all(appium_by.id('org.wikipedia.alpha:id/page_list_item_title'))[0].click()
        browser.element(appium_by.id('org.wikipedia.alpha:id/view_page_header_image')).should(be.visible)
        time.sleep(1)
    with step('Assert open image'):
        browser.element(appium_by.id('org.wikipedia.alpha:id/view_page_header_image')).click()
    with step('Assert close image'):
        browser.element(appium_by.class_name('android.widget.ImageButton')).should(be.visible)
        browser.element(appium_by.class_name('android.widget.ImageButton')).click()
    with step('Assert close post name'):
        browser.all(appium_by.class_name('android.view.View'))[0].element(appium_by.class_name('android.view.View')).should(have.text('Linkin Park'))
    with step('Assert contents open'):
        browser.element(appium_by.id('org.wikipedia.alpha:id/page_contents')).click()
    with step('Assert contents name'):
        browser.element(appium_by.id('org.wikipedia.alpha:id/toc_list')).should(be.visible)
        browser.all(appium_by.id('org.wikipedia.alpha:id/page_toc_item_text'))[0].should(have.text('Linkin Park'))

#run "env -S "context=local" pytest tests"