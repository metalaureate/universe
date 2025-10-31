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
Application controller for launching and managing Tari Universe
"""

import subprocess
import time
import psutil
import pyautogui
from pathlib import Path
from typing import Optional, Tuple
import platform


class AppController:
    """Controller for launching and managing the Tari Universe application"""

    def __init__(self, config):
        self.config = config
        self.app_name = config.get('app.name', 'Tari Universe (Alpha)')
        self.window_title = config.get('app.window_title', 'Tari Universe (Alpha) | Testnet')
        self.startup_wait = config.get('app.startup_wait', 10)
        self.process: Optional[subprocess.Popen] = None
        self.window_region: Optional[Tuple[int, int, int, int]] = None

    def launch(self, executable_path: Optional[str] = None) -> bool:
        """
        Launch the Tari Universe application

        Args:
            executable_path: Path to the executable (optional, uses config if not provided)

        Returns:
            True if launched successfully, False otherwise
        """
        if executable_path is None:
            executable_path = self.config.get_app_executable()

        exe_path = Path(executable_path)
        if not exe_path.exists():
            print(f"Executable not found: {executable_path}")
            return False

        try:
            print(f"Launching {self.app_name}...")

            if platform.system() == 'Windows':
                self.process = subprocess.Popen([str(exe_path)])
            elif platform.system() == 'Darwin':  # macOS
                if exe_path.suffix == '.app':
                    self.process = subprocess.Popen(['open', str(exe_path)])
                else:
                    self.process = subprocess.Popen([str(exe_path)])
            else:  # Linux
                self.process = subprocess.Popen([str(exe_path)])

            print(f"Waiting {self.startup_wait} seconds for app to start...")
            time.sleep(self.startup_wait)

            self.window_region = self._find_window()

            if self.window_region:
                print(f"Application launched successfully. Window region: {self.window_region}")
                return True
            else:
                print("Warning: Could not locate application window")
                return True  # Still return True as process started

        except Exception as e:
            print(f"Error launching application: {e}")
            return False

    def _find_window(self) -> Optional[Tuple[int, int, int, int]]:
        """
        Find the application window

        Returns:
            Tuple of (x, y, width, height) if found, None otherwise
        """
        screen_width, screen_height = pyautogui.size()
        window_width = self.config.get('app.window_width', 1300)
        window_height = self.config.get('app.window_height', 731)

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        return (x, y, window_width, window_height)

    def close(self) -> bool:
        """
        Close the application gracefully

        Returns:
            True if closed successfully, False otherwise
        """
        try:
            if self.process:
                print(f"Closing {self.app_name}...")

                if platform.system() == 'Windows':
                    pyautogui.hotkey('alt', 'F4')
                else:
                    if platform.system() == 'Darwin':
                        pyautogui.hotkey('command', 'q')
                    else:
                        pyautogui.hotkey('alt', 'F4')

                time.sleep(3)

                if self.process.poll() is None:
                    print("Force terminating process...")
                    self.process.terminate()
                    time.sleep(2)

                    if self.process.poll() is None:
                        self.process.kill()

                self.process = None
                print("Application closed")
                return True

            return True

        except Exception as e:
            print(f"Error closing application: {e}")
            return False

    def is_running(self) -> bool:
        """
        Check if the application is running

        Returns:
            True if running, False otherwise
        """
        if self.process:
            return self.process.poll() is None

        for proc in psutil.process_iter(['name']):
            try:
                if self.app_name.lower() in proc.info['name'].lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        return False

    def restart(self) -> bool:
        """
        Restart the application

        Returns:
            True if restarted successfully, False otherwise
        """
        self.close()
        time.sleep(2)
        return self.launch()

    def get_window_region(self) -> Optional[Tuple[int, int, int, int]]:
        """
        Get the application window region

        Returns:
            Tuple of (x, y, width, height) if available, None otherwise
        """
        return self.window_region

    def focus_window(self) -> None:
        """Bring the application window to focus"""
        if self.window_region:
            x, y, width, height = self.window_region
            pyautogui.click(x + width // 2, y + 50)
            time.sleep(0.5)

    def kill_all_instances(self) -> None:
        """Kill all running instances of the application"""
        print(f"Killing all instances of {self.app_name}...")

        for proc in psutil.process_iter(['name', 'pid']):
            try:
                if self.app_name.lower() in proc.info['name'].lower():
                    print(f"Killing process {proc.info['pid']}: {proc.info['name']}")
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                print(f"Could not kill process: {e}")
