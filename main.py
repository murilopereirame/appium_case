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

    def test_create_subtask(self):
        new_task_button = self.driver.find_element(by=AppiumBy.ID, value="newTaskButton")

        new_task_button.click()

        time.sleep(2)

        new_task_input = self.driver.find_element(by=AppiumBy.ID, value="newTaskDialogInputTitle")
        new_task_input.send_keys("Sample Text")

        new_task_create = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="CREATE"]')
        new_task_create.click()

        time.sleep(2)

        assert self.driver.current_activity == ".ui.activity.ActivitySubtaskList"

        self.openNewSubtaskDialog()

        new_sub_task_dialog_title = self.driver.find_element(by=AppiumBy.ID, value="alertTitle")

        assert new_sub_task_dialog_title is not None
        assert new_sub_task_dialog_title.text == "Create New Sub-Task"

        new_sub_task_input = self.driver.find_element(by=AppiumBy.ID, value="newSubTaskDialogInputTitle")

        assert new_sub_task_input is not None

        new_sub_task_input.send_keys("Sample SubTask")

        new_sub_task_create = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="CREATE"]')

        assert new_sub_task_create is not None

        new_sub_task_create.click()

        time.sleep(2)

        sub_task = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Sample SubTask"]')

        assert sub_task.text == "Sample SubTask"
        assert sub_task.get_attribute("checked") == "false"

        assert self.driver.current_activity == ".ui.activity.ActivitySubtaskList"

        self.openNewSubtaskDialog()

        new_sub_task_input = self.driver.find_element(by=AppiumBy.ID, value="newSubTaskDialogInputTitle")
        new_sub_task_input.send_keys("Sample SubTask Checked")

        new_sub_task_done = self.driver.find_element(AppiumBy.ID, value="newSubTaskDialogDone")
        new_sub_task_done.click()

        time.sleep(2)

        new_sub_task_create = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="CREATE"]')
        new_sub_task_create.click()

        time.sleep(2)

        sub_task = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Sample SubTask Checked"]')

        assert sub_task.text == "Sample SubTask Checked"
        assert sub_task.get_attribute("checked") == "true"

    def openNewSubtaskDialog(self):
        new_subtask_button = self.driver.find_element(by=AppiumBy.ID, value="subtaskListAddButton")
        assert new_subtask_button is not None
        new_subtask_button.click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
