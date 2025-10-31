#!/usr/bin/env python3
"""
Convenience script to run QA automation tests
"""

import sys
import subprocess
from pathlib import Path


def main():
    """Run pytest with common options"""
    qa_dir = Path(__file__).parent
    
    cmd = [
        sys.executable, "-m", "pytest",
        "-v",
        "--tb=short",
        "--html=reports/test_report.html",
        "--self-contained-html"
    ]
    
    cmd.extend(sys.argv[1:])
    
    print(f"Running tests from: {qa_dir}")
    print(f"Command: {' '.join(cmd)}")
    print("-" * 60)
    
    result = subprocess.run(cmd, cwd=qa_dir)
    
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
