import pytest

from pages.base_action_page import base_actions_all


def test_mobile_skip(setup_browser):
    if setup_browser == "mobile":
        pytest.skip("Это мобильное разрешение")
    base_actions_all.open_git()
    base_actions_all.desktop_actions()


def test_desktop_skip(setup_browser):
    if setup_browser == "desktop":
        pytest.skip("Это десктопное разрешение")
    base_actions_all.open_git()
    base_actions_all.mobile_actions()
