"""
Smoke tests for Tari Universe application
These tests verify basic functionality and app startup
"""

import pytest
# import time


@pytest.mark.smoke
class TestSmoke:
    """Smoke tests for basic application functionality"""

    def test_app_launches(self, app_controller):
        """Test that the application launches successfully"""
        assert app_controller.is_running(), "Application should be running"

    def test_app_window_visible(self, app_controller, screenshot_helper):
        """Test that the application window is visible"""
        window_region = app_controller.get_window_region()
        assert window_region is not None, "Application window should be visible"

        screenshot_helper.capture("app_main_window", region=window_region)

    def test_app_responsive(self, app_controller, ui_helper):
        """Test that the application is responsive to mouse movements"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region
            ui_helper.move_to(x + width // 2, y + height // 2)

            pos = ui_helper.get_mouse_position()
            assert pos is not None, "Mouse should be movable"

    def test_screen_capture_works(self, screenshot_helper):
        """Test that screenshot capture functionality works"""
        screenshot_path = screenshot_helper.capture("smoke_test_capture")
        assert screenshot_path.exists(), "Screenshot should be saved"
