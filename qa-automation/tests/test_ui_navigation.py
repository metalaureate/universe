"""
End-to-end tests for UI navigation in Tari Universe
These tests verify navigation between different sections of the app
"""

import pytest
# import time


@pytest.mark.ui
class TestUINavigation:
    """Tests for navigating through the application UI"""

    def test_sidebar_navigation(self, ui_helper, app_controller, screenshot_helper):
        """Test navigation through sidebar menu items"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            sidebar_x = x + 50

            screenshot_helper.capture("sidebar_initial", region=window_region)

            ui_helper.click(sidebar_x, y + 100)
            ui_helper.wait(1)
            screenshot_helper.capture("sidebar_nav_1", region=window_region)

            ui_helper.click(sidebar_x, y + 300)
            ui_helper.wait(1)
            screenshot_helper.capture("sidebar_nav_2", region=window_region)

            ui_helper.click(sidebar_x, y + 500)
            ui_helper.wait(1)
            screenshot_helper.capture("sidebar_nav_3", region=window_region)

    def test_main_dashboard_area(self, ui_helper, app_controller, screenshot_helper):
        """Test interaction with main dashboard area"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            dashboard_x = x + width // 2
            dashboard_y = y + height // 2

            dashboard_region = (x + 250, y, width - 250, height)
            screenshot_helper.capture("main_dashboard", region=dashboard_region)

            ui_helper.click(dashboard_x, dashboard_y)
            ui_helper.wait(1)

    def test_settings_access(self, ui_helper, app_controller, screenshot_helper):
        """Test accessing settings or configuration"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            settings_x = x + width - 50
            settings_y = y + 50

            screenshot_helper.capture("before_settings", region=window_region)
            ui_helper.click(settings_x, settings_y)
            ui_helper.wait(1)
            screenshot_helper.capture("after_settings_click", region=window_region)

    def test_window_scrolling(self, ui_helper, app_controller, screenshot_helper):
        """Test scrolling within the application window"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            center_x = x + width // 2
            center_y = y + height // 2
            ui_helper.move_to(center_x, center_y)

            screenshot_helper.capture("before_scroll", region=window_region)

            ui_helper.scroll(-3, center_x, center_y)
            ui_helper.wait(1)
            screenshot_helper.capture("after_scroll_down", region=window_region)

            ui_helper.scroll(3, center_x, center_y)
            ui_helper.wait(1)
            screenshot_helper.capture("after_scroll_up", region=window_region)

    def test_hover_interactions(self, ui_helper, app_controller, screenshot_helper):
        """Test hover interactions with UI elements"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            hover_points = [
                (x + 100, y + 150, "hover_sidebar_top"),
                (x + 100, y + 300, "hover_sidebar_middle"),
                (x + width // 2, y + 100, "hover_dashboard_top"),
                (x + width - 100, y + 100, "hover_top_right"),
            ]

            for hover_x, hover_y, name in hover_points:
                ui_helper.move_to(hover_x, hover_y, duration=0.5)
                ui_helper.wait(1)
                screenshot_helper.capture(name, region=window_region)
