# Tari Universe QA Automation

Comprehensive end-to-end UI automation testing framework for the Tari Universe desktop application using PyAutoGUI.

## Overview

This QA automation framework provides automated testing for the Tari Universe desktop mining application on Windows. It uses PyAutoGUI for GUI automation and supports both coordinate-based and image recognition-based testing.

## Features

- **Automated Application Launch**: Automatically starts and manages the Tari Universe application
- **Image Recognition**: Find and interact with UI elements using image matching
- **Screenshot Capture**: Automatic screenshot capture for test evidence and debugging
- **Comprehensive Test Coverage**: 
  - Smoke tests for basic functionality
  - Mining operation tests
  - UI navigation tests
  - Visual verification tests
  - Keyboard shortcut tests
  - Complete workflow tests
- **Flexible Configuration**: YAML-based configuration with environment variable support
- **Test Reporting**: HTML test reports with pytest-html

## Prerequisites

- Python 3.8 or higher
- Tari Universe application built and ready to run
- Windows OS (primary target, can be adapted for macOS/Linux)

## Installation

### 1. Install Python Dependencies

```bash
cd qa-automation
pip install -r requirements.txt
```

### 2. Configure the Framework

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and set the path to your Tari Universe executable:

```
APP_EXECUTABLE_PATH=C:/path/to/Tari Universe (Alpha).exe
```

Or edit `config.yaml` and set `app.executable_path`.

### 3. Capture Reference Images (Optional but Recommended)

For image recognition tests to work, you need to capture reference images of UI elements:

1. Build and run the Tari Universe application
2. Use a screenshot tool to capture UI elements
3. Save images to `qa-automation/images/`
4. See `images/README.md` for detailed instructions

## Running Tests

### Run All Tests

```bash
cd qa-automation
pytest
```

### Run Specific Test Categories

```bash
# Smoke tests only
pytest -m smoke

# Mining operation tests
pytest -m mining

# UI tests
pytest -m ui

# Regression tests
pytest -m regression
```

### Run Specific Test Files

```bash
pytest tests/test_smoke.py
pytest tests/test_mining_operations.py
pytest tests/test_ui_navigation.py
```

### Run with Verbose Output

```bash
pytest -v
```

### Skip Slow Tests

```bash
pytest -m "not slow"
```

## Test Structure

```
qa-automation/
├── config.yaml              # Main configuration file
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment variables
├── utils/                 # Utility modules
│   ├── __init__.py
│   ├── app_controller.py  # Application launch/control
│   ├── config_loader.py   # Configuration management
│   ├── screenshot_helper.py # Screenshot utilities
│   └── ui_helper.py       # PyAutoGUI wrapper
├── tests/                 # Test files
│   ├── conftest.py        # Pytest fixtures
│   ├── test_smoke.py      # Smoke tests
│   ├── test_mining_operations.py
│   ├── test_ui_navigation.py
│   ├── test_visual_verification.py
│   ├── test_keyboard_shortcuts.py
│   ├── test_image_recognition.py
│   └── test_comprehensive_workflow.py
├── images/                # Reference images for image recognition
│   └── README.md
├── screenshots/           # Test screenshots (auto-generated)
└── reports/              # Test reports (auto-generated)
```

## Configuration

### config.yaml

Main configuration file with settings for:
- Application paths and window settings
- Test timeouts and retry settings
- PyAutoGUI behavior settings
- Image recognition confidence thresholds
- Screenshot directory

### Environment Variables

Set in `.env` file:
- `APP_EXECUTABLE_PATH`: Path to Tari Universe executable
- `TEST_ENV`: Test environment (testnet/mainnet)
- `SKIP_APP_LAUNCH`: Set to 'true' to skip automatic app launch (for debugging)

## Test Development

### Creating New Tests

1. Create a new test file in `tests/` directory
2. Import required fixtures from `conftest.py`
3. Use pytest markers to categorize tests:
   - `@pytest.mark.smoke` - Basic functionality tests
   - `@pytest.mark.mining` - Mining-related tests
   - `@pytest.mark.ui` - UI interaction tests
   - `@pytest.mark.regression` - Regression tests
   - `@pytest.mark.slow` - Long-running tests

Example test:

```python
import pytest

@pytest.mark.smoke
def test_example(ui_helper, app_controller, screenshot_helper):
    """Example test"""
    window_region = app_controller.get_window_region()
    assert window_region is not None
    
    screenshot_helper.capture("example_test")
    # Your test logic here
```

### Using Image Recognition

```python
# Find an image on screen
location = ui_helper.find_image("images/button.png")

# Wait for an image to appear
location = ui_helper.wait_for_image("images/button.png", timeout=10)

# Find and click an image
success = ui_helper.click_image("images/button.png")
```

### Taking Screenshots

```python
# Capture full screen
screenshot_helper.capture("test_name")

# Capture specific region
screenshot_helper.capture("test_name", region=(x, y, width, height))

# Capture on test failure (automatic in conftest.py)
screenshot_helper.capture_on_failure("test_name")
```

## Troubleshooting

### Application Doesn't Launch

- Verify `APP_EXECUTABLE_PATH` is set correctly
- Check that the executable exists and is accessible
- Ensure no other instances are running
- Check application logs for startup errors

### Tests Fail to Find UI Elements

- Verify the application window is visible and not minimized
- Check window coordinates in screenshots
- Adjust `startup_wait` in config.yaml if app needs more time to load
- For image recognition: ensure reference images are captured correctly

### Image Recognition Not Working

- Check that reference images exist in `images/` directory
- Adjust `confidence` threshold in config.yaml (try 0.7 or 0.6)
- Recapture reference images at the same resolution
- Enable `grayscale` matching in config.yaml for faster matching

### Tests Are Too Slow

- Skip slow tests: `pytest -m "not slow"`
- Reduce `pause` time in config.yaml
- Reduce `startup_wait` if application starts quickly
- Run specific test files instead of full suite

### Screenshots Not Saving

- Check that `screenshot_dir` path is writable
- Verify disk space is available
- Check file permissions

## Best Practices

1. **Always capture screenshots** for test evidence
2. **Use descriptive test names** that explain what is being tested
3. **Add appropriate markers** to categorize tests
4. **Keep tests independent** - each test should work in isolation
5. **Use image recognition** for stable UI elements
6. **Use coordinates** for dynamic or frequently changing elements
7. **Add waits** after actions to allow UI to update
8. **Clean up** after tests (handled by fixtures)

## CI/CD Integration

To integrate with CI/CD pipelines:

1. Install dependencies in CI environment
2. Set `APP_EXECUTABLE_PATH` environment variable
3. Run tests: `pytest --html=reports/report.html`
4. Archive screenshots and reports as artifacts

Example GitHub Actions:

```yaml
- name: Install dependencies
  run: |
    cd qa-automation
    pip install -r requirements.txt

- name: Run tests
  env:
    APP_EXECUTABLE_PATH: ${{ github.workspace }}/path/to/app.exe
  run: |
    cd qa-automation
    pytest --html=reports/report.html

- name: Upload artifacts
  uses: actions/upload-artifact@v3
  with:
    name: test-results
    path: |
      qa-automation/screenshots/
      qa-automation/reports/
```

## Contributing

When adding new tests:

1. Follow existing test structure and naming conventions
2. Add appropriate markers
3. Include docstrings explaining what the test does
4. Capture screenshots for verification
5. Update this README if adding new features

## Support

For issues or questions:
- Check the troubleshooting section above
- Review test output and screenshots
- Check application logs
- Refer to PyAutoGUI documentation: https://pyautogui.readthedocs.io/

## License

This QA automation framework is part of the Tari Universe project and follows the same license.
