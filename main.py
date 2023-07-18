import time
import unittest

import appium.webdriver.common.mobileby
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='br.dev.murilopereira.todo',
    appActivity='.ui.activity.MainActivity'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_create_task(self) -> None:
        new_task_button = self.driver.find_element(by=AppiumBy.ID, value="newTaskButton")

        assert new_task_button is not None

        new_task_button.click()

        time.sleep(2)

        new_task_dialog_title = self.driver.find_element(by=AppiumBy.ID, value="alertTitle")

        assert new_task_dialog_title is not None
        assert new_task_dialog_title.text == "Create New Task"

        new_task_input = self.driver.find_element(by=AppiumBy.ID, value="newTaskDialogInputTitle")

        assert new_task_input is not None

        new_task_input.send_keys("Sample Text")

        new_task_create = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="CREATE"]')

        assert new_task_create is not None

        new_task_create.click()

        time.sleep(2)

        assert self.driver.current_activity == ".ui.activity.ActivitySubtaskList"

        self.driver.back()

        time.sleep(2)

        assert self.driver.current_activity == '.ui.activity.MainActivity'

        task_title = self.driver.find_element(by=AppiumBy.ID, value='taskListTitle')

        assert task_title.text == "Sample Text"


if __name__ == '__main__':
    unittest.main()
