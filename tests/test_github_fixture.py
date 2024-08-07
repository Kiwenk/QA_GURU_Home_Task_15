from pages.base_action_page import base_actions_desktop, base_actions_mobile


def test_mobile_fixture(mobile_browser):
    base_actions_mobile.open_git()
    base_actions_mobile.mobile_actions()


def test_desktop_fixture(desktop_browser):
    base_actions_desktop.open_git()
    base_actions_desktop.desktop_actions()
