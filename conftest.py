import os

import allure
import pytest
import requests
from selene.support.shared import browser

userName = os.getenv('userName')
accessKey = os.getenv('accessKey')


def video_url_browserstack(*, session_id):
    session_details = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(userName, accessKey),
    ).json()

    return session_details['automation_session']['video_url']


def video_from_browserstack(session_id, *, name='video recording'):
    print(session_id)
    video_url = video_url_browserstack(session_id=session_id)

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name=name,
        attachment_type=allure.attachment_type.HTML,
    )


def abs_path_from_project(relative_path: str):
    import mobile_auto_browserstack
    from pathlib import Path

    return (
        Path(mobile_auto_browserstack.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )


# @pytest.fixture(scope='function', autouse=True)
# def driver_management(request):
#     yield
#     session_id = browser.driver.session_id
#     print(session_id)
#     video_from_browserstack(session_id)
