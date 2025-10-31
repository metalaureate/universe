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
Visual verification tests for Tari Universe
These tests capture and verify visual elements of the application
"""

import pytest
# import time


@pytest.mark.ui
class TestVisualVerification:
    """Tests for visual verification of UI elements"""

    def test_capture_full_window(self, app_controller, screenshot_helper):
        """Capture full application window for visual verification"""
        window_region = app_controller.get_window_region()
        if window_region:
            screenshot_helper.capture("full_window_capture", region=window_region)

    def test_capture_mining_view(self, app_controller, screenshot_helper, ui_helper):
        """Capture the mining view for visual verification"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            ui_helper.click(x + 100, y + 150)
            ui_helper.wait(2)

            mining_view_region = (x + 250, y + 50, width - 250, height - 150)
            screenshot_helper.capture("mining_view", region=mining_view_region)

    def test_capture_sidebar_sections(self, app_controller, screenshot_helper):
        """Capture different sections of the sidebar"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            sidebar_region = (x, y, 250, height)
            screenshot_helper.capture("sidebar_full", region=sidebar_region)

            top_section = (x, y, 250, 200)
            screenshot_helper.capture("sidebar_top_section", region=top_section)

            middle_section = (x, y + 200, 250, 200)
            screenshot_helper.capture("sidebar_middle_section", region=middle_section)

            bottom_section = (x, y + height - 200, 250, 200)
            screenshot_helper.capture("sidebar_bottom_section", region=bottom_section)

    def test_capture_earnings_area(self, app_controller, screenshot_helper):
        """Capture the earnings display area"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            earnings_region = (x + 300, y + 50, width - 350, 250)
            screenshot_helper.capture("earnings_area", region=earnings_region)

    def test_capture_mining_controls(self, app_controller, screenshot_helper):
        """Capture the mining control buttons"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            controls_region = (x + 250, y + height - 150, width - 250, 150)
            screenshot_helper.capture("mining_controls", region=controls_region)

    @pytest.mark.slow
    def test_capture_animation_sequence(self, app_controller, screenshot_helper, ui_helper):
        """Capture a sequence of screenshots to verify animations"""
        window_region = app_controller.get_window_region()
        if window_region:
            for i in range(5):
                screenshot_helper.capture(f"animation_frame_{i:02d}", region=window_region)
                ui_helper.wait(1)

    def test_verify_visual_mode_toggle(self, app_controller, screenshot_helper, ui_helper):
        """Test visual mode toggle if accessible"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            screenshot_helper.capture("visual_mode_before", region=window_region)

            settings_x = x + width - 50
            settings_y = y + 50
            ui_helper.click(settings_x, settings_y)
            ui_helper.wait(2)

            screenshot_helper.capture("visual_mode_after", region=window_region)
