# Copyright 2024. The Tari Project
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
# disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
