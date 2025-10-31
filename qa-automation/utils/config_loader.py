"""
Configuration loader for QA automation
"""

import os
import yaml
from pathlib import Path
from typing import Any, Dict
from dotenv import load_dotenv


class ConfigLoader:
    """Loads and manages configuration for QA automation"""

    def __init__(self, config_path: str = "qa-automation/config.yaml"):
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = {}
        self._load_config()
        self._load_env()

    def _load_config(self) -> None:
        """Load configuration from YAML file"""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        with open(self.config_path, 'r') as f:
            self.config = yaml.safe_load(f)

    def _load_env(self) -> None:
        """Load environment variables from .env file"""
        env_path = self.config_path.parent / '.env'
        if env_path.exists():
            load_dotenv(env_path)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value using dot notation
        Example: config.get('app.window_title')
        """
        keys = key.split('.')
        value = self.config

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default

        return value if value is not None else default

    def get_app_executable(self) -> str:
        """Get the application executable path"""
        env_path = os.getenv('APP_EXECUTABLE_PATH')
        if env_path:
            return env_path

        config_path = self.get('app.executable_path')
        if config_path:
            return config_path

        raise ValueError(
            "Application executable path not configured. "
            "Set APP_EXECUTABLE_PATH in .env or app.executable_path in config.yaml"
        )

    def get_screenshot_dir(self) -> Path:
        """Get the screenshot directory path"""
        screenshot_dir = Path(self.get('test.screenshot_dir', 'qa-automation/screenshots'))
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        return screenshot_dir
