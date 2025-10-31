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
