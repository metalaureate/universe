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
Pytest configuration and fixtures for QA automation
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config_loader import ConfigLoader  # noqa: E402
from utils.app_controller import AppController  # noqa: E402
from utils.ui_helper import UIHelper  # noqa: E402
from utils.screenshot_helper import ScreenshotHelper  # noqa: E402


@pytest.fixture(scope="session")
def config():
    """Load configuration"""
    return ConfigLoader()


@pytest.fixture(scope="session")
def app_controller(config):
    """Create app controller"""
    return AppController(config)


@pytest.fixture(scope="session")
def ui_helper(config):
    """Create UI helper"""
    return UIHelper(config)


@pytest.fixture(scope="session")
def screenshot_helper(config):
    """Create screenshot helper"""
    return ScreenshotHelper(config.get_screenshot_dir())


@pytest.fixture(scope="session", autouse=True)
def launch_app(app_controller, config):
    """
    Launch the application before tests and close after
    This fixture runs automatically for all tests
    """
    import os
    if os.getenv('SKIP_APP_LAUNCH', '').lower() == 'true':
        print("Skipping app launch (SKIP_APP_LAUNCH=true)")
        yield
        return

    success = app_controller.launch()
    if not success:
        pytest.exit("Failed to launch application", returncode=1)

    yield

    app_controller.close()


@pytest.fixture(autouse=True)
def test_wrapper(request, screenshot_helper, app_controller):
    """
    Wrapper for each test to handle failures and screenshots
    """
    test_name = request.node.name
    print(f"\n{'='*60}")
    print(f"Starting test: {test_name}")
    print(f"{'='*60}")

    app_controller.focus_window()

    yield

    if request.node.rep_call.failed:
        print(f"Test failed: {test_name}")
        screenshot_helper.capture_on_failure(test_name)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to make test results available to fixtures
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
