import pydantic
from appium.options.android import UiAutomator2Options
from typing import Optional, Literal
from conftest import abs_path_from_project

EnvContext = Literal['local', 'browserstack']

class Settings(pydantic.BaseSettings):
    context: EnvContext = 'local'

    platformName: str = None
    platformVersion: str = None
    deviceName: str = None
    app: Optional[str] = None
    appName: Optional[str] = None
    appWaitActivity: Optional[str]  = None
    newCommandTimeout: Optional[int] = 60000

    projectName: Optional[str] = None
    buildName: Optional[str] = None
    sessionName: Optional[str] = None
    user_name: Optional[str] = None
    access_key: Optional[str] = None
    udid: Optional[str] = None

    remote_url: str = 'http://127.0.0.1:4723/wd/hub'
    timeout: float = 16.0

    @property
    def run_on_browserstack(self):
        return 'hub.browserstack.com' in self.remote_url

    @property
    def driver_options(self):
        options = UiAutomator2Options()
        if self.deviceName:
            options.deviceName = self.deviceName
        if self.platformName:
            options.platformName = self.platformName
        if self.app:
            options.app = self.app
        if self.udid:
            options.udid = self.udid
        if self.appWaitActivity:
            options.app_wait_activity = self.appWaitActivity
        if self.appName:
            options.appName = self.appName
        if self.newCommandTimeout:
            options.newCommandTimeout = self.newCommandTimeout
        if self.remote_url:
            options.load_capabilities({
                'platformVersion': self.platformVersion,
                'bstack:options': {
                    'projectName': self.projectName,
                    'buildName': self.buildName,
                    'sessionName': self.sessionName,
                    'userName': self.user_name,
                    'accessKey': self.access_key
                }
            }
            )
        return options




    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None) -> 'Settings':
        """
        factory method to init Settings with values from corresponding .env file
        """
        asked_or_current = env or cls().context
        return  cls(
            _env_file=abs_path_from_project(f'config.{asked_or_current}.env')
        )

settings = Settings.in_context()

def test():
    print(settings)
#
#
# def test_in_context(cls, env: Optional[EnvContext] = 'local'):
#
#     asked_or_current = env or cls().context
#     print(abs_path_from_project(f'config.{asked_or_current}.env'))
