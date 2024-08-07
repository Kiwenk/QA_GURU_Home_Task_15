from selene import browser


class BaseActionsDesktop:
    def __init__(self):
        self.headermenu_signup = '.HeaderMenu-link--sign-up'

    def open_git(self):
        browser.open('')

    def desktop_actions(self):
        browser.element(self.headermenu_signup).click()


base_actions_desktop = BaseActionsDesktop()


class BaseActionsMobile:
    def __init__(self):
        self.headermenu_signup = '.HeaderMenu-link--sign-up'
        self.button_content = '.Button-content'

    def open_git(self):
        browser.open('')

    def mobile_actions(self):
        browser.element(self.button_content).click()
        browser.element(self.headermenu_signup).click()


base_actions_mobile = BaseActionsMobile()
