import pytest
from pages.base_action_page import base_actions_desktop, base_actions_mobile

desktop_only = pytest.mark.parametrize("setup_browser",
                                       [(2560, 1440), (1920, 1080)],
                                       indirect=True,
                                       ids=['1440p', '1080p'])
mobile_only = pytest.mark.parametrize("setup_browser",
                                      [(414, 896)],
                                      indirect=True,
                                      ids=['IPhone XR'])


@mobile_only
def test_mobile_indirect(setup_browser):
    base_actions_mobile.open_git()
    base_actions_mobile.mobile_actions()


@desktop_only
def test_desktop_indirect(setup_browser):
    base_actions_desktop.open_git()
    base_actions_desktop.desktop_actions()
