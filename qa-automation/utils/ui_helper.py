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
UI interaction helper using PyAutoGUI
"""

import time
import pyautogui
from typing import Optional, Tuple


class UIHelper:
    """Helper class for UI interactions using PyAutoGUI"""

    def __init__(self, config):
        self.config = config
        self.pause = config.get('test.pause', 0.5)
        self.confidence = config.get('image_recognition.confidence', 0.8)
        self.default_timeout = config.get('test.default_timeout', 30)

        pyautogui.PAUSE = self.pause
        if config.get('test.fail_safe', True):
            pyautogui.FAILSAFE = True

    def click(self, x: int, y: int, clicks: int = 1, button: str = 'left') -> None:
        """
        Click at specific coordinates

        Args:
            x: X coordinate
            y: Y coordinate
            clicks: Number of clicks
            button: Mouse button ('left', 'right', 'middle')
        """
        pyautogui.click(x, y, clicks=clicks, button=button)
        time.sleep(self.pause)

    def double_click(self, x: int, y: int) -> None:
        """Double click at specific coordinates"""
        self.click(x, y, clicks=2)

    def right_click(self, x: int, y: int) -> None:
        """Right click at specific coordinates"""
        self.click(x, y, button='right')

    def move_to(self, x: int, y: int, duration: float = 0.5) -> None:
        """
        Move mouse to specific coordinates

        Args:
            x: X coordinate
            y: Y coordinate
            duration: Duration of movement in seconds
        """
        pyautogui.moveTo(x, y, duration=duration)

    def type_text(self, text: str, interval: float = 0.1) -> None:
        """
        Type text

        Args:
            text: Text to type
            interval: Interval between keystrokes
        """
        pyautogui.write(text, interval=interval)
        time.sleep(self.pause)

    def press_key(self, key: str) -> None:
        """
        Press a keyboard key

        Args:
            key: Key to press (e.g., 'enter', 'tab', 'esc')
        """
        pyautogui.press(key)
        time.sleep(self.pause)

    def hotkey(self, *keys: str) -> None:
        """
        Press a combination of keys

        Args:
            keys: Keys to press together (e.g., 'ctrl', 'c')
        """
        pyautogui.hotkey(*keys)
        time.sleep(self.pause)

    def find_image(self, image_path: str, confidence: Optional[float] = None) -> Optional[Tuple[int, int]]:
        """
        Find an image on screen

        Args:
            image_path: Path to the image to find
            confidence: Confidence threshold (0.0 to 1.0)

        Returns:
            Tuple of (x, y) coordinates if found, None otherwise
        """
        conf = confidence if confidence is not None else self.confidence

        try:
            location = pyautogui.locateOnScreen(image_path, confidence=conf)
            if location:
                center = pyautogui.center(location)
                return (center.x, center.y)
        except Exception as e:
            print(f"Error finding image {image_path}: {e}")

        return None

    def wait_for_image(
        self,
        image_path: str,
        timeout: Optional[int] = None,
        confidence: Optional[float] = None
    ) -> Optional[Tuple[int, int]]:
        """
        Wait for an image to appear on screen

        Args:
            image_path: Path to the image to find
            timeout: Timeout in seconds
            confidence: Confidence threshold

        Returns:
            Tuple of (x, y) coordinates if found, None if timeout
        """
        timeout = timeout if timeout is not None else self.default_timeout
        start_time = time.time()

        while time.time() - start_time < timeout:
            location = self.find_image(image_path, confidence)
            if location:
                return location
            time.sleep(1)

        return None

    def click_image(
        self,
        image_path: str,
        timeout: Optional[int] = None,
        confidence: Optional[float] = None
    ) -> bool:
        """
        Find and click an image

        Args:
            image_path: Path to the image to find and click
            timeout: Timeout in seconds
            confidence: Confidence threshold

        Returns:
            True if clicked, False if not found
        """
        location = self.wait_for_image(image_path, timeout, confidence)
        if location:
            self.click(location[0], location[1])
            return True
        return False

    def get_screen_size(self) -> Tuple[int, int]:
        """Get screen size"""
        return pyautogui.size()

    def get_mouse_position(self) -> Tuple[int, int]:
        """Get current mouse position"""
        return pyautogui.position()

    def scroll(self, clicks: int, x: Optional[int] = None, y: Optional[int] = None) -> None:
        """
        Scroll the mouse wheel

        Args:
            clicks: Number of clicks (positive for up, negative for down)
            x: Optional X coordinate
            y: Optional Y coordinate
        """
        if x is not None and y is not None:
            pyautogui.scroll(clicks, x=x, y=y)
        else:
            pyautogui.scroll(clicks)
        time.sleep(self.pause)

    def drag_to(self, x: int, y: int, duration: float = 0.5, button: str = 'left') -> None:
        """
        Drag mouse to specific coordinates

        Args:
            x: X coordinate
            y: Y coordinate
            duration: Duration of drag
            button: Mouse button to use
        """
        pyautogui.dragTo(x, y, duration=duration, button=button)
        time.sleep(self.pause)

    def wait(self, seconds: float) -> None:
        """Wait for specified seconds"""
        time.sleep(seconds)

    def find_text_on_screen(self, text: str) -> bool:
        """
        Check if text appears on screen (requires OCR)
        Note: This is a placeholder for OCR functionality

        Args:
            text: Text to search for

        Returns:
            True if found (currently always returns False as OCR is not implemented)
        """
        print(f"Text search not implemented: {text}")
        return False
