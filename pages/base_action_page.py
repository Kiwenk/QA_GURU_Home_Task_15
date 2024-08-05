from selene import browser


class BaseActionsTest:
    def open_git(self):
        browser.open('')

    def mobile_actions(self):
        browser.element('.Button-content').click()
        browser.element('.HeaderMenu-link--sign-up').click()

    def desktop_actions(self):
        browser.element('.HeaderMenu-link--sign-up').click()


base_actions = BaseActionsTest()
