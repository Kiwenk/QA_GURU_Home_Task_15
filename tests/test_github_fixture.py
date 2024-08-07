from pages.base_action_page import base_actions_all


def test_mobile_fixture(mobile_browser):
    base_actions_all.open_git()
    base_actions_all.mobile_actions()


def test_desktop_fixture(desktop_browser):
    base_actions_all.open_git()
    base_actions_all.desktop_actions()
