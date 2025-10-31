"""
Tests for keyboard shortcuts and keyboard interactions
"""

import pytest
# import time


@pytest.mark.ui
class TestKeyboardShortcuts:
    """Tests for keyboard shortcuts and interactions"""

    def test_tab_navigation(self, ui_helper, app_controller, screenshot_helper):
        """Test navigation using Tab key"""
        window_region = app_controller.get_window_region()
        if window_region:
            app_controller.focus_window()

            screenshot_helper.capture("tab_nav_initial", region=window_region)

            for i in range(5):
                ui_helper.press_key('tab')
                ui_helper.wait(0.5)
                screenshot_helper.capture(f"tab_nav_{i+1}", region=window_region)

    def test_escape_key(self, ui_helper, app_controller, screenshot_helper):
        """Test Escape key functionality"""
        window_region = app_controller.get_window_region()
        if window_region:
            screenshot_helper.capture("before_escape", region=window_region)

            ui_helper.press_key('esc')
            ui_helper.wait(1)

            screenshot_helper.capture("after_escape", region=window_region)

    def test_enter_key(self, ui_helper, app_controller, screenshot_helper):
        """Test Enter key functionality"""
        window_region = app_controller.get_window_region()
        if window_region:
            app_controller.focus_window()

            screenshot_helper.capture("before_enter", region=window_region)

            ui_helper.press_key('enter')
            ui_helper.wait(1)

            screenshot_helper.capture("after_enter", region=window_region)

    def test_arrow_key_navigation(self, ui_helper, app_controller, screenshot_helper):
        """Test arrow key navigation"""
        window_region = app_controller.get_window_region()
        if window_region:
            app_controller.focus_window()

            arrow_keys = ['up', 'down', 'left', 'right']

            for key in arrow_keys:
                screenshot_helper.capture(f"before_arrow_{key}", region=window_region)
                ui_helper.press_key(key)
                ui_helper.wait(1)
                screenshot_helper.capture(f"after_arrow_{key}", region=window_region)

    def test_space_key(self, ui_helper, app_controller, screenshot_helper):
        """Test Space key functionality"""
        window_region = app_controller.get_window_region()
        if window_region:
            app_controller.focus_window()

            screenshot_helper.capture("before_space", region=window_region)

            ui_helper.press_key('space')
            ui_helper.wait(1)

            screenshot_helper.capture("after_space", region=window_region)
