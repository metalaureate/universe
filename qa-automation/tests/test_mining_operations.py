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
End-to-end tests for mining operations in Tari Universe
These tests interact with the mining controls and verify mining functionality
"""

import pytest
# import time


@pytest.mark.mining
@pytest.mark.ui
class TestMiningOperations:
    """Tests for mining start/stop/pause operations"""

    def test_locate_mining_button(self, ui_helper, app_controller, screenshot_helper):
        """Test that we can locate the mining button area"""
        window_region = app_controller.get_window_region()
        assert window_region is not None, "Window should be visible"

        screenshot_helper.capture("mining_interface", region=window_region)

        x, y, width, height = window_region
        mining_button_area = (x, y + height - 200, width, 200)
        screenshot_helper.capture("mining_button_area", region=mining_button_area)

    def test_click_mining_control_area(self, ui_helper, app_controller, screenshot_helper):
        """Test clicking in the mining control area"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            mining_button_x = x + width // 2
            mining_button_y = y + height - 100

            screenshot_helper.capture("before_mining_click", region=window_region)

            ui_helper.click(mining_button_x, mining_button_y)
            ui_helper.wait(2)

            screenshot_helper.capture("after_mining_click", region=window_region)

    def test_mining_mode_interaction(self, ui_helper, app_controller, screenshot_helper):
        """Test interaction with mining mode controls"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            sidebar_x = x + 100
            sidebar_y = y + 200

            sidebar_region = (x, y, 300, height)
            screenshot_helper.capture("sidebar_area", region=sidebar_region)

            ui_helper.click(sidebar_x, sidebar_y)
            ui_helper.wait(1)
            screenshot_helper.capture("after_cpu_tile_click", region=window_region)

    @pytest.mark.slow
    def test_mining_state_changes(self, ui_helper, app_controller, screenshot_helper):
        """Test mining state changes over time"""
        window_region = app_controller.get_window_region()
        if window_region:
            for i in range(3):
                screenshot_helper.capture(f"mining_state_{i}", region=window_region)
                ui_helper.wait(5)

    def test_earnings_display_visible(self, ui_helper, app_controller, screenshot_helper):
        """Test that earnings display is visible"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            earnings_region = (x + 300, y + 100, width - 300, 300)
            screenshot_helper.capture("earnings_display", region=earnings_region)

    def test_mining_tiles_interaction(self, ui_helper, app_controller, screenshot_helper):
        """Test interaction with CPU and GPU mining tiles"""
        window_region = app_controller.get_window_region()
        if window_region:
            x, y, width, height = window_region

            cpu_tile_x = x + 100
            cpu_tile_y = y + 150

            gpu_tile_x = x + 100
            gpu_tile_y = y + 250

            screenshot_helper.capture("before_cpu_tile", region=window_region)
            ui_helper.click(cpu_tile_x, cpu_tile_y)
            ui_helper.wait(1)
            screenshot_helper.capture("after_cpu_tile", region=window_region)

            ui_helper.click(gpu_tile_x, gpu_tile_y)
            ui_helper.wait(1)
            screenshot_helper.capture("after_gpu_tile", region=window_region)
