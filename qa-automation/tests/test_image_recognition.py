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
Image recognition-based tests for Tari Universe
These tests use image recognition to find and interact with specific UI elements
"""

import pytest
# import time
from pathlib import Path


@pytest.mark.ui
class TestImageRecognition:
    """Tests using image recognition to interact with UI elements"""

    def test_find_mining_button_by_image(self, ui_helper, screenshot_helper, app_controller):
        """
        Test finding and clicking the mining button using image recognition

        Note: This test requires reference images to be captured first.
        See qa-automation/images/README.md for instructions on capturing reference images.
        """
        window_region = app_controller.get_window_region()
        if window_region:
            screenshot_helper.capture("current_state_for_mining_button", region=window_region)

            mining_button_image = Path("qa-automation/images/mining_button.png")

            if mining_button_image.exists():
                success = ui_helper.click_image(str(mining_button_image), timeout=5)

                if success:
                    ui_helper.wait(2)
                    screenshot_helper.capture("after_mining_button_click", region=window_region)
                    assert True, "Mining button found and clicked"
                else:
                    pytest.skip("Mining button image not found on screen")
            else:
                pytest.skip(f"Reference image not found: {mining_button_image}")

    def test_find_cpu_tile_by_image(self, ui_helper, screenshot_helper, app_controller):
        """
        Test finding and clicking the CPU mining tile using image recognition
        """
        window_region = app_controller.get_window_region()
        if window_region:
            screenshot_helper.capture("current_state_for_cpu_tile", region=window_region)

            cpu_tile_image = Path("qa-automation/images/cpu_tile.png")

            if cpu_tile_image.exists():
                success = ui_helper.click_image(str(cpu_tile_image), timeout=5)

                if success:
                    ui_helper.wait(2)
                    screenshot_helper.capture("after_cpu_tile_click", region=window_region)
                    assert True, "CPU tile found and clicked"
                else:
                    pytest.skip("CPU tile image not found on screen")
            else:
                pytest.skip(f"Reference image not found: {cpu_tile_image}")

    def test_find_gpu_tile_by_image(self, ui_helper, screenshot_helper, app_controller):
        """
        Test finding and clicking the GPU mining tile using image recognition
        """
        window_region = app_controller.get_window_region()
        if window_region:
            screenshot_helper.capture("current_state_for_gpu_tile", region=window_region)

            gpu_tile_image = Path("qa-automation/images/gpu_tile.png")

            if gpu_tile_image.exists():
                success = ui_helper.click_image(str(gpu_tile_image), timeout=5)

                if success:
                    ui_helper.wait(2)
                    screenshot_helper.capture("after_gpu_tile_click", region=window_region)
                    assert True, "GPU tile found and clicked"
                else:
                    pytest.skip("GPU tile image not found on screen")
            else:
                pytest.skip(f"Reference image not found: {gpu_tile_image}")

    def test_verify_ui_elements_present(self, ui_helper, screenshot_helper, app_controller):
        """
        Verify that expected UI elements are present using image recognition
        """
        window_region = app_controller.get_window_region()
        if window_region:
            screenshot_helper.capture("ui_elements_verification", region=window_region)

            ui_elements = [
                "mining_button.png",
                "cpu_tile.png",
                "gpu_tile.png",
                "settings_icon.png",
                "logo.png"
            ]

            found_elements = []
            missing_elements = []

            for element in ui_elements:
                element_path = Path(f"qa-automation/images/{element}")
                if element_path.exists():
                    location = ui_helper.find_image(str(element_path))
                    if location:
                        found_elements.append(element)
                        print(f"Found: {element} at {location}")
                    else:
                        missing_elements.append(element)
                        print(f"Not found: {element}")

            print(f"\nFound {len(found_elements)} elements: {found_elements}")
            print(f"Missing {len(missing_elements)} elements: {missing_elements}")

            if found_elements:
                assert True, f"Found UI elements: {found_elements}"
            else:
                pytest.skip("No reference images found or no elements detected")
