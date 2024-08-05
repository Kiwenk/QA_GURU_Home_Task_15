import pytest
from pages.base_action_page import base_actions

desktop_only = pytest.mark.parametrize("desktop_browser",
                                       [(2560, 1440), (1920, 1080)],
                                       indirect=True,
                                       ids=['1440p', '1080p'])
mobile_only = pytest.mark.parametrize("mobile_browser",
                                      [(414, 896)],
                                      indirect=True,
                                      ids=['IPhone XR'])


@mobile_only
def test_mobile_indirect(mobile_browser):
    base_actions.open_git()
    base_actions.mobile_actions()

@desktop_only
def test_desktop_indirect(desktop_browser):
    base_actions.open_git()
    base_actions.desktop_actions()



