from selene import browser


class BaseActions:
    def __init__(self):
        self.headermenu_signup = '.HeaderMenu-link--sign-up'
        self.button_content = '.Button-content'

    def open_git(self):
        browser.open('')


class BaseActionsMobAndDesk(BaseActions):

    def desktop_actions(self):
        browser.element(self.headermenu_signup).click()

    def mobile_actions(self):
        browser.element(self.button_content).click()
        browser.element(self.headermenu_signup).click()


base_actions_all = BaseActionsMobAndDesk()
