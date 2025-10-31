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
Screenshot helper for capturing test evidence
"""

import pyautogui
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple


class ScreenshotHelper:
    """Helper class for taking and managing screenshots"""

    def __init__(self, screenshot_dir: Path):
        self.screenshot_dir = screenshot_dir
        self.screenshot_dir.mkdir(parents=True, exist_ok=True)

    def capture(self, name: str, region: Optional[Tuple[int, int, int, int]] = None) -> Path:
        """
        Capture a screenshot

        Args:
            name: Base name for the screenshot
            region: Optional region to capture (x, y, width, height)

        Returns:
            Path to the saved screenshot
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = self.screenshot_dir / filename

        if region:
            screenshot = pyautogui.screenshot(region=region)
        else:
            screenshot = pyautogui.screenshot()

        screenshot.save(str(filepath))
        print(f"Screenshot saved: {filepath}")
        return filepath

    def capture_window(self, name: str, window_region: Tuple[int, int, int, int]) -> Path:
        """
        Capture a specific window region

        Args:
            name: Base name for the screenshot
            window_region: Window region (x, y, width, height)

        Returns:
            Path to the saved screenshot
        """
        return self.capture(name, region=window_region)

    def capture_on_failure(self, test_name: str) -> Path:
        """
        Capture a screenshot when a test fails

        Args:
            test_name: Name of the failed test

        Returns:
            Path to the saved screenshot
        """
        return self.capture(f"FAILED_{test_name}")
