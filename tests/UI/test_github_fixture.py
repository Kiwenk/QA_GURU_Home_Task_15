from pages.base_action_page import base_actions


def test_mobile_fixture(mobile_browser):
    base_actions.open_git()
    base_actions.mobile_actions()


def test_desktop_fixture(desktop_browser):
    base_actions.open_git()
    base_actions.desktop_actions()